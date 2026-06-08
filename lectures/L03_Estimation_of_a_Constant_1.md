---
lecture: L03
title: "Estimation of a Constant #1"
course: Identification
source: "https://www.youtube.com/watch?v=G6Auo4Mw_V0"
---

# L03 — Estimation of a Constant #1

## Warm-up: guessing the parameters of generated data

Building on the previous exercises (generating random numbers and plotting them):
given several samples — rolling a dice, measuring a temperature, a pressure,
anything — each experiment is marked with its value. Looking at such generated
data (1,000 samples), what mean and standard deviation generated it?

- The **mean** looks like it should be around **1**.
- For the **standard deviation**, use the **3σ band**: from last week, within
  $\pm 3\sigma$ lie about **99.73%** of values, so almost all values should lie in
  that band. If the full spread is about **0.6** (half is **0.3**), and that
  equals **three** standard deviations, then **one** standard deviation is
  **0.1** — which is exactly what generated the distribution.

## The problem: estimation of a constant

This is the **estimation of a constant** — essentially finding the **mean** — and
also studying the **properties** of that mean as we take **more and more
samples**.

We measure data and want to compute a single constant. We can estimate the mean
"on the fly": take the first 10 samples and estimate the mean, then 50 samples,
etc., and watch how the estimate tends toward the true mean. Notation: the true
constant $\bar{y}$ (or $\hat{y}$, the hat denoting an **estimate**), which changes
with time as more samples arrive.

### Statistical model

If the data obey a normal distribution — i.e. any discrepancy/error comes from a
Gaussian/normal distribution — the model is a simple **statistical model**: the
true constant equals the estimated mean plus some error (because we did not run a
million experiments):

$$y = \bar{y} + e$$

The measurements are normally distributed about a mean value $\bar{y}$ (whose true
value we may never reach) with some variance/standard deviation. By taking care of
the mean (estimating it), the **error** is then normal with **zero mean** and some
standard deviation:

$$e \sim N(0, \sigma^2)$$

### Notation for samples in time

Measurements arrive at times $t_1, t_2, t_3, \dots$; using the subscript notation
you will soon see in Theory of Automatic Control (discrete-time systems), we drop
the explicit time and just write experiment number 1, 2, 3, …

If there were **no noise**, every experiment would consistently measure the true
constant (e.g. the current room temperature). With noise, the points scatter, and
the mean of, say, three measurements does not land exactly on $\bar{y}$ — if two
of the points lie above the true value, the estimated mean is slightly off.

## Where this is used

- **Torricelli's law / a valve constant.** With a tank we can measure the height
  $H$ and an outflow $Q$. We may not know the valve constant, so we set up several
  experiments, measure $H$ and $Q$ each time, and compute the constant as

  $$C = \frac{Q}{\sqrt{H}}$$

  Different experiments give scattered values; we want the statistically best one.

- **Static gain / time constants of a transfer function.** From several step
  tests (or steady-state input/output pairs), the **static gain** is

  $$Z = \frac{\Delta y}{\Delta u}$$

  i.e. a column of input changes and a column of output changes. For a nonlinear
  system the time constant is not even unique, and with measurement noise the data
  again do not show one consistent value.

## Three ways to get a single representative number

Given data $y_1, y_2, \dots, y_N$ and wanting a single number that ideally
predicts the outcome, we consider three "means."

### Arithmetic mean

$$\hat{y} = \frac{1}{N}\sum_{i=1}^{N} y_i$$

(the same formula as last time).

### Geometric mean

Instead of adding, we **multiply** the numbers and take the $N$-th root (so the
unit of the estimate matches):

$$\hat{y} = \sqrt[N]{\,y_1 \cdot y_2 \cdots y_N\,}$$

A property used in Theory of Automatic Control (whether the step response of two
tanks can be periodic): the **arithmetic mean is always greater than or equal to
the geometric mean** ($\text{AM} \ge \text{GM}$).

### Median

The **median** (which got media attention as the *7-day median* of COVID-19
incidence) is found by an algorithm rather than a closed formula:

1. **Sort** the measurements into $\tilde{y}_1, \tilde{y}_2, \dots$
2. If $N$ is **odd**, take the middle element at position $\dfrac{N+1}{2}$.
   (Check: $N = 3 \Rightarrow (3+1)/2 = 2$, the second element.)
3. If $N$ is **even**, take the **average of the two middle elements**, at
   positions $\dfrac{N}{2}$ and $\dfrac{N}{2}+1$:

   $$y_m = \frac{\tilde{y}_{N/2} + \tilde{y}_{N/2 + 1}}{2}$$

## Comparing the three estimators

### One run ("on the fly")

On the same dataset, the arithmetic mean (blue), geometric mean (red) and median
(yellow) are each recomputed from **all samples seen so far** (e.g. the value at
40 uses the first 400 samples <!-- unclear: lecturer says "at 40 we take 400 previous samples" -->).

Observations:
- In the **beginning**, with few samples, all three **oscillate** relative to the
  scale.
- After some time they all settle and are "doing their jobs"; the **noise is much
  larger than the error of the estimate**, so even with few samples they are not
  far off.
