---
lecture: L05
title: "Linear Regression #1"
course: Identification
source: "https://www.youtube.com/watch?v=J6QAT6-BkDY"
---

# L05 — Linear Regression #1

> Formulas verified against the lecturer's slide deck (*Ident 17 03 2026 / 24 03
> 2026*); where the caption garbled an expression (notably the slope confidence
> interval and the standardization) it was reconstructed from the slide and noted.

## From estimating a constant to linear regression

Last lecture we did a thousand experiments measuring one constant quantity with
measurement noise, and found the **arithmetic mean** is the best estimator,
getting closer to the true value as the number of measurements grows. In another
view, we built a **histogram** of the data and **fit a normal (Gaussian)
distribution** (two parameters: mean and standard deviation), estimating the
constant and reflecting the uncertainty.

Today the picture changes slightly: we still do several experiments, but now there
is a quantifiable **difference between experiments**, captured by an independent
variable $x$. Practical example (also in the exercises): take measurements of some
gas at different **temperatures** $x$ and record the corresponding **pressures**
$y$. If we rotate/tilt the previous picture, the task is similar — we look for a
**mean value, but now a curve** depending on $x$. Along that line we again imagine
a "mini-Gaussian," take every measurement into account, and find the **maximum
likelihood estimate**, which we know equals the **least-squares estimate**.

## The linear regression model

Each $k$-th observation is explained by a **model / prediction** plus the
**uncertainty** (measurement noise). For linear regression the model is as simple
as possible — a **line** parameterized by two values:

$$
\hat{y}_k = a\,x_k + b
$$

- $a$ — the **slope**.
- $b$ — the **abscissa intercept** / **offset** / **bias**. If the slope is zero,
  this reduces to the **estimation of a constant** from last time.

(More generally the slide also writes $\hat{y} = \hat{p}\,f(x)$.) The assumption
from last week remains: with no error we would measure points exactly on the line;
the error is **Gaussian / normally distributed** with **zero mean** (the sensor is
right on average) and some standard deviation:

$$
e \sim N(0, \sigma^2)
$$

## Why "regression"? (Galton)

"Regression" means deterioration / something going wrong. The name is inherited
from **Galton**, a biologist, who plotted the **height of a parent** vs. the
**height of a child**. One expects $y = x$ (tall parents → tall children, short
parents → short children), but the real data showed a **deviation**: tall parents
had children slightly **shorter**, and short parents had children slightly
**taller** than expected. He concluded the height of the population turns toward
the mean — the children's height is **"regressing toward the mean,"** and the term
stuck.

## Least squares: the two normal equations

Data are pairs $(x_k, y_k)$, $k = 1, \dots, N$. Find $a$ and $b$ by least squares
(the $\tfrac{1}{2}$ multiplier is included for convenience):

$$
\min_{a,b}\; \frac{1}{2}\sum_{k=1}^{N}\big(a\,x_k + b - y_k\big)^2
$$

Differentiate with respect to $a$ and $b$ (the $x_k, y_k$ are numbers) and set to
zero. The derivative of a sum is the sum of derivatives; for the square we get
twice the bracket times the derivative of the bracket interior:

$$
\frac{\partial}{\partial a} = 0 = \frac{1}{2}\sum_{k=1}^{N} 2\,x_k\,(a\,x_k + b - y_k)
$$

$$
\frac{\partial}{\partial b} = 0 = \frac{1}{2}\sum_{k=1}^{N} 2\,(a\,x_k + b - y_k)
$$

The constant $\tfrac{1}{2}$ and the $2$ cancel. Splitting each bracket into
separate sums (and using $\sum_{k=1}^{N} b = N b$):

$$
0 = a\sum_{k=1}^{N} x_k + bN - \sum_{k=1}^{N} y_k
$$

$$
0 = a\sum_{k=1}^{N} x_k^2 + b\sum_{k=1}^{N} x_k - \sum_{k=1}^{N} y_k x_k
$$

### The bias has a simple form

From the first equation, isolating $b$ (move $-Nb$ over, divide by $N$) gives only
**arithmetic means**:

$$
b = \frac{1}{N}\sum_{k=1}^{N} y_k - a\,\frac{1}{N}\sum_{k=1}^{N} x_k
    = \bar{y} - a\,\bar{x}
$$

"Once you see the arithmetic mean, you cannot unsee it."

### Matrix form $Mp = r$

Both equations have the structure constant $+\,a\cdot(\text{const}) +
b\cdot(\text{const})$, so write them as a linear algebraic system $Mp = r$ with
$p = \binom{a}{b}$, solved in MATLAB as `p = M\r` (confirmed on the slide):

$$
\begin{pmatrix}
\sum_{k=1}^{N} x_k & N \\
\sum_{k=1}^{N} x_k^2 & \sum_{k=1}^{N} x_k
\end{pmatrix}
\begin{pmatrix} a \\ b \end{pmatrix}
=
\begin{pmatrix}
\sum_{k=1}^{N} y_k \\
\sum_{k=1}^{N} y_k x_k
\end{pmatrix}
$$

The matrix $M$ contains only the data ($x$); the right-hand side mixes $y$ and $x$.

## Centering and standardizing the data

Starting from $y = a x + b$ and substituting $b = \bar{y} - a\bar{x}$:

$$
y = a x + \bar{y} - a\bar{x}
  \quad\Longrightarrow\quad
  y - \bar{y} = a\,(x - \bar{x})
$$

So if we **transform the data first**, the bias disappears. Define (slide):

