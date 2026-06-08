---
lecture: L10
title: "Practical Aspects of Identification"
course: Identification
source: "https://www.youtube.com/watch?v=uuRbAaWFfmQ"
---

# L10 — Practical Aspects of Identification

> Transcript-only (no matching slide deck for this lecture). Formulas are typeset
> as spoken; where a sum limit or expression was not fully stated it is marked.

## One more dynamic model: ARMAX

Last time we covered FIR (predicts the output only from the **inputs**) and the
**ARX** model (easily represents linear discrete-time transfer functions). One more
model extends ARX: the **ARMAX** model — **AutoRegressive Moving Average with
eXogenous input** — combining ARX with a **moving average (MA)** term. Its
prediction equation:

$$y_k = -\sum_{i=1}^{n} a_i\, y_{k-i}
        + \sum_{i=1}^{m} b_i\, u_{k-i}
        + \sum_{i=1}^{n_c} c_i\, e_{k-i}$$

<!-- the upper limit of the MA (c) sum is not explicitly stated in the lecture -->

The three parts: the **autoregressive** part ($a_i$, past outputs), the
**exogenous input** part ($b_i$, past inputs), and the new **moving average** part
($c_i$, past **errors** $e_{k-i}$).

### What the error term does

The error $e_{k-i}$ uses only **past** measured data (the index $k-i$). It captures
the **discrepancy** between what was predicted in the past and what was actually
measured afterward. So ARMAX is **not** the train-once-on-a-year-of-data-and-let-it
-run type — it **corrects itself while running**, doing a moving average of the
previous errors.

**Why useful?** When identifying ARX/FIR from historical data we collect
input–output pairs but **neglect disturbances** (e.g. a **leaking valve**). If a
disturbance is **measured** (e.g. an ambient-temperature sensor), it can become a
model input, predicted via a weather forecast. If it is **unmeasured** (e.g. a
different feed quality changing reactor conditions, which nobody reports), ARMAX
tries to **detect and learn** it: the $c$ coefficients absorb the **systematic
errors** from disturbances, **freeing** the $a$ and $b$ coefficients to learn the
**true plant dynamics**.

**Training and prediction.** ARMAX often needs **nonlinear optimization** to fit.
To predict into the **future** (where the errors $e_k$ are unknown), one usually
assumes $e_k$ follows a **normal distribution with zero mean** and some variance —
not necessarily the best choice, but it lets you treat the mean case as "no
disturbance" and build scenarios for $\pm 1\sigma, 2\sigma, 3\sigma$ disturbances.

## The system-identification algorithm

Given a black-box device, find a mathematical model of its behavior. The steps
(with feedback loops):

### 1. Prior knowledge

Before anything, get **prior knowledge** — read the manual, ask people. Plants have
many undocumented features. This tells you what to expect (fast/slow), guiding the
experiment.

### 2. Experiment design

Decide the inputs, how long the experiment runs, when to change inputs. This is a
whole field (design of experiments). A key choice is the **input signal shape**:

- A simple **step** can reach steady state and reveal a dominant time constant, but
  a **fast pole** may be completely hidden (especially under noise), and you cannot
  tell first vs. second order easily.
- A **short, almost-impulse** input: a **slow** pole barely reacts (no time to
  rise), but a **fast** pole shows at least something (visible to the mathematics /
  standard deviation, if not the eye).
- A long step reveals the slow pole.

Combining short and long steps that jump between levels is the idea behind the
**pseudo-random binary sequence (PRBS)** — it jumps between two levels (e.g. 0 and
1, or any two values). Generating random numbers and thresholding gives this shape.
PRBS excites both fast and slow dynamics.

### 3. Data collection and pre-processing

Collect and pre-process: **standardization**, checking magnitudes, removing
**outliers**, producing a clean data set.

### 4. Choose the model set

Decide the model **structure**, using prior knowledge:

- **Static vs. dynamic.** Test with step changes of, e.g., $\tfrac{1}{3},
  \tfrac{2}{3}, 1$ (or 1, 2, 3) and inspect the steady-state outputs:
  - **Proportional** outputs → a **static gain** (a steady-state equation) suffices.
  - **Non-proportional but same-sign** gain → **nonlinear but bearable** (the gain
    changes size but not sign) — solvable with integral control action.
  - **Gain changes sign** → **red alert**: strongly nonlinear, essentially
    impossible to control with a linear controller (even LQR fails).
  - An **immediate scaled step** with no transient → no pole/zero information; use a
    **static** model (or it is a discrete system with a large period); no point
    fitting a dynamic ARMAX — the numbers would not represent anything, as the
    validation/testing data would soon reveal.
  - (This means the deciding step changes must already be planned into the original
    experiment; processes often have feedback loops.)
- Also decide the **model order** and whether to include an **input delay**.

#### Unstable systems

For a **stable** system we are in well-charted territory. For an **unstable**
system we must first **design a stabilizing controller** — a chicken-and-egg
problem (need the model to design the controller, need the controller to get data).
If the plant has run in production for years, a stabilizing controller may already
exist. We then **put the controller and plant in one box** and identify the
**closed loop** (reference → response), because the open-loop steady-state data
reveals nothing about time constants, delays, poles, zeros.

