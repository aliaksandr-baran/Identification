# Identification — Oral Exam Preparation (Theory)

> Goal: be able to *explain in words* the concepts behind every practical step,
> answer "why", and write the key formulas on a board.

## Exam format
You are randomly assigned **two topics — one from each category**:

**I. Static Identification**
1. Introduction to Statistics
2. Estimation of a Constant
3. Linear Regression
4. Practical Aspects of Linear Regression

**II. Dynamic Identification**
5. Filtration of Dynamic Signals
6. Modelling of Dynamic Systems
7. Recursive Identification
8. Practical Aspects of Identification

The rest of this file has two parts: **(1)** a per-topic *talk track* — what to
put on the board for each of the 8 topics — and **(2)** detailed Q&A (Parts A–R)
backing them up.

---

## Topic talk-tracks (what to say if assigned this topic)

### Topic 1 — Introduction to Statistics  *(→ Parts A, B)*
1. Population vs sample; random variable; measurement = signal + noise.
2. Location: mean, median, geometric mean — and when each is used (robustness).
3. Spread: variance & standard deviation; the **$N-1$** (unbiased) denominator.
4. **PDF** (density, integrates to 1) vs **CDF** ($P(X \le x)$) vs **quantile** (inverse CDF).
5. The **normal distribution**; the 68–95–99.7 rule ($\pm 1/2/3\,\sigma$).
6. Histograms; with more data the histogram $\to$ the true PDF (law of large numbers).
7. Why it matters: Gaussian noise is what makes **least squares optimal**.

### Topic 2 — Estimation of a Constant  *(→ Part EC, B)*
1. Setup: many noisy measurements of one true value, $y_i = c + e_i$.
2. Least-squares estimate of the constant = the **arithmetic mean** (derive it).
3. Estimator properties: **unbiased**, **consistent**; variance of the estimate
   $\mathrm{var}(\hat{c}) = \sigma^2/N$ $\to$ error shrinks as $1/\sqrt{N}$ (averaging beats noise).
4. Alternative estimators: median (robust to outliers), geometric mean
   (multiplicative data); compare spread via repeated trials / box plots.
5. Under Gaussian noise the mean is the **maximum-likelihood** estimate.
6. Confidence interval on the estimate; more data $\to$ tighter interval.

### Topic 3 — Linear Regression  *(→ Part C)*
1. Model **linear in the parameters**: $y = X p + e$ (features may be nonlinear
   in the data: $\sqrt{h}$, $T^2$, $1/T$).
2. The regressor/design matrix $X$; the intercept (bias) column.
3. Least squares: minimise $\|X p - y\|^2$ $\to$ **normal equations**
   $p = (X^T X)^{-1} X^T y$ = `X\y` (QR internally).
4. **Gauss–Markov assumptions** $\to$ LS is the Best Linear Unbiased Estimator (BLUE).
5. Quality: **RMSE**, parity plot, parameter confidence intervals.
6. Extends to multivariate (many inputs).

### Topic 4 — Practical Aspects of Linear Regression  *(→ Parts C7, D, E)*
1. **Standardization** (zero mean, unit variance): comparable scales + better
   conditioning of $X^T X$.
2. **Correlation vs covariance**; correlation $\in [-1, 1]$.
3. **Multicollinearity**: correlated inputs make $X^T X$ near-singular $\to$ unstable
   coefficients $\to$ drop redundant features (feature selection).
4. **PCA** for decorrelation / dimensionality reduction (elbow rule).
5. **Training vs testing**; over- vs under-fitting; choosing model order/structure.
6. Outliers and data cleaning.

### Topic 5 — Filtration of Dynamic Signals  *(→ Part F)*
1. Why filter: separate the useful signal from noise by **frequency content**.
2. **Low-pass** (keep slow trend), **high-pass** (keep fast part), band-pass;
   the cut-off frequency.
3. **Moving average** = a FIR low-pass filter; window size sets the smoothing.
4. **Causal** (`filter`, introduces delay) vs **zero-phase** (`filtfilt`, no lag).
5. Trade-off: more smoothing removes noise but also destroys real dynamics.