- **Centered data:** $\tilde{x} = x - \bar{x}$, $\tilde{y} = y - \bar{y}$
  (subtract the mean — shift the cloud of points so the origin sits at its
  center). Then $\tilde{y} = a\,\tilde{x}$ (no intercept).
  Example: $x = 1,2,3,4,5 \Rightarrow \tilde{x} = -2,-1,0,1,2$.
- **Standardized (normalized) data:** also divide by the standard deviation

$$
\tilde{x} = \frac{x - \bar{x}}{\sigma_x}, \qquad
    \tilde{y} = \frac{y - \bar{y}}{\sigma_y}
$$

  with $\sigma = \sqrt{\dfrac{1}{N-1}\sum_{k=1}^{N}(x_k - \bar{x})^2}$ (Bessel
  correction). The standardized variables have **zero mean and standard deviation
  one**. <!-- The caption's algebra here was garbled; the slide gives the clean centered/standardized definitions used above. -->

**Why center?** We can directly see whether the correlation is **positive or
negative** (a positive $x$ pairing with a positive $y$ → positive slope), which is
hard to read off raw axes like Kelvin (250–350) vs. pascals.

**Why standardize?** Different variables have wildly different spreads — pressure
in pascals ($10^5$–$10^6$) vs. temperature (a 100 K span) — making the slope hard
to compare. After standardization the normalized slope $a_n$ lands in the order of
$[-1, 1]$, so with several independent variables you can **compare the strength of
correlations**: the closer $|a_n|$ is to 1, the more strongly the measured
variable depends on that independent variable. The lecturer stresses that
**normalization / standardization** saves enormous time in any data task (not just
identification); "standardization" specifically means zero mean and unit standard
deviation.

## Confidence interval for the slope

As last week (where we standardized the estimation error to use the chi-square
statistic), we can build a confidence interval for the slope. With the estimate
$\hat{a}$ obtained from `M\r`, an $\alpha$ level of probability (e.g. 95%), and the
chi-square quantile, the true slope $a^*$ lies in (slide):

$$
\hat{a} - \frac{\hat{\sigma}}{\sqrt{N}}\,\chi^{-1}_{\alpha}
  \;\le\; a^* \;\le\;
  \hat{a} + \frac{\hat{\sigma}}{\sqrt{N}}\,\chi^{-1}_{\alpha}
$$

where $\chi^{-1}_{\alpha}$ is the inverse CDF (quantile) of the chi-square
distribution (a single MATLAB command), and $\hat{\sigma}$ is the standard
deviation of how the model fits the data:

$$
\hat{\sigma} = \sqrt{\frac{1}{N-1}\sum_{k=1}^{N}(\hat{y}_k - y_k)^2}
$$

This is the **root mean squared error (RMSE)** (sometimes just MSE, the mean
squared error, without the root). RMSE is practical because, like a standard
deviation, it lives in the same units as the data — "our model is off by 0.01 bar."

## Toward multivariable regression — matrix/vector notation

With more parameters the sum-based matrices grow, so we move to **matrix/vector
notation**. In general we measure several independent variables — e.g. temperature
$T$, concentration $C$, and even a transformation like $T^2$. A model such as

$$
\hat{y} = a_1 T + a_2 C + a_3 T^2 + \dots
$$

is still **linear in the parameters**, so linear regression still applies (a
**model linear in parameters**). But carrying sums of $T$, $C$, $T^2$, $T\cdot y$,
etc. quickly becomes impractical.

### The regressor matrix

Arrange the data so each **column** is one independent variable (or its
transformation) and each **row** is one experiment. With $N$ experiments and $P$
variables, the **regressor matrix** $X$ has dimensions $N \times P$ (the lecturer
deliberately writes columns first because, in practice, there may be ~200
variables but ~16,000 measurements (e.g. 15-minute data over a year), so the
columns, representing each physical variable, matter more). Lowercase $x$ denotes
a single data **vector** (one column); capital $X$ is the full matrix. The output
$y$ is assumed to be a single measured quantity, so it stays a **vector**.

### Useful vector identities (confirmed on the slide)

For $x = (x_1, \dots, x_N)^T$ and the all-ones vector $\mathbf{1}$:

$$
x^T x = x_1^2 + x_2^2 + \dots + x_N^2 = \sum_{k=1}^{N} x_k^2
$$

$$
\mathbf{1}^T x = x^T \mathbf{1} = \sum_{k=1}^{N} x_k, \qquad
  \mathbf{1}^T y = \sum_{k=1}^{N} y_k, \qquad
  x^T y = \sum_{k=1}^{N} x_k y_k
$$

Note matrix multiplication does not commute, $A B \ne B A$, but for vectors
$a^T b = b^T a$.

Using these, the two normal equations collapse: $\sum x_k^2 \to x^T x$,
$\sum y_k x_k \to y^T x$, $\sum x_k \to \mathbf{1}^T x$, $\sum y_k \to
\mathbf{1}^T y$, and $N$ stays $N$.

### The matrix model and the least-squares problem

The model in matrix form uses the regressor matrix $X$ ($N \times P$) and the
parameter vector $p$ ($P \times 1$):

$$
\hat{y} = X p
$$

so $\hat{y}$ is $N \times 1$ — one prediction per experiment, the same size as the
measured data. Pose finding $p$ as a least-squares problem, writing the sum of
squared differences in vector form (transpose-times-itself, as $x^T x = \sum
x_k^2$):

$$
\min_{p}\; \frac{1}{2}\,(y - \hat{y})^T (y - \hat{y})
$$

**Next time** we substitute $\hat{y} = X p$ and derive the solution, which will
have the form $p = (\text{matrix})^{-1}(\text{matrix})\,(\text{vector})$ — the
normal equations. (Useful prerequisite: the transpose of a product,
$(AB)^T = B^T A^T$.)
