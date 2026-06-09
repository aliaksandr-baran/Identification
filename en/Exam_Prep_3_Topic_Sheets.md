# Identification — Oral Exam Topic Sheets

One page per topic. You get **2 topics, one from each category**. For each sheet:
**Say this** = the board plan to talk through · **Formulas** = what to write ·
**Follow-ups** = likely probing questions · **If stuck** = a safe thing to add.

*(Each topic is separated by a page break for printing to PDF.)*

---

# I — STATIC IDENTIFICATION

## Topic 1 — Introduction to Statistics
*Lecture L02 · backs: Parts A, B*

**Say this (board plan)**
1. We measure with noise: **measurement = true signal + noise**. Statistics
   describes the noise and lets us extract the signal.
2. **Location** of data: mean, median, geometric mean.
3. **Spread** of data: variance and standard deviation.
4. **PDF** vs **CDF** vs **quantile** (inverse CDF).
5. The **normal (Gaussian)** distribution and the 68–95–99.7 rule.
6. Histogram → true PDF as sample size grows (law of large numbers).
7. Why we care: Gaussian noise makes **least squares optimal**.

**Formulas**

$$
\begin{aligned}
\text{mean}\quad &\mu = \frac{1}{N}\sum_i x_i \\
\text{variance}\quad &\sigma^2 = \frac{1}{N-1}\sum_i (x_i-\mu)^2 \quad(N-1=\text{unbiased}) \\
\text{std}\quad &\sigma = \sqrt{\sigma^2} \\
\text{CDF}\quad &F(x) = P(X \le x) = \int \mathrm{pdf}, \qquad \text{quantile} = F^{-1}(p) \\
\text{normal}\quad &\pm1\sigma \approx 68\%,\ \ \pm2\sigma \approx 95\%,\ \ \pm3\sigma \approx 99.7\%
\end{aligned}
$$

**Follow-ups**
- *Why $N-1$?* → makes the sample variance an unbiased estimate of the true variance.
- *PDF vs CDF?* → density vs cumulative; CDF is the integral of the PDF, goes 0→1.
- *Mean vs median?* → median is robust to outliers; mean is sensitive.

**If stuck:** mention that all of identification rests on these — every parameter
we estimate is a statistic computed from noisy data.

<div style="page-break-after: always"></div>

## Topic 2 — Estimation of a Constant
*Lectures L03–L04 · backs: Part EC, B*

**Say this (board plan)**
1. Simplest identification: estimate one true value $c$ from $N$ noisy readings
   $y_i = c + e_i$. It's regression with $X = \mathbf 1_N$ (a column of ones).
2. Least squares → the estimate **is the arithmetic mean** (derive it).
3. Estimator quality: **unbiased**, **consistent**, $\mathrm{var}(\hat{c}) = \sigma^2/N$.
4. The **$\sqrt{N}$ law**: error $\propto \sigma/\sqrt{N}$ → 4× data to halve the
   error. This is why we average repeated measurements.
5. Alternatives: **median** (robust to outliers), **geometric mean**
   (multiplicative data). Compare spread with box plots (tank $k_{11}$, Seminar 4).
6. Gaussian noise → mean is the **maximum-likelihood** estimate.

**Formulas**

$$
\begin{aligned}
J(c) &= \sum_i (y_i - c)^2 \\
\frac{dJ}{dc} = -2\sum_i (y_i - c) = 0 \;&\Rightarrow\; \hat{c} = \frac{1}{N}\sum_i y_i = \text{mean} \\
\mathrm{var}(\hat{c}) &= \frac{\sigma^2}{N}, \qquad \text{standard error} = \frac{\sigma}{\sqrt{N}} \\
\text{95\% CI:}\quad &\hat{c} \pm t\cdot\frac{\hat{\sigma}}{\sqrt{N}}
\end{aligned}
$$

**Follow-ups**
- *Why is the mean "best"?* → minimum-variance unbiased estimate for Gaussian noise.
- *When does it fail?* → outliers/skew → use median; ratios → geometric mean.
- *How does error shrink?* → as $1/\sqrt{N}$, not $1/N$ — diminishing returns.