- Zooming in (band ~0.94 to ~1.06): the condition $\text{AM} \ge \text{GM}$ holds
  — the **red (geometric) curve is always below the blue (arithmetic)**.
- The **arithmetic mean** does the best job overall and **meanders less and less**
  / becomes more confident as more samples are taken. By contrast the **median**
  settles but then gets "knocked off" by disturbances (violent behaviour) that the
  arithmetic mean shrugs off, because the median is based on only one or two
  numbers while the arithmetic and geometric means take **every** number into
  account.

A suggested overall measure of quality: the **integral of the difference with
respect to 1** (the true value).

### Statistics over many runs (box plots)

To be fair, instead of one "race" we generate **1,000 data points** and compute
the three estimators, and repeat this **1,000 times** (code is in the e-learning).
This is real statistics — 1,000 races.

The results are shown as **box plots**, obtained from the histogram of the 1,000
estimates:
- The **central line** is the most probable estimate (mean of the histogram).
- The **box edges** mark where the **cumulative distribution function** reaches
  **0.25** and **0.75** — i.e. 25% of race results lie below the lower edge and
  25% above the upper edge, so the box contains the central **50%**.
- The **whiskers** (black bars) show the spread / range of outcomes (e.g. a run
  where the median ended at 0.983, failing to estimate 1).

Reading the box plots:
- **Arithmetic mean** — best: most probable value reaches **1**, and there is a
  **50% chance** the error is within about **±0.003**.
- **Geometric mean** — essentially a copy of the arithmetic case shifted to
  slightly **lower** values (again $\text{AM} \ge \text{GM}$), similar range.
- **Median** — worst in one respect: although its most probable value is also 1,
  it is more probable to have a **larger error** than the arithmetic mean, and its
  **spread is the largest** (possible to be off by nearly 0.02). This wide spread
  is attributed to the median's "teeth" behaviour: a single sample can change
  which numbers are picked into the formula.

## Optimization-based approach: least squares

Before the fully statistical approach, formulate the problem as **least-squares
estimation**. With $N$ data points, find the estimate $\hat{y}$ that minimizes the
sum of squared residuals:

$$\min_{\hat{y}} \sum_{i=1}^{N} (y_i - \hat{y})^2$$

This is a **scalar, unconstrained optimization problem with one variable**. Solve
it **analytically** by setting the derivative to zero (not a gradient — that is
for multidimensional problems):

$$\frac{d}{d\hat{y}} \sum_{i=1}^{N} (y_i - \hat{y})^2
  = \sum_{i=1}^{N} 2\,(y_i - \hat{y})(-1) = 0$$

The derivative of a sum is the sum of the derivatives. Pull the constant $2$ and
$-1$ out of the sum; since the right-hand side is zero we can divide by $-2$:

$$\sum_{i=1}^{N} (y_i - \hat{y}) = 0$$

Split the sum. The term $\sum_{i=1}^{N}\hat{y}$ equals $N\hat{y}$ (adding $\hat{y}$
to itself $N$ times — "one banana, second banana, … until $N$ bananas"):

$$\sum_{i=1}^{N} y_i - N\hat{y} = 0 \quad\Longrightarrow\quad
  \hat{y} = \frac{1}{N}\sum_{i=1}^{N} y_i$$

So the **arithmetic mean** is the answer. Moreover, the minimized quantity
$\sum (y_i - \hat{y})^2$ is essentially the (scaled) **variance** — so minimizing
least squares is **minimizing the variance of the estimate**. That is why the
arithmetic mean behaves so well: it minimizes the error/variance itself.

## Toward the statistical approach: maximum likelihood

The statistical approach starts from the same ground (data points from a normal
distribution with mean $\bar{y}$ and some variance), but now we **take the $N$
samples and find the most probable value** representing them.

### The likelihood function

Let $k$ be the ordinal number of an experiment. Statisticians write the
probability of seeing a data point **given** the parameters (the vertical bar "|"
reads "given that") — the PDF encoded by the mean and variance. But our case is
the **other way around**: we are **given the data** and want to find the
parameters. The same Gaussian function is reused under a different name — the
**likelihood function** — asking the likelihood that the data were generated by a
distribution with mean $\hat{y}$ and standard deviation $\sigma$:

$$L(\bar{y}, \sigma \mid y_k) = \frac{1}{\sigma\sqrt{2\pi}}\,
  e^{-\frac{(y_k - \bar{y})^2}{2\sigma^2}}$$

It is the same good old Gaussian; only the name changes. (A **log-likelihood**
function will appear soon.) Evaluating it for $y_1, y_2, \dots$ gives the
contribution of each data point to the mean and standard deviation.

### Maximum likelihood estimation

To get a **single** number out of the several experiments, we form a **joint**
quantity — as with the dice last time, the probability of event A **and** event B
is the **product** of their probabilities (e.g. rolling a one twice in a row:
$a \cdot a$). The single likelihoods are the $L$'s, so we pose **maximum
likelihood estimation** as maximizing the **joint** probability — the product over
all samples — with respect to the two parameters:

$$\max_{\bar{y},\,\sigma} \;\prod_{k=1}^{N} L(\bar{y}, \sigma \mid y_k)$$

This "beast" — a product of several Gaussian fractions/exponentials — will be
**solved analytically next time** (cliffhanger).