### Topic 6 — Modelling of Dynamic Systems  *(→ Part G)*
1. Dynamic vs static: the output has **memory** (depends on past).
2. **Impulse response** & **convolution** $y(t) = \int g(\tau)\,u(t-\tau)\,d\tau$.
3. Discrete models: **FIR** $y_k = \sum b_i u_{k-i}$ (all-zero, always stable, high order).
4. **ARX** $y_k = -\sum a_i y_{k-i} + \sum b_i u_{k-i}$ (poles+zeros, few parameters).
5. **ARMAX** = ARX + a moving-average term on past **errors** (models disturbances).
6. Both ARX/FIR are **linear in parameters** $\to$ least squares (regressor of lags).
7. **Transfer function** in $z^{-1}$ (unit delay); FIR vs ARX comparison; stability.

### Topic 7 — Recursive Identification  *(→ Part R)*
1. Batch vs **recursive**: update the estimate per new sample (online / real-time).
2. **RLS** structure: $\theta_k = \theta_{k-1} + K_k (y_k - \phi_k^T \theta_{k-1})$
   = old + gain × innovation.
3. The covariance $P$ and gain $K$ (= Kalman gain); initialization ($P_0$ large).
4. **Forgetting factor $\lambda$**: $1$ = standard RLS (= batch LS); $<1$ tracks
   time-varying parameters (tracking vs noise trade-off).
5. RLS is a special case of the **Kalman filter**.
6. Simplest special case: the **bias update** (adapt only the offset $b$ by the
   prediction error, optionally filtered by a trust gain $\delta$).

### Topic 8 — Practical Aspects of Identification  *(→ Parts G6, H, E)*
1. **Experiment / input design**: needs **persistent excitation** (rich spectrum).
2. Input types: step (few frequencies) → random → **PRBS** (near-white, preferred).
3. **Sampling time** choice (avoid aliasing / stiffness).
4. **Model-order selection** from **ACF/PACF** of the output.
5. **Validation**: training vs testing RMSE, one-step prediction vs free
   simulation, residual checks; overfitting.
6. Real workflow (Flexy², Assignment 2): clean → standardize → split → FIR/ARX →
   compare.

---

## Part A — Fundamentals

### A1. What is system identification?
Building a **mathematical model** of a system from **measured input–output
data**, instead of from first-principles physics. We choose a model *structure*
(class of equations) and then *estimate its parameters* so the model reproduces
the data. It is data-driven (empirical / black-box) modelling, the counterpart
to white-box (physical) modelling. A grey-box model mixes both.

### A2. Black-box vs grey-box vs white-box?
The three differ by **how much internal knowledge of the system you have/use** —
a spectrum from "none" to "complete":

- **White-box** (full internal knowledge): model derived from physical laws
  (mass/energy balances, conservation); structure *and* parameters have physical
  meaning. *Most insight, most effort/expertise needed.*
- **Black-box** (no internal knowledge): structure chosen only for convenience
  (FIR, ARX); parameters are just fitted numbers with no physical meaning — you
  only see inputs and outputs. *Fastest, but no physical insight; can't explain
  *why* it works.*
- **Grey-box** (partial internal knowledge): known structure from physics with
  unknown parameters fitted to data — a balanced hybrid combining both.

**Vending-machine analogy:**
- *Black-box* = a **user** of the machine: insert money, get a drink, no idea of
  the internal mechanism.
- *White-box* = the **technician**: inspects every internal component to
  understand how each part contributes.
- *Grey-box* = the **operator**: knows the basic mechanical principles but not
  every detail.

| Aspect | White-box | Grey-box | Black-box |
|--------|-----------|----------|-----------|
| Internal knowledge | Complete | Partial | None |
| Parameters | Physical | Mixed | Just fitted |
| Effort / expertise | High | Medium | Low |
| Physical insight | Full | Some | None |
| Course examples | First-principles tank/gas models | Known structure + LS fit | FIR, ARX |

*Note:* the same white/black/grey-box vocabulary is used in **software testing**
(testing without code knowledge vs. inspecting the source vs. partial access) —
the underlying idea is identical: **the level of internal visibility you have
into the thing you're analysing.** In *identification* it describes the **model**;
in testing it describes the **code under test**.

### A3. The general identification procedure (steps)?
1. Design an experiment & collect data (choose input signal).
2. Inspect / visualize / clean the data.
3. Choose a model structure (static/dynamic, FIR/ARX, order).
4. Estimate parameters (least squares).
5. Validate the model (RMSE on independent test data, residual checks).
6. If unsatisfactory, revise structure/order and repeat.

### A4. Static vs dynamic model?
- **Static:** output depends only on the *current* input — $y = f(u)$
  (e.g. tank $q = k\sqrt{h}$, gas tank $V = f(T)$). No memory.