**If stuck:** stress the $\sqrt{N}$ law and that "estimate a constant" = the
one-parameter case of linear regression.

<div style="page-break-after: always"></div>

## Topic 3 — Linear Regression
*Lectures L05–L06 · backs: Part C*

**Say this (board plan)**
1. Model **linear in the parameters**: $y = X p + e$. Features can be nonlinear
   in the data ($\sqrt{h}$, $T^2$, $1/T$) — only the *parameter* dependence is linear.
2. The **regressor/design matrix** $X$ (columns = features); intercept column.
3. Least squares minimises $\|X p - y\|^2$ → **normal equations**; MATLAB `X\y`.
4. **Gauss–Markov** assumptions → LS is **BLUE** (best linear unbiased estimator).
5. Assess fit: **RMSE**, parity plot, parameter confidence intervals.
6. Generalises to many inputs (multivariate regression).

**Formulas**

$$
\begin{aligned}
&\min_p \|X p - y\|^2 \;\Rightarrow\; p = (X^T X)^{-1} X^T y \quad(= X\backslash y,\ \text{QR internally}) \\
&\hat{y} = X p \\
&\mathrm{RMSE} = \sqrt{\mathrm{mean}\big((\hat{y}-y)^2\big)}
\end{aligned}
$$

Gauss–Markov (zero-mean, constant-variance, uncorrelated noise) $\Rightarrow$ **BLUE**.

**Follow-ups**
- *Why squared error?* → differentiable, closed form, = MLE under Gaussian noise.
- *Linear in what?* → in parameters, not necessarily in the data.
- *What is the intercept?* → the `ones` column; allows a non-zero offset.

**If stuck:** draw a line through scattered points and the residuals it minimises.

<div style="page-break-after: always"></div>

## Topic 4 — Practical Aspects of Linear Regression
*Lecture L07 · backs: Parts C7, D, E*

**Say this (board plan)**
1. **Standardize** inputs ($(x-\mu)/\sigma$): comparable scales + better-conditioned $X^T X$.
2. **Correlation vs covariance**; correlation $\in [-1, 1]$, dimensionless.
3. **Multicollinearity**: correlated inputs → near-singular $X^T X$ → unstable, huge
   coefficients → drop redundant features (feature selection).
