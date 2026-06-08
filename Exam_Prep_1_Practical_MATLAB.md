# Identification — Practical Exam Preparation (MATLAB)

> Goal: be able to sit at MATLAB and, from raw measured data, reproduce the
> full identification workflow taught in seminars 1–11 and Assignments 1–2.
> Every code block below is a **reusable template** — memorize the *pattern*,
> not the exact numbers.

---

## 0. The standard workflow (memorize this skeleton)

Almost every task in this course follows the same pipeline:

1. **Load** data (`readtable`, `load`, or `sim`)
2. **Visualize** raw signals (time series + scatter/dependency)
3. **Clean** the data (remove outliers / bad operating regions)
4. **Standardize** (zero mean, unit variance)
5. **Split** into training (TV) and testing (TS) datasets
6. **Fit a model** by least squares (`X\y`)
7. **Predict** and evaluate with **RMSE**
8. **Compare** models / visualize fit (parity plot, overlay)

Keep this skeleton in your head — the exam task is usually a variation of it.

### House-keeping header used everywhere
```matlab
clc; clear all; close all; rng(100);   % rng for reproducible random numbers
```

### The plotting boilerplate (reused in every figure)
```matlab
figure; hold on; grid on; box on; text = [];
plot(x, y, '.r', 'MarkerSize', 10);          text = [text; {'Measurements'}];
legend(text, 'Interpreter', 'latex', 'Location', 'best');
xlabel('$x$', 'Interpreter', 'latex');
ylabel('$y$', 'Interpreter', 'latex');
set(gca, 'FontSize', 15, 'ticklabelinterpreter', 'latex');
set(gcf, 'Position', [100, 100, 1400, 600]);
```
*The `text = [text; {...}]` trick builds the legend cell array incrementally,
one entry per `plot` call.*

---

## 1. Loading & visualizing data (Seminar 1, 3, 4)

```matlab
% From CSV / table
data  = readtable('tank_data.csv');
time  = table2array(data(:,1));        % or  data.Year
h     = table2array(data(:,9));

% From .mat
d = load('data_FCC_dep_XY_anonymous.mat');   % gives struct d.X, d.Y, ...

% Save / load to skip slow recomputation (the "con" switch pattern)
con = 1;
if con == 1
    data = sim('s_gas_tank', time);     % run Simulink, slow
    save('data_training', 'data');
else
    load('data_training');              % reuse, fast
end
```