- **Dynamic:** output depends on *past* inputs and/or outputs — has memory /
  time evolution (FIR, ARX). Needed when the system has inertia/lag.

---

## Part B — Statistics & data

### B1. Mean, variance, standard deviation — definitions?
- Mean (expected value): $\mu = \frac{1}{N}\sum_{i} x_i$.
- Sample variance: $\sigma^2 = \frac{1}{N-1}\sum_{i}(x_i - \mu)^2$.
- Std: $\sigma = \sqrt{\sigma^2}$, same units as the data; spread around the mean.
- The **$N-1$** (Bessel's correction) makes the sample variance an *unbiased*
  estimate of the true variance.

### B2. PDF vs CDF?
- **PDF** $f(x)$: probability *density*; area under it over an interval = the
  probability of being in that interval; integrates to 1.
- **CDF** $F(x) = P(X \le x)$: monotonically increasing from 0 to 1; it is the
  integral of the PDF.
- **Quantile / inverse CDF** answers "which $x$ has cumulative probability $p$".

### B3. Normal (Gaussian) distribution — why does it matter?
Defined by $\mu$ and $\sigma$. About 68% of data within $\pm 1\sigma$, 95% within
$\pm 2\sigma$, 99.7% within $\pm 3\sigma$. Measurement noise is commonly assumed
Gaussian, which is exactly what makes **least squares** the statistically optimal
(maximum-likelihood) estimator.

### B4. Law of large numbers (seen in Seminar 2)?
As sample size grows, the empirical histogram converges to the true PDF and the
sample mean converges to the true mean. More data → more reliable statistics.

### B5. Mean vs median vs geometric mean — when to use which? (Seminar 4)
- **Arithmetic mean:** best for symmetric noise; sensitive to outliers.
- **Median:** robust to outliers / skew.
- **Geometric mean:** for multiplicative / log-normal data (e.g. growth rates).
A box plot compares their spread across repeated estimates.

---

## Part EC — Estimation of a constant (Exam topic 2 / Lectures L03–L04)

### EC1. What is "estimation of a constant"?
The simplest identification problem: estimate a single unknown true value $c$
from $N$ noisy measurements $y_i = c + e_i$, where $e_i$ is measurement noise
(zero-mean). It is a one-parameter special case of linear regression with
regressor $X = \mathbf{1}_{N}$ (a column of ones).

### EC2. Show that the least-squares estimate of a constant is the mean.
Minimise $J(c) = \sum_{i}(y_i - c)^2$. Set the derivative to zero:

$$
\frac{dJ}{dc} = -2\sum_{i}(y_i - c) = 0 \quad\Longrightarrow\quad
\sum_{i} y_i = N c \quad\Longrightarrow\quad \hat{c} = \frac{1}{N}\sum_{i} y_i .
$$

So the LS estimate of a constant **is exactly the arithmetic mean** — consistent
with `X\y` when $X = \mathbf{1}_{N}$.

### EC3. Properties of the mean estimator?
- **Unbiased:** $E[\hat{c}] = c$ (on average, correct).
- **Variance:** $\mathrm{var}(\hat{c}) = \sigma^2/N$ — drops with more data.
- **Consistent:** as $N \to \infty$, $\hat{c} \to c$ (variance $\to 0$).
- **Standard error** $= \sigma/\sqrt{N}$: to halve the error you need **4× the
  data** (the $\sqrt{N}$ law). This is *why* we average repeated measurements.
- Under **Gaussian** noise the mean is also the **maximum-likelihood** estimate.

### EC4. When is the mean a bad estimator — and what to use instead?
- With **outliers / skew**, use the **median** (robust — a few bad points barely
  move it).
- With **multiplicative / log-normal** data (ratios, growth rates), use the
  **geometric mean**.

Comparing the three estimators over many repeated trials (box plots) shows the
mean has the smallest spread for clean Gaussian noise, the median the most
robustness to outliers (Seminar 4, the tank constant $k_{11}$).

### EC5. Confidence interval on the estimate?
$\hat{c} \pm t\cdot\hat{\sigma}/\sqrt{N}$ ($t$ from the Student/normal
distribution for the chosen confidence, e.g. 95%). More measurements → narrower
interval. It quantifies how much to trust the estimate.

---

## Part C — Least squares & regression

### C1. State the least-squares problem.
Given regressor matrix $X$ (rows = measurements, columns = features) and outputs
$y$, find parameters $p$ minimizing the sum of squared residuals
$\min_{p}\|X p - y\|^2$. Solution = **normal equations**:

$$
p = (X^T X)^{-1} X^T y .
$$

MATLAB computes this as `X\y` — internally via QR factorization, not by forming
$X^T X$, which is more numerically stable (same answer, better algorithm).

### C2. Why squared errors (not absolute)?
- Differentiable → closed-form linear solution.
- Penalizes large errors more.
- Maximum-likelihood estimate under Gaussian noise.

(Absolute error → robust regression, but no closed form.)

### C2b. When is least squares the *best* estimator? (Gauss–Markov)
Under the **Gauss–Markov assumptions** the LS estimate is the **Best Linear
Unbiased Estimator (BLUE)** — minimum variance among all linear unbiased
estimators:
1. The model is **linear in the parameters** and correctly specified.
2. Noise has **zero mean** ($E[e] = 0$).
3. Noise is **homoscedastic** (constant variance).
4. Noise is **uncorrelated** across measurements.

(If, in addition, the noise is **Gaussian**, LS = maximum-likelihood.) When these
break — e.g. correlated noise in dynamic data — plain LS becomes
biased/suboptimal, motivating methods beyond ARX.

### C3. What is the regressor / design matrix?
The matrix whose columns are the model's basis functions evaluated at each data
point. The model must be **linear in the parameters** for `X\y` to apply — note
the *features themselves* can be nonlinear ($\sqrt{h}$, $T^2$, $1/T$); only the
parameter dependence must be linear.

### C4. Role of the intercept (bias) term?
The `ones(size(...))` column lets the fit have a non-zero offset
($y = p_1 x + p_0$). Omitting it forces the line through the origin (used for
$q = k\sqrt{h}$, which must be 0 when $h = 0$).

### C5. RMSE — what is it and why use it?

$$
\mathrm{RMSE} = \sqrt{\tfrac{1}{N}\sum_{k}(\hat{y}_k - y_k)^2} .
$$

Average prediction error in the **same units as $y$**; it equals the standard
deviation of the residuals when their mean is $\approx 0$ (true for LS with an
intercept). Lower = better. Used to compare competing models.

### C6. Parity plot — what does it show?
Predicted vs measured with a 45° reference line. Points on the diagonal = perfect
predictions; systematic deviation reveals bias or model-structure error.

### C7. Why standardize data? (zero mean, unit variance)
- Puts variables of different units/scales on equal footing.
- Improves numerical conditioning of $X^T X$.
- Makes regression coefficients comparable in importance.
- Required before correlation/PCA so large-magnitude variables don't dominate.

Formula: $x_s = (x - \mu)/\sigma$. A constant signal can't be standardized
($\sigma = 0$).

---

## Part D — Correlation, covariance, PCA

### D1. Covariance vs correlation?
- **Covariance** $\mathrm{cov}(x,y)$: joint variability, units =
  units($x$)·units($y$), unbounded.
- **Correlation** (Pearson $r$): covariance normalized by the two std devs →
  dimensionless, in **$[-1, 1]$**. $r = +1$ perfect positive linear, $-1$ perfect
  negative, $0$ no *linear* relation.
- Correlation is just the covariance of the **standardized** variables.

### D2. "Correlation does not imply causation" — relevance?
Two variables can move together due to a common cause or coincidence. In
identification this matters for **input selection**: a highly correlated input
isn't necessarily a *causal driver* of the output.

### D3. What is multicollinearity and why remove correlated inputs? (Seminar 6/7)
If two regressor columns are strongly correlated, $X^T X$ becomes near-singular →
unstable, large, untrustworthy coefficients. Removing redundant (linearly
dependent) inputs gives a better-conditioned, more generalizable model. This is
the "feature selection" step.

### D4. What is PCA and what is it for?
**Principal Component Analysis** rotates the data onto orthogonal directions
(eigenvectors of the covariance matrix) ordered by variance explained
(eigenvalues). Uses: dimensionality reduction, decorrelation, visualization. The
first PC is the direction of maximum variance.

### D5. Geometric meaning of covariance eigenvectors?
They are the **axes of the data's scatter ellipse**; eigenvalues = variance along
each axis (ellipse semi-axis lengths $\propto \sqrt{\text{eigenvalue}}$). Drawing
the $1\sigma/2\sigma/3\sigma$ ellipses visualizes the covariance structure.

### D6. How to choose the number of principal components?
Plot cumulative/explained variance vs PC index and find the **elbow (knee)** —
the point of diminishing returns — keep PCs up to there.

### D7. Parameter confidence ellipse and "interval contains zero" (L07)?
The parameter covariance is $V_p = \sigma^2 (X^T X)^{-1}$ (noise variance ×
inverse information). Treating $p \sim \mathcal{N}(\hat{p}, V_p)$, the quadratic
form $(p-\hat{p})^T V_p^{-1}(p-\hat{p})$ follows a **chi-square** with $n_p$
degrees of freedom, so its level set $\le \chi^2_{n_p,\alpha}$ is the
**confidence ellipse** — the multivariate generalization of the scalar interval.
Semi-axis lengths come from the parameter CIs; off-diagonal terms tilt the
ellipse. Practical test: if a parameter's confidence interval **contains zero**
(e.g. $[-1, 2]$ at 95%), the model can live **without** that parameter — it may
be unobservable (collinearity), under-excited, or simply not causal. A clean way
to prune overfit terms.

---

## Part E — Training/testing & model quality

### E1. Why split into training and testing datasets?
Train estimates parameters; test gives an **honest, unbiased** estimate of
predictive accuracy on data the model has never seen. Judging accuracy only on
training data is over-optimistic.

### E2. Overfitting vs underfitting?
- **Overfitting:** model too complex (too many parameters/order) — fits noise;
  low training RMSE but high testing RMSE.
- **Underfitting:** model too simple — high error everywhere.

The aim is the order that minimizes **testing** RMSE (bias–variance trade-off).

### E3. How does model order relate to over/underfitting?
Increasing order always lowers *training* error but eventually raises *testing*
error. Choose the smallest order that captures the dynamics (parsimony /
Occam's razor).

---

## Part F — Signals & filtering

### F1. Low-pass vs high-pass filter?
- **Low-pass** keeps slow components (trend), removes fast noise → smoothing.
- **High-pass** keeps fast components (noise/edges), removes slow trend.

The cut-off (normalized) frequency sets the boundary.

### F2. Moving-average filter — what is it?
A FIR filter with equal weights $1/n$; averages the last $n$ samples. Larger $n$
→ smoother but more lag and more edge distortion. It is literally a low-pass
filter.

### F3. Causal filter vs zero-phase filter?
- **Causal** (`filter`) uses only past samples → introduces a **time delay**.
- **Zero-phase** (`filtfilt`, forward+backward) removes the delay → output
  aligned in time. Used to build the *smoothed testing output* in Assignment 2
  so it stays time-aligned with the input.

### F4. Why filter / smooth before identification?
Noise corrupts parameter estimates; smoothing yields a cleaner reference output.
But over-smoothing destroys real dynamics — trade-off.

---

## Part G — Dynamic identification (the core)

### G1. What does convolution describe? (Seminar 9)
A linear time-invariant system's output is the convolution of its **impulse
response** $g(t)$ with the input:

$$
y(t) = \int_0^{t} g(\tau)\,u(t-\tau)\,d\tau .
$$

In discrete time this becomes a weighted sum of past inputs — the basis of the
FIR model.

### G2. Define the FIR model and its meaning.
**Finite Impulse Response:** $y_k = \sum_{i=1}^{m} b_i\,u_{k-i}$. Output is a
weighted sum of the last $m$ inputs; the weights $b_i$ *are* the (sampled)
impulse response. No feedback → always stable. Written as $X p = y$ and solved by
least squares; $X$ is the (lower-triangular, shifted) matrix of past inputs.

### G3. Define the ARX model.
**Auto-Regressive with eXogenous input:**

$$
y_k = -\sum_{i=1}^{n} a_i\,y_{k-i} + \sum_{i=1}^{m} b_i\,u_{k-i} .
$$

Output depends on past **outputs** (the AR part, $a$) and past **inputs** (the
exogenous part, $b$). Transfer function in $z$:

$$
G(z^{-1}) = \frac{\sum_i b_i z^{-i}}{1 + \sum_i a_i z^{-i}} .
$$

Still **linear in parameters** → least squares. $n$ = output order, $m$ = input
order, with $n \ge m$.

### G4. FIR vs ARX — compare.
| | FIR | ARX |
|---|---|---|
| Uses past outputs | No | Yes (feedback) |
| Structure | All-zero (numerator only) | Poles + zeros |
| Stability | Always stable | Can be unstable (poles) |
| Parameters needed | Many (high order ~50) | Few |
| Captures slow decay | Needs long tail | Implicit via poles |
| Typical accuracy | Lower | Higher (fewer params, lower RMSE) |

ARX is more *parsimonious*: feedback models the impulse-response decay with a few
poles, whereas FIR must spell out the whole tail.

### G5. Why does FIR need such a high order (e.g. 50)?
It has no recursion, so each impulse-response sample needs its own coefficient.
A system whose response decays slowly needs many $b$ terms to represent the
"memory". ARX gets the same memory cheaply through the recursive $a_i y_{k-i}$
terms.

**Quantitative version (good board point):** a FIR of order $m$ only remembers
the last $m$ samples — a **memory window $\tau = m\cdot T_s$**. This must span the
system's **settling time**. Example (Assignment 2): $m = 50$, $T_s = 0.02$ s $\to$
$\tau = 1$ s of memory; if the plant settles slower, the FIR is underfit.
Sweeping $m$ up to ~1000 barely lowers RMSE — proof that adding FIR coefficients
is an inefficient substitute for ARX's feedback.

### G6. How do you choose ARX orders $n$ and $m$? (ACF/PACF)
- **ACF** (autocorrelation): how the output correlates with its own past →
  indicates overall memory / MA ($b$) behavior.
- **PACF** (partial autocorrelation): correlation at a lag with intermediate
  lags removed → the lag after which PACF falls inside the confidence band gives
  the **AR order $n$**. Choose $m \le n$ to avoid overfitting.

### G7. What is the z-transform / $z^{-1}$ operator?
$z^{-1}$ is the **unit (one-sample) delay** operator: $z^{-1} y_k = y_{k-1}$. It
turns difference equations into algebraic transfer functions $G(z^{-1}) = Y/U$.
$z^{-n_k}$ represents a pure input **time delay** of $n_k$ samples.

### G7b. What is the ARMAX model and when do you need it?
**Auto-Regressive Moving Average with eXogenous input** — ARX plus a
moving-average term on the past **prediction errors**:

$$
y_k = -\sum_i a_i\,y_{k-i} + \sum_i b_i\,u_{k-i} + \sum_i c_i\,e_{k-i} .
$$

The three parts: AR (past outputs, $a$), exogenous input (past inputs, $b$), and
the new MA part (past errors $e_{k-i}$, weights $c$). Why it helps: plain ARX/FIR
**ignore disturbances** (a leaking valve, a changed feed quality). The MA term
lets the $c$ coefficients **absorb the systematic disturbance errors**, freeing
$a$ and $b$ to learn the *true* plant dynamics. Unlike train-once ARX, ARMAX
**corrects itself online** (a moving average of recent errors). Cost: usually
needs **nonlinear optimization** to fit; to predict ahead (future $e_k$ unknown)
you assume $e_k$ is zero-mean Gaussian noise and build $\pm\sigma$ disturbance
scenarios.

### G8. One-step-ahead prediction vs simulation?
- **One-step-ahead (OSA):** predict $y_k$ using *measured* past outputs $y_{k-i}$
  (regressor uses real data) — what `Phi*theta` computes.
- **Simulation (free-run):** feed the model's *own* past predictions back; only
  the input is given (`lsim`/`sim`). Simulation is the tougher, more honest test.
- **Why it matters when comparing models:** OSA always looks better than
  simulation (it gets the true recent output for free). A very low ARX *test*
  RMSE (e.g. 0.02 in Assignment 2) partly reflects OSA on smoothed data. To
  compare FIR and ARX fairly, evaluate **both the same way** — otherwise
  ARX-by-OSA vs FIR-by-simulation flatters the ARX.

---

## Part R — Recursive estimation (Lecture L11)

### R1. What is recursive estimation and why use it?
Updating the parameter estimate **sample-by-sample** as new data arrives, instead
of re-solving the full batch least squares each time. Motivation:
- **Online / real-time** identification (adaptive control).
- **Time-varying systems** — track parameters that drift.
- **Memory/computation** — no need to store or reprocess all past data.

### R2. State the Recursive Least Squares (RLS) update in words.
For each new sample: compute the **prediction error (innovation)**
$e_k = y_k - \phi_k^T \theta_{k-1}$ (measured minus predicted), then correct the
estimate $\theta_k = \theta_{k-1} + K_k e_k$, where the **gain** $K_k$ comes from
the current covariance $P$. Finally update $P$. Structure = **"old estimate +
gain × prediction error."**

Formulas:

$$
\begin{aligned}
K_k &= \frac{P_{k-1}\,\phi_k}{\lambda + \phi_k^T P_{k-1}\,\phi_k} \\[4pt]
\theta_k &= \theta_{k-1} + K_k\,(y_k - \phi_k^T \theta_{k-1}) \\[4pt]
P_k &= \frac{1}{\lambda}\bigl(P_{k-1} - K_k\,\phi_k^T P_{k-1}\bigr)
\end{aligned}
$$

### R3. What is the forgetting factor $\lambda$?
A weight $\lambda \in (0, 1]$ that exponentially discounts older data.
- $\lambda = 1$: standard RLS — all data weighted equally; converges to the
  **same result as batch LS**.
- $\lambda < 1$ (typ. 0.95–0.99): old data "forgotten" → the estimator can
  **follow time-varying parameters**. Smaller $\lambda$ = faster tracking but
  noisier (variance ↑).

This is the bias–variance / tracking–noise trade-off.

### R4. What is the matrix $P$ and the gain $K$?
- $P$ = **covariance of the parameter estimate** (proportional to $(X^T X)^{-1}$);
  it shrinks as more data builds confidence. Initialized large (e.g. $10^6 I$) to
  signal low initial confidence and allow fast convergence.
- $K$ = **gain** (the Kalman gain): scales how much the latest prediction error
  corrects the estimate. Large when uncertain, small once confident.

### R5. Relationship of RLS to batch least squares and the Kalman filter?
- With $\lambda = 1$, RLS after $N$ samples = batch LS `X\y` exactly — same
  answer, computed incrementally.
- RLS is a **special case of the Kalman filter** (estimating constant parameters
  instead of a moving state); the gain $K$ is the Kalman gain.

### R6. What is the "innovation"?
$e_k = y_k - \phi_k^T \theta_{k-1}$ — the part of the new measurement **not
predicted** by the current model, i.e. the genuinely new information. RLS moves
the estimate in proportion to it.

### R7. Bias update — the simplest recursive scheme (L11).
If a deployed model develops an almost **constant systematic error** (e.g. a
changed feed/supplier, mild nonlinearity) but the **slope is still correct**, you
adapt only the **offset $b$**, not the verified slopes — industry prefers this.
Update by the prediction error: $b_k = b_{k-1} + (y_{k-1} - \hat{y}_{k-1})$.
Reacting to one point is myopic, so filter it with a trust gain
$\delta \in [0,1]$:

$$
b_k = \delta\,b_{k-1} + (1-\delta)\,(\text{new bias}) .
$$

$\delta \to 1$ = distrust measurements (slow drift to a new operating point);
$\delta = 0$ = follow the latest point fully. Same shape as a P controller
(estimate ← estimate + gain × error); the scalar slope version (RLS with $b = 0$)
is $a_N = a_{N-1} + \frac{x_N}{\sum_k x_k^2}(y_N - a_{N-1}x_N)$, whose gain shrinks
automatically as data accumulates — add a **forgetting window** to keep adapting.

---

## Part H — Experiment design

### H1. What makes a good identification input signal?
It must be **persistently exciting** — rich enough in frequencies to excite all
the system's modes. A constant or single step reveals little; you need variety in
amplitude and frequency.

### H2. Compare step, random, and PRBS inputs. (Seminars 9–11)
- **Step / staircase:** simple, shows gain & time constants, but excites few
  frequencies.
- **Random uniform levels:** broad excitation, but power spread unevenly.
- **PRBS (pseudo-random binary sequence):** switches between two levels
  pseudo-randomly; near-white spectrum, optimal power, **reproducible** → the
  preferred input for dynamic identification.

### H3. Sampling time $T_s$ — why does it matter?
Too large → aliasing, miss fast dynamics; too small → numerically stiff,
noise-dominated, huge data. Should resolve the system's dominant time constant
(rule of thumb: several samples per time constant).

### H4. What is the role of `rng(100)`?
Fixes the random-number seed so simulations with random inputs/noise are
**reproducible** — essential for comparing results and grading.

### H5. Why remove "bad" sections of data before identifying?
Least squares assumes a **consistent input→output relationship across the whole
record**. Sections where that breaks — e.g. a dead-zero startup where the input
is already on but the output hasn't responded, or a saturated/zero-sensor region
at the end — inject a **structural bias into the regressor matrix**: the model is
forced to explain output that the input didn't cause. Result: worse fit, higher
RMSE. Trimming these non-representative regions (keeping only clean,
input-driven behavior) is why data cleaning comes before model fitting.

### H6. How do you validate that standardization didn't distort the data?
Plot the standardized value against the original value — it must be a **straight
line** (standardization is a purely *linear* $(x-\mu)/\sigma$ map). A straight
line confirms no nonlinear distortion was introduced; numerically, check
$\mathrm{mean} \approx 0$, $\mathrm{std} \approx 1$.

### H7. Static vs dynamic, and the linearity check (L10)?
Plan step changes of, say, $\tfrac13, \tfrac23, 1$ and read the **steady-state**
outputs:
- **Proportional** outputs → a **static gain** suffices (no dynamic model needed).
- **Non-proportional but same-sign** gain → nonlinear but **bearable** (integral
  control can handle it).
- **Gain that changes sign** → **red alert**: strongly nonlinear, essentially
  uncontrollable with a linear controller (even LQR fails).
- **Immediate scaled step, no transient** → no pole/zero info → use a static
  model; fitting ARMAX here gives meaningless numbers the test data will expose.

This is why the deciding step changes must be in the **original experiment design**.

### H8. How do you identify an *unstable* plant (closed-loop ID)?
You can't run an open-loop experiment on an unstable system, and you need a model
to design a stabilizing controller — a **chicken-and-egg** problem. If the plant
already runs in production, a stabilizing controller likely exists. Then put
**controller + plant in one box** and identify the **closed loop** (reference →
response), because open-loop steady-state data reveals nothing about poles/delays.
Example: a P controller $K_R$ on $K/(Ts+1)$ (positive pole, $T < 0$) gives the
closed-loop characteristic equation $Ts + 1 + K_R K = 0$; choosing $K_R$
stabilizes it, and the reference→response relation (two unknowns) is fitted as a
discrete **ARX** model. A bad experiment can fit a *stable* model to an unstable
plant — a reason to loop back and redesign.

---

## Part I — The two assignments (be ready to discuss yours)

### I1. Assignment 1 — static identification.
Fit static input–output relations (e.g. tank $q = k\sqrt{h}$, gas-tank
$V = f(T)$) by least squares; compare candidate structures
(linear/quadratic/inverse) with RMSE and parity plots; study the effect of
measurement noise on the estimate.

### I2. Assignment 2 — dynamic identification of the Flexy² device.
Flexy²: $u$ = fan speed (input), $n$ = noise level, $y$ = flex-sensor bend
(output). Workflow: load & interpolate (ZOH) → remove bad regions (zero-fan,
saturated bend) → standardize (use $u$, not the constant $n$) → train = noisy /
test = zero-phase-smoothed output → FIR(50) → ARX (order from ACF/PACF) → compare
RMSE. Expected conclusion: **ARX more accurate with fewer parameters**.

### I3. Why use the constant $n$ channel or not?
$n$ is (near) constant → zero variance → carries no dynamic information and can't
be standardized. So $u$ (fan speed) is the input used to identify the dynamics.

---

## Quick rapid-fire recall

- Least squares solution → $p = (X^T X)^{-1} X^T y$ = `X\y`.
- RMSE = std of residuals, units of $y$.
- Standardize → $(x-\mu)/\sigma$; correlation $\in [-1,1]$.
- PCA = eigenvectors of covariance, ordered by variance.
- FIR = past **inputs** only, all-zero, high order, always stable.
- ARX = past inputs **and outputs**, poles+zeros, low order, can be unstable.
- ARMAX = ARX + MA on past **errors** ($c_i e_{k-i}$) → models disturbances, self-corrects.
- $z^{-1}$ = unit delay.
- PACF → AR order $n$; ACF → MA/memory.
- PRBS = best persistently-exciting input.
- Train fits, test judges; gap = overfitting.
- RLS = "old estimate + gain × innovation"; $\lambda = 1 \Rightarrow$ batch LS; $\lambda < 1 \Rightarrow$ tracks drift.
- RLS gain $K$ = Kalman gain; $P$ = estimate covariance (starts large).
- Bias update = simplest recursive scheme: shift only the offset by the prediction error.
- Unstable plant → identify the **closed loop** (controller + plant in one box).