4. **PCA**: rotate onto orthogonal directions of max variance → decorrelate /
   reduce dimension (choose #PCs by the elbow rule).
5. **Training vs testing**; over- vs under-fitting; pick the model order that
   minimises *testing* error.
6. Watch outliers and clean the data first.

**Formulas**

$$
\begin{aligned}
\text{standardize:}\quad &x_s = \frac{x-\mu}{\sigma} \\
\text{correlation:}\quad &r = \frac{\mathrm{cov}(x,y)}{\sigma_x\,\sigma_y} \in [-1,1]
\end{aligned}
$$

- PCA: $\mathrm{eig}\big(\mathrm{cov}(X)\big)$ → eigenvectors (directions), eigenvalues (variance).
- Overfit: $\mathrm{RMSE_{\text{train}}}\downarrow \text{ but } \mathrm{RMSE_{\text{test}}}\uparrow$.

**Follow-ups**
- *Why remove correlated inputs?* → ill-conditioning, unreliable coefficients.
- *Why standardize before PCA?* → so large-scale variables don't dominate.
- *How to detect overfitting?* → gap between training and testing RMSE.

**If stuck:** "the maths is the same as Topic 3 — these are the things that make
it work on real, messy data."

<div style="page-break-after: always"></div>

# II — DYNAMIC IDENTIFICATION

## Topic 5 — Filtration of Dynamic Signals
*Lecture L08 · backs: Part F*

**Say this (board plan)**
1. Real signals = useful dynamics + noise, separated by **frequency content**.
2. **Low-pass** keeps the slow trend (smoothing); **high-pass** keeps the fast
   part; band-pass keeps a middle band. The **cut-off frequency** sets the split.
3. A **moving average** is a FIR low-pass filter; bigger window = more smoothing.
4. **Causal** (`filter`) uses only past samples → adds a **time delay**;
   **zero-phase** (`filtfilt`, forward+backward) → no delay.
5. Trade-off: more smoothing removes noise but also flattens real dynamics.

**Formulas**

$$
y_{s,k} = \frac{1}{n}\sum_{i=0}^{n-1} y_{k-i} \quad(\text{moving average — FIR, low-pass})
$$

- Causal `filter` → phase delay; `filtfilt` → zero phase (no lag).
- Low-pass: keep low frequencies; high-pass: keep high frequencies.

**Follow-ups**
- *Why zero-phase?* → keeps the smoothed output time-aligned (used for the test
  output in Assignment 2).
- *Low- vs high-pass for noise?* → noise is high-frequency → low-pass to remove it.
- *Downside of heavy smoothing?* → you lose the fast dynamics you want to identify.

**If stuck:** sketch a noisy curve and a smooth line through it; note the lag a
causal filter would add.

<div style="page-break-after: always"></div>

## Topic 6 — Modelling of Dynamic Systems
*Lecture L09 · backs: Part G*

**Say this (board plan)**
1. **Dynamic** = output has **memory** (depends on past inputs/outputs), unlike a
   static map.
2. LTI systems: output = **convolution** of input with the **impulse response**.
3. **FIR** model: $y_k = \sum b_i u_{k-i}$ — weights = impulse response; all-zero,
   **always stable**, needs **high order**.
4. **ARX** model: $y_k = -\sum a_i y_{k-i} + \sum b_i u_{k-i}$ — uses past outputs
   (feedback); **few parameters**, can be unstable.
5. **ARMAX** = ARX + a moving-average term on past **errors** → captures
   disturbances and self-corrects online.
6. All are **linear in the parameters** (ARMAX needs nonlinear optimization for the
   $c$ part) → least squares with a regressor of lagged samples (`X\y`).
7. Transfer function in $z^{-1}$ (unit delay). FIR vs ARX: ARX usually lower RMSE
   with far fewer parameters.

**Formulas**

$$
\begin{aligned}
\text{convolution:}\quad &y(t) = \int_0^t g(\tau)\,u(t-\tau)\,d\tau \quad(g=\text{impulse response}) \\
\text{FIR:}\quad &y_k = \sum_{i=1}^{m} b_i u_{k-i} \\
\text{ARX:}\quad &y_k = -\sum_i a_i y_{k-i} + \sum_i b_i u_{k-i} \\
\text{ARMAX:}\quad &y_k = -\sum_i a_i y_{k-i} + \sum_i b_i u_{k-i} + \sum_i c_i e_{k-i} \\
&G(z^{-1}) = \frac{\sum_i b_i z^{-i}}{1 + \sum_i a_i z^{-i}}, \qquad z^{-1}=\text{unit delay}
\end{aligned}
$$

**Follow-ups**
- *FIR vs ARX?* → FIR all-zero/stable/high-order; ARX poles+zeros/few-params/can be
  unstable.
- *What does ARMAX add?* → an MA term on past errors that absorbs **disturbances**
  (leaking valve, feed change), freeing $a,b$ to learn the true dynamics.
- *Why does FIR need order ~50?* → no feedback; memory window $\tau = m\cdot T_s$ must
  span the settling time ($m=50$, $T_s=0.02$ → only 1 s), and higher orders barely help.
- *What is $z^{-1}$?* → one-sample delay: $z^{-1} y_k = y_{k-1}$.

**If stuck:** "it's still least squares — only the regressor matrix (now made of
lagged inputs and outputs) changes."

<div style="page-break-after: always"></div>

## Topic 7 — Recursive Identification
*Lecture L11 · backs: Part R*

**Say this (board plan)**
1. **Batch** LS reprocesses all data; **recursive** updates the estimate with each
   new sample → **online / real-time** identification.
2. **RLS** structure: **new estimate = old estimate + gain × innovation**, where the
   **innovation** is the prediction error.
3. The covariance $P$ (confidence, starts large) and the gain $K$ (= **Kalman gain**).
4. **Forgetting factor $\lambda$**: $1$ = standard RLS ($\equiv$ batch LS); $<1$
   discounts old data → **tracks time-varying parameters** (tracking vs noise trade-off).
