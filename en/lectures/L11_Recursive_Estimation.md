---
lecture: L11
title: "Recursive Estimation"
course: Identification
source: "https://www.youtube.com/watch?v=cTlkFkwKV4U"
---

# L11 — Recursive Estimation

> Formulas verified against the lecturer's slide deck (*L Identifikácia, L11 —
> 30. 04. 2024*). Note: on camera the lecturer momentarily wrote the slope estimate
> as $\sum y_k / \sum x_k$; the slide (and the recursion he then derives) uses the
> correct least-squares form $a_N = \frac{\sum y_k x_k}{\sum x_k^2}$, used below.

## The problem

We have a plant/process/system for which, from an experiment, we built a model
that predicts the historical data. Deployed in industry, the model should predict
future outputs for whatever inputs, so the **prediction error** should be
approximately zero:

$$
e \approx 0
$$

(the difference between the system's measured output $y_k^{\text{meas}}$ and the
model's prediction $\hat{y}_k$). **Recursive estimation** addresses the case when
this does **not** happen and the model must **adapt online**.

## Bias update

Suppose the historical (nominal) data was well fit, but in a region of the
independent variables not explored in training, the real plant evolves with an
almost **constant systematic error** (e.g. nonlinearity, or a changed reactant
supplier). The **slope** still looks correct (the dependent variable still reacts
the same way), and we cannot change the independent variables — so we only adjust
the **bias / offset** $b$ to absorb the constant shift. This is the simplest
recursive estimation, the **bias update**, much used in industry (companies prefer
not to change verified slopes/dependencies).

The bias becomes a function of time. The previous prediction

$$
\hat{y}_{k-1} = a x_{k-1} + b_{k-1}
$$

is compared with the actual measurement $y_{k-1}$, and we update the bias by the
prediction error:

$$
b_k = b_{k-1} + \big(y_{k-1} - \hat{y}_{k-1}\big)
$$

This shifts the line to the new operating point.

### Filtered bias update

Reacting to a single measurement is **myopic** (one noisy point swings the bias).
Add **filtering** with a parameter $\delta \in [0, 1]$ acting as a **trust gain**:

$$
b_k = \delta\, b_{k-1} + (1 - \delta)\,(\text{prediction-error term})
$$

<!-- the exact combination was stated loosely; delta weights the old bias against the new error-based correction -->

- $\delta$ close to **1**: we do **not trust** recent measurements much; the bias
  changes little, but a sustained trend gradually accumulates and slowly shifts the
  line to a new operating point.
- $\delta = 0$: the estimate is driven **entirely** by the new measurement.

This $\delta$ is like the gain of a **P controller**, where the control action
changes by gain × control error (slide):

$$
u_k = K\, e_k = K\,(w_k - y_k)
$$

Here, instead, the **estimate** changes by gain × **prediction error**.

## Updating the slope: recursive least squares (scalar)

Now the case where the **dependencies** themselves must change. Take the simplest
linear-regression setup ($b = 0$, scalar $a$), $y_k = a x_k$. The least-squares
estimate from $N$ measurements and from $N-1$ measurements (slide):

$$
a_N = \frac{\sum_{k=1}^{N} y_k x_k}{\sum_{k=1}^{N} x_k^2},
  \qquad
  a_{N-1} = \frac{\sum_{k=1}^{N-1} y_k x_k}{\sum_{k=1}^{N-1} x_k^2}
$$

Taking all $N$ (e.g. a thousand or a million) historical values each time is
impractical (large matrix inversions in the multidimensional case), and there is a
**pattern**: the new value should be the old value plus a (filtered) correction.

### Deriving the recursion

Split off the last term in the numerator and denominator,
$\sum_{k=1}^{N} = \sum_{k=1}^{N-1} + (\text{term } N)$, and substitute
$\sum_{k=1}^{N-1} y_k x_k = a_{N-1}\sum_{k=1}^{N-1} x_k^2$:

$$
a_N = \frac{a_{N-1}\sum_{k=1}^{N-1} x_k^2 + y_N x_N}{\sum_{k=1}^{N} x_k^2}
$$

To recover $a_{N-1}$ times the **full** sum, **add and subtract** $a_{N-1} x_N^2$
("fake it till you make it"):

$$
a_N = \frac{a_{N-1}\sum_{k=1}^{N} x_k^2 + y_N x_N - a_{N-1} x_N^2}
             {\sum_{k=1}^{N} x_k^2}
$$

Separating $a_{N-1}$ gives the **recursive update**:

$$
a_N = a_{N-1} + \frac{x_N}{\sum_{k=1}^{N} x_k^2}\,\big(y_N - a_{N-1} x_N\big)
$$

The structure mirrors the bias update and the controller:

- $y_N$ is the **measurement** just taken.
- $a_{N-1} x_N$ is the **prediction of the old (un-updated) model** — the
  prediction at time $N$ based on information available until time $N-1$, written
  $\hat{y}_{N\mid N-1}$. So $(y_N - a_{N-1}x_N)$ is the **prediction error**.
- $\dfrac{x_N}{\sum_{k=1}^{N} x_k^2}$ is the **gain** — how much we trust the new
  measurement.

### The gain shrinks automatically (and forgetting)

Unlike the bias update, the gain is **not** our free choice. Starting out with one
measurement ($x = 1$) the gain is 1; after 100 measurements (all $x = 1$) it is
$\tfrac{1}{100}$ — much smaller. This is desirable: $a_{N-1}$ already carries the
information of $N-1$ points, which we do not want erased by one possibly-noisy
measurement.

But if 10 years of data dictate a correlation and only ~5 recent measurements
contradict it, we can **limit** the past data — use only the last month or half
year. This is a **shortened time window for more recent updates** (forgetting),
tuned by how much the process can change.

## Recursive least squares: general (vector) case

In general the prediction model is $y = X p$, with the regressor (row) vector
$\phi_N$ for sample $N$ giving $y_N = \phi_N^T p$. The same line of reasoning yields
the vector recursion (slide):

$$
p_N = p_{N-1} + P_N^{-1}\,\phi_N\,\big(y_N - \phi_N^T p_{N-1}\big)
$$

with the **covariance** matrix accumulating as

$$
P_N = P_{N-1} + \phi_N\,\phi_N^T \quad\longrightarrow\ \text{covariance}
$$

(equivalently the gain is $(X^T X)^{-1} x_N$ in the earlier notation). The
ingredients are again the same:

- the **prediction error** $\big(y_N - \phi_N^T p_{N-1}\big)$;
- the **a priori knowledge** $p_{N-1}$ (the previous parameter estimate);
- the **gain** $P_N^{-1}\phi_N$ — built from the covariance matrix (the accumulated
  $X^T X$ of historical $x$ values) and its inverse, so as the number of past
  values grows the gain **shrinks**.

(Over time, the estimate $p$ converges toward the real $p^{*}$, with a shrinking
confidence band around it.)

## Connection to the Kalman filter

With more time, this is one step away from a **state estimator**. For a
state-space model

$$
x_k = A x_{k-1} + B u_{k-1}
$$

a corrected estimate of the form

$$
\hat{x}_k = A \hat{x}_{k-1} + B u_{k-1} + K\big(y_k - C \hat{x}_k\big)
$$

with a wisely chosen gain $K$ (the **Kalman gain**) becomes the **Kalman filter** —
which estimates the **states** of a dynamic system rather than the parameters. The
idea is identical: from the previous prediction (at time $k-1$) we predict $x_k$;
we measure something about the state; and we correct using a **gain matrix** times
the measurement discrepancy.

*(This concludes the course.)*