Example with a **P controller** $G_C = K_R$ and plant $G_S = \dfrac{K}{Ts+1}$
(where a **negative** time constant $T$, i.e. a positive pole, makes it unstable).
The closed-loop characteristic equation (after a common denominator):

$$T s + 1 + K_R K = 0$$

Choosing the right $K_R$ (here likely negative if $K$ is positive) can push the
unstable pole to be **stable**. The closed-loop relation (reference → response) has
two unknown parameters that can be transformed to discrete time and **fitted as an
ARX model**.

### 5. Choose the fitting criterion

Decide whether **least squares** is acceptable: least squares is appropriate when
the noise is **Gaussian** (normally distributed). For many outliers, a **sum of
absolute values** criterion helps.

### 6. Fit the model

With all three ingredients — the **model set**, the **data**, and the **fitting
criterion** — finally **fit (calculate) the model**.

### 7. Test the model, and the feedback loops

**Test / validate** the model. A good model should come with a **"certificate"**:
the domain it was trained in and the math it uses — **use with caution, never
outside that domain**. If the model is **not good enough**, loop back to:

- **redesign the experiment** (e.g. we fitted a stable model to an unstable plant
  because of a wrong experiment/model set), or
- **change the fitting criterion** (e.g. switch to sum of absolute values if
  outliers cannot be discarded).

## Choosing the model order: correlation analysis

In the static case we chose regressors (pressure, temperature, …) via
**correlation analysis** — roughly, summing the centered products of an input with
the output (and normalizing to get a correlation coefficient). In the **dynamic**
case the model terms represent **past data**, so the task is similar: which **past
values** (lags) should the model include — the first, second, …, but maybe not the
third?

### Autocorrelation function (ACF)

We compare a signal with **itself shifted in time**: is $y_k$ correlated with the
value one sample earlier? Take a copy of the signal, shift it **backwards** in
time, and compute the correlation coefficient of the signal with its shifted copy —
the **autocorrelation** (Slovak intuition: "Inception"). Repeating for shifts of 1,
2, 3, … samples gives the **autocorrelation function (ACF)**, available in MATLAB /
Python. Conceptually (centered products, normalized):

$$\text{ACF}(i) \;\sim\; \frac{1}{N}\sum_{k}(y_k - \bar{y})(y_{k-i} - \bar{y})$$

<!-- the exact normalization was not fully written on the board; the function normalizes so ACF(0)=1 -->

Reading the MATLAB ACF stem plot:

- Horizontal axis = the **lag** (the shift $i$, intuitively the delay).
- **ACF(0) = 1** always — the signal is 100% correlated with itself (the function
  standardizes the data).
- The **blue band** is an internally computed **±3σ** noise interval — ignore any
  stems lying inside it.

### Partial autocorrelation function (PACF)

The **partial autocorrelation function (PACF)** is similar, but when computing the
correlation at a lag it **removes** the correlation already explained by the
**intermediate** (e.g. unit-delay) shifts (a crude description of the idea).

### Examples

- **Gaussian noise input** (mean ≈ 0, σ ≈ 1): each sample is independent of the
  previous (like rolling a dice), so the ACF shows only the spike at lag 0; all
  other stems lie in the band — **no correlation**.
- **Second-order FIR (moving average)** output, e.g. $y_1 = \tfrac{1}{2}u_1 +
  \tfrac{1}{2}u_0$, $y_2 = \tfrac{1}{2}u_2 + \tfrac{1}{2}u_1$: the ACF has **one
  significant value at lag 1**, because $y_1$ and $y_2$ share the common input
  $u_1$. This suggests $y_k$ is a function of $u_{k-1}$ — a dynamic model shifted at
  least one sample back. The PACF is not very informative here with only 100
  samples.
- **First-order ARX**, e.g. $y_1 = \tfrac{9}{10}y_0 + \tfrac{1}{10}u_0$, $y_2 =
  \tfrac{9}{10}y_1 + \dots = \tfrac{81}{100}y_0 + \dots$: the ACF shows correlation
  over **many** lags (the output is influenced by the initial condition even ~10
  steps later), so it may **over-suggest** a high order (5th, 10th). The **PACF**
  cleanly suggests **first order** by removing the carried-over correlation — so for
  AR/transfer-function-type models the **PACF is better for selecting the order**.
- **Input shape matters.** The same first-order system with a $0,1,0,1,\dots$ input
  (instead of PRBS) confuses the analysis (the input jumps far between consecutive
  steps); PRBS, where consecutive inputs stay closer, behaves much better. The ACF
  still shows dynamic behavior; ignore a slightly distracted PACF unless there is
  genuine seasonality.
- **Second-order dynamics** with Gaussian-noise or PRBS input: the ACF shows much
  self-correlation, but the **PACF clearly suggests taking two past values** —
  select **second order**.

Combine correlation analysis with **cross validation** (training / validation /
testing data) to be sure the selected model order is correct.