**Log-scale plotting** (for exponential growth, e.g. Moore's law):
```matlab
set(gca, 'YScale', 'log');              % or 'xscale','log'
plot(t, log(y), '-*');                  % alternative: transform the data
```

---

## 2. Descriptive statistics (Seminar 1, 2)

```matlab
n   = length(x);
mu  = mean(x);              %  = 1/n * sum(x)
s   = std(x);               %  = sqrt( 1/(n-1) * sum((x-mu).^2) )  (sample std, N-1)
v   = var(x);               %  = s^2
med = median(x);
g   = geomean(x);
```
Know that `std`/`var` use the **N−1** (unbiased) denominator by default.

### Counting data inside ±3σ (Seminar 2)
```matlab
idx_in  = find(abs(x) <= 3);            % within 3 sigma
idx_out = find(abs(x) > 3);
pct_in  = length(idx_in)/length(x)*100; % ~99.7% for normal data
```

---

## 3. Probability distributions: PDF / CDF (Seminar 2)

```matlab
xe = linspace(-5, 5, 1000);

% Build a distribution and evaluate PDF/CDF
pd    = makedist('normal', 'mu', 0, 'sigma', 1);
p_pdf = pdf(pd, xe);
p_cdf = cdf('norm', xe, 0, 1);

% Inverse CDF (quantile): "what x gives this probability?"
x_q   = icdf('normal', 0.841, 0, 1);    % ~ +1 sigma

% Overlay theoretical PDF on a normalized histogram
figure; hold on; grid on;
histogram(x, 'Normalization', 'pdf');
plot(xe, p_pdf, '.k');
```
- Larger sample size → histogram converges to the theoretical PDF (law of large numbers).

---

## 4. Least-squares model fitting

**Everything** in this course is solved with the MATLAB backslash:
```matlab
p = X \ y;          % solves  min || X*p - y ||^2   (normal equations)
yhat = X * p;       % model prediction
```
`X` is the **regressor (design) matrix** — each column is one basis function /
feature, each row one measurement.

### Static-model examples (Seminars 3, 5)
```matlab
% Tank:  q1 = k * sqrt(h)   (no intercept)
k    = sqrt(h) \ q1;
q1c  = k * sqrt(h);

% Linear with intercept:  V = p1*T + p0
p1   = [T, ones(size(T))] \ V;
Vhat = [T, ones(size(T))] * p1;

% Try several structures and compare:
pLin = [T,     ones(size(T))] \ V;     % linear
pQua = [T.^2,  ones(size(T))] \ V;     % quadratic
pInv = [1./T,  ones(size(T))] \ V;     % inverse
```
**Tip:** building `X` with `[feature, ones(size(...))]` adds an intercept
(bias) term. Drop the `ones` column for a through-origin fit.

---

## 5. Accuracy: RMSE and the parity plot

```matlab
RMSE = sqrt(mean((yhat - y).^2));       % manual
RMSE = rmse(yhat, y);                   % built-in (newer MATLAB)
```

### Parity / predicted-vs-measured plot (recurring exam graphic)
```matlab
figure; hold on; grid on; box on;
plot(y, yhat, '.m', 'MarkerSize', 10);                 % points
lims = [min([y;yhat]), max([y;yhat])];
plot(lims, lims, '--k');                               % ideal 45° line
xlabel('Measured $y$', 'Interpreter', 'latex');
ylabel('Predicted $\hat{y}$', 'Interpreter', 'latex');
```
Points on the diagonal = perfect prediction. Scatter away from it = error.

---

## 6. Standardization (Seminars 5, 7, 9)

```matlab
xs = (x - mean(x)) / std(x);            % zero mean, unit variance
```
Validate numerically — `mean(xs) ≈ 0`, `std(xs) ≈ 1`:
```matlab
disp(['mu = ', mat2str(round(mean(xs),4)), ', sigma = ', mat2str(round(std(xs),4))]);
```
**Watch-out:** a *constant* signal has `std = 0` → division by zero.
Guard it (Assignment 2, the noise channel `n`):
```matlab
if std(n) == 0, ns = zeros(size(n)); else, ns = (n-mean(n))/std(n); end
```

---

## 7. Correlation, covariance, PCA (Seminars 6, 7)

```matlab
% Pearson correlation coefficient between two variables
c = corrcoef(x1, x2);  c = c(1,2);      % off-diagonal element, in [-1, 1]

% Covariance & correlation matrices
K  = cov(X);                            % covariance
R  = corrcoef(X);                       % correlation (standardized covariance)

% Visual correlation matrix of many variables
corrplot(X, 'varNames', tags);

% Eigen-decomposition of the covariance (principal directions)
[eigvec, eigval] = eig(K);

% Draw the covariance "ellipse" (1σ/2σ/3σ) — Seminar 7
nc = 1000;  Xc = [cos(linspace(0,2*pi,nc))', sin(linspace(0,2*pi,nc))'];
ellipse = mean(X) + Xc * sqrtm(K);      % sqrtm = matrix square root
```

### PCA (Seminar 7, Task 6–7)
```matlab
[COEFF, SCORE, LATENT, TSQ, EXPLAINED, MU] = pca(X);
% COEFF    = principal directions (loadings)
% SCORE    = data in PC coordinates
% EXPLAINED= % variance explained per PC
% Reconstruct:  X_centered ≈ SCORE * COEFF'
```
**Knee/elbow rule** to choose the number of PCs: draw a line from first to last
point of the `EXPLAINED` curve; the point with max distance to that line is the
elbow:
```matlab
it = (1:numel(EXPLAINED))';
p  = [it(1) 1; it(end) 1] \ [EXPLAINED(1); EXPLAINED(end)];
d  = abs([it ones(size(it))]*p - EXPLAINED);
idx = find(d == max(d));                 % elbow index
```

---

## 8. Multivariate regression + train/test (Seminars 6, 7)

```matlab
% Feature selection: drop linearly-dependent / collinear columns
idx_remove        = sort([8;15;13;18]);
Xsel              = X;  Xsel(:,idx_remove) = [];

% Train / test split
nTR   = 100;
Xtr   = X(1:nTR,:);   Xts = X(nTR+1:end,:);
ytr   = y(1:nTR);     yts = y(nTR+1:end);

p          = Xtr \ ytr;                  % train on TR only
RMSE_tr    = sqrt(mean((Xtr*p - ytr).^2));
RMSE_ts    = sqrt(mean((Xts*p - yts).^2));  % honest test error
```
**Overfitting signal:** `RMSE_tr` small but `RMSE_ts` large → too many features.

### 95% confidence interval on regression (Seminar 5)
```matlab
[b, bint] = regress(y, X);               % bint = 95% CI for each coefficient
```

---

## 9. Signal filtering / smoothing (Seminars 8, Assignment 2)

```matlab
yl = lowpass(y, 0.001);                  % keep slow trend (small Wn)
yh = highpass(y, 0.1);                   % keep fast noise

% Moving-average FIR smoother, window n:
n  = 50;  b = ones(n,1)/n;
ys = filter(b, 1, y);                    % causal (introduces delay)

% Zero-phase smoothing (no time delay) — used to build TEST output in Assign. 2
win  = 201;  b_ma = ones(1,win)/win;
ytest = filtfilt(b_ma, 1, y);            % forward-backward => no lag
```
- **Low-pass** removes noise but lags / smooths edges.
- **filtfilt** = zero phase: same smoothing, **no delay** (used for the smoothed
  testing reference).

---

## 10. Dynamic system identification — FIR & ARX (Seminars 9–11, Assignment 2)

Both models are still just least squares; only the regressor matrix changes.

### FIR model  `y_k = Σ b_i · u_{k-i}`  (output = weighted past inputs)
```matlab
m = 50;  N = length(u);                 % m = model order (# past inputs)
Phi = zeros(N-m, m);  Y = zeros(N-m,1);
for k = (m+1):N
    Phi(k-m,:) = u(k-1:-1:k-m)';        % [u(k-1), u(k-2), ..., u(k-m)]
    Y(k-m)     = y(k);
end
b    = Phi \ Y;                         % FIR coefficients (impulse response)
yhat = Phi * b;
RMSE = sqrt(mean((yhat - Y).^2));
```

### ARX model  `y_k = -Σ a_i·y_{k-i} + Σ b_i·u_{k-i}`  (uses past *outputs* too)
```matlab
n = 3; m = 3; p = max(n,m);  N = length(y);
Phi = zeros(N-p, n+m);  Y = zeros(N-p,1);
for k = (p+1):N
    ylag = -y(k-1:-1:k-n)';             % NOTE the minus sign on output lags
    ulag =  u(k-1:-1:k-m)';
    Phi(k-p,:) = [ylag, ulag];
    Y(k-p)     = y(k);
end
theta = Phi \ Y;                        % [a1..an, b1..bm]
a = theta(1:n);  b = theta(n+1:end);
yhat = Phi * theta;
```

### ARMAX model  `y_k = -Σ a_i y_{k-i} + Σ b_i u_{k-i} + Σ c_i e_{k-i}`
ARX plus a moving-average term on **past errors** — models disturbances and
self-corrects online. The `c` part makes it **nonlinear** in the parameters, so
plain `\` no longer works; use the System Identification Toolbox:
```matlab
dataID = iddata(y, u, Ts);               % package output/input
na = 2; nb = 2; nc = 2; nk = 1;          % AR / X / MA orders + input delay
sysARMAX = armax(dataID, [na nb nc nk]); % iterative (nonlinear) estimation
ypred = predict(sysARMAX, dataID, 1);    % 1-step-ahead prediction
```
Use ARMAX when ARX residuals are clearly **correlated** (a sign that an unmodelled
disturbance is leaking into `a, b`).

### Building transfer functions from the coefficients (Seminars 9–10)
```matlab
% FIR:  a = 1,  b = [0, b1..bm]
G_fir = tf([0 b'], 1, Ts, 'Variable', 'z^-1');

% ARX:  a = [1, a1..an],  b = [0, b1..bm]
G_arx = tf([0 b'], [1 a'], Ts, 'Variable', 'z^-1');

% Simulate the model response to an input:
y_sim = lsim(G_arx, u);                 % or  idpoly(a,b,'Ts',Ts) + sim()
```

### Choosing model order with ACF / PACF (Seminar 11, Assignment 2 Task 6)
```matlab
autocorr(y, 'NumLags', 50);             % ACF  -> overall memory / b (MA) order
parcorr(y, 'NumLags', 50);              % PACF -> AR order n: last lag outside
                                        %         the confidence band
```
Rule of thumb taught here: pick `n` where the **PACF** drops inside the
confidence band; keep `m ≤ n` to avoid overfitting.
- A **slowly-decaying ACF** (stays outside the band for hundreds/thousands of
  lags) = a **dominant time constant** / strong long-term memory → you'll need a
  sizeable AR order `n`.

### FIR memory window: why order must be large (Assignment 2 insight)
A FIR model of order `m` only "remembers" the last `m` input samples, i.e. a
**memory window of `τ = m·Ts` seconds**. For a good fit, `τ` must span the
system's **settling time** (how long the step response takes to level off).
```matlab
tau = m * Ts;            % e.g. m=50, Ts=0.02 s  ->  tau = 1 s of memory
```
If the system settles in, say, a few seconds, `m=50` (1 s) is **underfit**. But
sweeping `m` up to 1000 shows RMSE barely improves — proof that piling on FIR
coefficients is an inefficient substitute for the feedback that ARX provides.
```matlab
for mi = [10 25 50:50:1000]              % RMSE-vs-order sweep
    [~,Gi] = deal(fir_train(u,y,mi));    % refit, predict, store RMSE(mi)
end                                       % curve flattens -> diminishing returns
```

### One-step-ahead prediction vs free simulation (how you evaluate matters)
Two different ARX "predictions" give very different RMSE:
```matlab
% (a) One-step-ahead (OSA): regressor uses the REAL measured past outputs
y_osa = Phi * theta;                     % Phi built from actual y(k-1..k-n)
% (b) Free simulation: model feeds its OWN past outputs back
y_sim = lsim(G_arx, u);                  % only u is given
```
- **OSA** is the easier task → lower RMSE (the near-zero ARX test RMSE in
  Assignment 2 is OSA on *smoothed* test data). **Free simulation** is the
  honest, harder test. When comparing models, evaluate them the **same way** —
  comparing ARX-by-OSA against FIR-by-`lsim` is not fully apples-to-apples.

---

## 11. Designing the INPUT signal (Seminars 8–11)

Good identification needs a **persistently exciting** input (rich in frequencies):

```matlab
% Step changes (staircase)
u(1:200) = 1200; u(201:400) = 1000; ...   % piecewise constant

% Random uniform levels
u(idx) = 0 + (10-0).*rand;

% PRBS — pseudo-random binary sequence (best for dynamics)
sig = prbs(5, 100);                       % order 5, 100 samples
u   = sig * 10;
```
- A pure step excites few frequencies; **PRBS** excites a broad band → better
  dynamic models. (Hint in Assignment 2 Task 1: "systems react differently to
  slow and fast changes — choose an input that captures all dynamics.")

---

## 12. Assignment 2 task map (likely practical-exam template)

| Task | What to do | Key MATLAB |
|------|-----------|-----------|
| 1 | Load Flexy² data, plot u, n, y | `interp1(..,'previous')`, `plot` |
| 2 | Remove bad sections (e.g. y>40%, zero-fan) | `find`, index trim |
| 3 | Standardize; pick `u` not constant `n` | `(x-mean)/std` |
| 4 | Train = noisy, Test = zero-phase smoothed y | `filtfilt(ones(1,201)/201,1,y)` |
| 5 | FIR order 50, RMSE on TR/TS | loop builds `Phi`, `Phi\Y` |
| 6 | ARX, order from ACF/PACF, RMSE | `autocorr`,`parcorr`, `Phi\Y` |
| 7 | Compare FIR vs ARX (overlay + RMSE bar) | `bar([...])` |

> **Why FIR needs high order (~50):** it has no feedback (no `a` terms), so it
> must approximate the whole impulse-response tail with many `b` coefficients.
> **ARX** captures the same dynamics with far fewer parameters because the
> recursive `a·y_{k-i}` terms model the decay implicitly → usually lower RMSE.

---

## 13. Common pitfalls / quick checklist

- [ ] Used `rng(100)` so random results are reproducible?
- [ ] `std`/`var` are **N−1** based — don't re-divide.
- [ ] Standardizing a **constant** channel → guard against `÷0`.
- [ ] Regressor `Phi` must use **past** samples only (`u(k-1:-1:k-m)`), never `u(k)`.
- [ ] ARX output lags carry a **minus sign** in `Phi`.
- [ ] Evaluate RMSE on **testing** data for the honest accuracy.
- [ ] Skip the first ~100 transient samples before computing RMSE (`idx_ac=100`).
- [ ] Parity plot diagonal must be the **same** axis limits on x and y.
- [ ] For "no time delay" smoothing use `filtfilt`, not `filter`.

---

## 14. Lecture map (Ident_2025 — UIAM FCHPT, 11 lectures, 15.5 h)

The **Ident_2025** playlist is the **theory-lecture** series (the seminars are
the MATLAB practice). Use this to line up each lecture with the matching seminar
code and the relevant section of these notes.

| # | Lecture (video title) | Matching seminar | Notes § |
|---|----------------------|------------------|---------|
| L01 | Introduction to Identification. Data Visualization. | `seminar1.m` | §1, §2 |
| L02 | Introduction to Statistics | `seminar2.m` | §2, §3 |
| L03 | Estimation of a Constant #1 | `seminar3.m`,`seminar4.m` | §2, §4, §5 |
| L04 | Estimation of a Constant #2 | `seminar4.m` | §4, §11 |
| L05 | Linear Regression #1 | `seminar5.m` | §4, §5 |
| L06 | Linear Regression #2 | `seminar6.m` | §6, §8 |
| L07 | Practical Aspects of Linear Regression | `seminar7.m` | §7, §8 |
| L08 | Filtration of Dynamic Signals | `seminar8.m` | §9 |
| L09 | Identification of Dynamic Systems | `seminar9.m` | §10 |
| L10 | Practical Aspects of Identification | `seminar10.m`,`seminar11_Flexy2.m` | §10, §11, §12 |
| L11 | **Recursive Estimation** | *(no seminar — theory only)* | **§13a** |

- **"Estimation of a constant"** (L03/L04) = estimating a single parameter from
  noisy repeated measurements (the `k11` tank constant in Seminar 4: arithmetic
  mean vs geometric mean vs median, their spread via box plots).
- **L11 Recursive Estimation** is the one lecture topic with **no seminar** — its
  practical recipe is in the new §13a below.

---

## 13a. Recursive Least Squares — RLS (Lecture L11)

**Idea:** instead of recomputing `X\y` over the *whole* dataset every time a new
sample arrives, **update** the previous estimate with just the new measurement.
Used for online / real-time identification and for time-varying systems.

### The RLS update (per new sample k)
```matlab
% --- Recursive Least Squares with forgetting factor ---
lambda = 1;                 % forgetting factor: 1 = standard RLS (all data equal)
                            %                    <1 (e.g. 0.95..0.99) tracks change
np     = size(Phi, 2);      % number of parameters
theta  = zeros(np, 1);      % initial parameter estimate
P      = 1e6 * eye(np);     % initial covariance: large = "I trust data, not prior"
Theta  = zeros(np, N);      % to store the parameter trajectory

for k = 1:N
    phi   = Phi(k, :)';                       % current regressor (column vector)
    e     = y(k) - phi' * theta;              % innovation / prediction error
    K     = P*phi / (lambda + phi'*P*phi);    % Kalman-type gain (a vector)
    theta = theta + K * e;                    % CORRECTION: update estimate
    P     = (P - K*phi'*P) / lambda;          % update covariance
    Theta(:, k) = theta;                      % log evolution
end
```

### What each piece means
| Symbol | Meaning |
|--------|---------|
| `theta` | current parameter estimate (updated each step) |
| `e` | **innovation** = new info the sample brings (measured − predicted) |
| `P` | covariance of the estimate (shrinks as confidence grows) |
| `K` | gain — how strongly the new error corrects the estimate |
| `lambda` | **forgetting factor** ∈ (0,1]; `1` = remember all, `<1` = discount old data |

### Key facts to remember
- With `lambda = 1`, after processing **all** N samples RLS gives the **same
  result as batch least squares** `X\y`, computed incrementally. (Strictly exact
  in the limit of a large initial `P`; with the finite `P₀=1e6·I` above it is a
  negligibly regularized version.)
- **`lambda < 1`** makes the estimator "forget" old data exponentially → it can
  **track parameters that drift** (time-varying systems). Smaller λ = faster
  tracking but noisier estimates (trade-off).
- Large initial `P` (e.g. `1e6·I`) = low confidence in the guess → fast initial
  convergence. Small `P` = strong trust in the initial `theta`.
- RLS is a special case of the **Kalman filter** (the gain `K` is the Kalman gain).
- Plot `Theta` rows vs `k` to show the estimates converging to their true values.

### Bias update — the one-line recursive scheme (L11)
When only a constant **offset** has drifted (slope still good), adapt just `b`:
```matlab
delta = 0.95;                              % trust gain in [0,1]; ->1 = slow/cautious
for k = 2:N
    yhat = a*x(k-1) + b;                   % prediction with current bias
    b    = delta*b + (1-delta)*(b + (y(k-1) - yhat));   % filtered bias update
end
```
Same "estimate ← estimate + gain × prediction-error" shape as a P controller;
`delta→1` ignores noisy single points, `delta=0` follows the latest measurement.

---

## 15. Function cheat-sheet

| Need | Function |
|------|----------|
| Least squares | `X\y` |
| RMSE | `sqrt(mean((yh-y).^2))` / `rmse` |
| Mean/std/var/median | `mean std var median geomean` |
| PDF/CDF/quantile | `pdf cdf icdf makedist` |
| Histogram | `histogram(...,'Normalization','pdf')` |
| Correlation | `corrcoef` , `corrplot` |
| Covariance | `cov` , `sqrtm` , `eig` , `chol` |
| PCA | `pca` |
| Reg. confidence interval | `regress` |
| Filters | `lowpass highpass filter filtfilt` |
| Dyn. model order | `autocorr parcorr` |
| Transfer function | `tf idpoly lsim sim` |
| Input design | `prbs rand` |
| Simulink run | `sim('model', time)` |