5. RLS is a special case of the **Kalman filter**.
6. Simplest version = the **bias update**: when only a constant offset drifts, shift
   $b$ by the prediction error (optionally filtered by a trust gain $\delta$).

**Formulas**

$$
\begin{aligned}
e_k &= y_k - \phi_k^T \theta_{k-1} \quad(\text{innovation / prediction error}) \\
K_k &= \frac{P_{k-1}\,\phi_k}{\lambda + \phi_k^T P_{k-1}\,\phi_k} \quad(\text{gain}) \\
\theta_k &= \theta_{k-1} + K_k\,e_k \quad(\text{update estimate}) \\
P_k &= \frac{1}{\lambda}\big(P_{k-1} - K_k\,\phi_k^T P_{k-1}\big) \quad(\text{update covariance}) \\
\text{bias:}\quad b_k &= b_{k-1} + (y_{k-1} - \hat{y}_{k-1}), \quad \delta \in [0,1] \\
\text{scalar:}\quad a_N &= a_{N-1} + \frac{x_N}{\sum_k x_k^2}\,(y_N - a_{N-1}x_N)
\end{aligned}
$$

**Follow-ups**
- *Why recursive?* → real-time use; time-varying systems; no need to store all data.
- *What does $\lambda$ do?* → $\lambda<1$ forgets old data to follow drift; smaller = faster but noisier.
- *Link to batch LS / Kalman?* → $\lambda=1 \Rightarrow$ same as batch LS; RLS = Kalman for constant params.
- *Simplest case?* → bias update — adapt only the offset; same "old + gain × error" shape.

**If stuck:** write the one-line mantra "**old + gain × innovation**" and explain
each term.

<div style="page-break-after: always"></div>

## Topic 8 — Practical Aspects of Identification
*Lecture L10 · backs: Parts G6, H, E*

**Say this (board plan)**
1. **Experiment design**: the input must be **persistently exciting** (rich in
   frequencies) or the dynamics can't be seen.
2. Input types: **step** (few frequencies) → **random** → **PRBS** (near-white,
   preferred, reproducible).
3. **Sampling time** $T_s$: too big → aliasing/miss fast dynamics; too small →
   noisy/stiff.
4. **Model-order selection** from **ACF/PACF** of the output (PACF → AR order $n$).
5. **Static vs dynamic / linearity check**: step $\tfrac13,\tfrac23,1$ → proportional
   = static gain; same-sign-but-not-proportional = nonlinear-bearable; **sign flip =
   red alert** (uncontrollable by a linear controller).
6. **Unstable plant** → identify the **closed loop** (controller + plant in one box,
   reference → response), then fit ARX.
7. **Validation**: training vs testing RMSE; one-step prediction vs free
   simulation; residual checks; avoid overfitting.
8. Real workflow (**Flexy²**, Assignment 2): clean → standardize → split → FIR/ARX
   → compare.

**Formulas**
- **Persistent excitation:** input rich enough to excite all modes.
- **PRBS:** 2-level pseudo-random, near-white spectrum (best dynamic input).
- **Order:** PACF drops inside the confidence band at lag $n$ $\Rightarrow$ AR order
  $n$; keep $m \le n$.
- **Validate** on **testing** data; free simulation is the harder test.

**Follow-ups**
- *Why PRBS over a step?* → step excites few frequencies; PRBS excites a broad band.
- *How to choose order?* → ACF/PACF; smallest order that captures dynamics (parsimony).
- *Train vs test?* → train fits parameters, test gives the honest accuracy; gap = overfit.
- *Why clean the data first?* → bad regions (dead-zero start, saturated end) break the
  input→output link and bias the regressor → higher RMSE.
- *One-step-ahead vs simulation?* → OSA uses real past outputs (easier, lower RMSE);
  compare models the *same* way to be fair.
- *How tell static from dynamic?* → step changes; immediate scaled output = static,
  no point fitting a dynamic model.
- *Unstable plant?* → can't run open-loop; identify the closed loop with an existing
  stabilizing controller.

**If stuck:** describe your Assignment 2 pipeline end-to-end — it touches every
practical point.
