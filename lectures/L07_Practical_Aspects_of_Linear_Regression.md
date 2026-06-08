---
lecture: L07
title: "Practical Aspects of Linear Regression"
course: Identification
source: "https://www.youtube.com/watch?v=HqCN0mFgmTQ"
---

# L07 — Practical Aspects of Linear Regression

> Formulas verified against the titled slide deck (*Identification L07 — Practical
> aspects of lin reg*). On camera the lecturer was unsure about the constant in the
> parameter-covariance result; the slide gives the clean
> $V_P = \sigma_y^2 (X^TX)^{-1}$, used below.

This lecture is mostly practical. The running example is a **distillation column**
with many measured temperatures, pressures, and sometimes compositions; a typical
goal is to predict the **composition** of a distillate or bottom stream, which
physical chemistry (vapour–liquid equilibria) says should be correlated with
temperature and pressure. The problem is an **abundance** of measurements.

## Choosing the model terms

The prediction model is $\hat{y} = X p$. Columns of $X$ can be temperature at the
first tray, temperature at the second tray, pressure at the top, pressure at the
bottom, and so on — including **nonlinear transformations**: products, the
distillate-to-feed ratio $D/F$, or $e^{T}$ (Arrhenius law). A simpler version is a
**polynomial** in one variable:

$$
\hat{y} = p_0 + p_1 x + p_2 x^2 + p_3 x^3 + \dots
$$

(Two variables would add cross terms.) The question is how to **select** reasonable
terms.

## Correlation vs. dependence

Building on last time's correlation concept: is "correlated" the same as
"dependent"? No — it is a **one-sided implication** (slide):

$$
\text{correlation} \;\Longleftarrow\; \text{dependence (causality)}
$$

If variables are **dependent**, that **implies** correlation (we should see it in
the correlation coefficient). But **correlation does not imply dependence** —
recall the students-abroad example, where the numbers were correlated only because
the COVID pandemic dropped them all at once.

### Correlation among inputs is unwanted; with the output it is desired

- **$x_1, x_2$ correlated — unwanted.** Correlation *among the independent
  variables* (collinearity) is a problem.
- **$x_1, y$ correlated — desired.** We *want* an input to correlate with the
  output we predict; otherwise the parameter could take an essentially random
  value unrelated to reality.

### Why collinearity is harmful

Suppose a two-input model $\hat{y} = p_1 x_1 + p_2 x_2$, but unknown to us
$x_1 = k\,x_2$ (two nearby distillation trays are strongly correlated, or the
experiment was run by always increasing temperature and pressure together).
Substituting:

$$
\hat{y} = p_1 k\, x_2 + p_2 x_2 = (p_1 k + p_2)\, x_2
$$

Only **one** effective parameter exists. If, say, $k = 1$ and the true value of the
bracket is $3$, then any $p_1, p_2$ with $p_1 + p_2 = 3$ is a valid regression
result — $(1, 2)$, $(\tfrac{1}{2}, 2\tfrac{1}{2})$, $(-5, 8)$, … — an unwanted
**extra degree of freedom** that makes the "physical" parameters meaningless.

Geometrically (3D): the data lie along a line in the $x_1$–$x_2$ plane, and **any
plane rotated about that line** fits equally well — the fit is non-unique. When the
points are well spread, it is hard to wiggle the plane away from the data. The
remedy: build the covariance matrix, check correlations, and **remove correlated
independent variables**, keeping $x_1, x_2$ as independent as possible.

## Polynomial fitting, overfitting and extrapolation

For a one-variable polynomial fit of scattered data:

- A **linear** fit may not be bad — the residuals can look like normal
  measurement noise.
- A **quadratic** fit may track most points.
- An **octic** (8th-degree) fit passes through almost every point — but it is
  **fitting the noise**, which we do not want. We want to fit the *information* in
  the data, not the noise.

**Do not extrapolate.** Outside the training range the high-degree polynomial
escapes wildly. Even a **linear** model can be extrapolated only a little (e.g.
doubling the interval is already too far). Collect data over the **full range**
where the model must be valid — otherwise a change in plant operation (different
crude oil, a different supplier's raw material) makes the model fail and "your boss
tells you it doesn't work."

Why try polynomials at all? Because of the **Taylor expansion** — any nonlinear
function can be approximated by a polynomial, so polynomials are good
approximators. With physical insight (distillation) one can guess the shape
(exponential, logarithmic); for things like Bitcoin price the underlying reality is
much harder to know.

## Cross validation

To choose model complexity, use **cross validation**: split the data (slide ratio
**50 : 30 : 20**) into

- **Training (TR)** — used to compute the parameter values;
- **Validation (V)** — used to decide the model order/complexity;
- **Testing (TS)** — typically ~20%, locked "in a vault" before anything else and
  used only for the **final** performance stamp (as if the model went live).

Plotting a performance measure (e.g. RMSE) against model complexity $n_p$ (number
of parameters):

- **Training** error **decreases monotonically** as terms are added — optimization
  keeps pleasing us, even fitting noise (the octic fit), so training alone never
  reveals the best model.
- **Testing / validation** error **decreases then increases**, revealing an optimal
  complexity $n_p^{*}$. Since the real testing data are hidden, the **validation**
  data simulate them for the order-selection decision.

## Assessment criteria

Do not rely on a single number; check several for each candidate model.

### Root mean squared error (RMSE)

$$
\text{RMSE} = \sqrt{\frac{1}{N}\sum_{k=1}^{N}\big(y_k - \hat{y}_k\big)^2}
$$

(sometimes RMSPE, root mean squared **prediction** error). It lives in the units
of the data — "our model is off by 0.01 bar."

### Coefficient of determination $R^2$

Compares the model against simply fitting a **constant** (the mean of the data):

$$
R^2 = 1 - \frac{\sum_{k=1}^{N}(y_k - \hat{y}_k)^2}{\sum_{k=1}^{N}(y_k - \bar{y})^2}
$$

The denominator's constant fit is the average $\bar{y}$. When the model's residual
sum (numerator) is small relative to the constant-fit sum (denominator),
$R^2 \to 1$. By construction $R^2 \in [0, 1]$ (1 = perfect, 0 = no better than a
constant). A **negative** $R^2$ signals an **error** in fitting the model.

### Parity plot

Plot **prediction vs. measurement** (a parity / correlation plot). Useful even
when more than two or three independent variables make other plots impractical.

- Points on the **diagonal** $\hat{y} = y$ (up to noise) — **good**, very
  desirable.
- A consistent **offset with a correct trend** (predict larger → measure larger,
  but shifted) — a **missing regressor / input**: some dependence (e.g. on
  pressure) was disregarded.
- An **okayish-then-deviating** shape — likely **nonlinear behavior** not included
  in the model.

## Confidence intervals of the parameters

For lots of data the statistics work well, and confidence intervals can flag an
**overfitted** parameter: if the interval **contains zero**, the model can live
without that parameter with the same probability level.

Build the **parameter covariance matrix** analogously to the data covariance:

$$
V_P = E[P P^T], \qquad
V_P = \begin{pmatrix} \sigma_{p_1}^2 & \sigma_{p_1 p_2} & \cdots \\
                      \sigma_{p_1 p_2} & \sigma_{p_2}^2 & \\
                      \vdots & & \ddots \end{pmatrix}
$$

($P$ is $n_p \times 1$, so $P P^T$ is the $n_p \times n_p$ matrix.) Substituting
$P = (X^T X)^{-1} X^T y$ and its transpose $P^T = y^T X (X^T X)^{-1}$ (using
symmetry of $X^T X$):

$$
V_P = E\!\left[(X^T X)^{-1} X^T y\, y^T X (X^T X)^{-1}\right]
$$

Assume **independent, constant measurement noise**, so $E[y y^T] = V_y =
\sigma_y^2 I$. Pulling out $\sigma_y^2$, the inner $X^T X$ cancels with one
$(X^T X)^{-1}$ (an $A^{-1} A$ pair):

$$
V_P = \sigma_y^2\, (X^T X)^{-1}
$$

**Interpretation:** parameter uncertainty grows with the noise $\sigma_y^2$, and —
because of the inverse — **shrinks as more measurements** make $X^T X$ grow (just
like estimating a constant). It also depends on the **experiment design** (the
choice of independent data): if the points lie on a line, $X^T X$ is not
invertible (the collinearity problem above).

### The parameter distribution and confidence ellipse

Treating $P$ as a random vector, $P \sim N(\hat{P}, V_P)$, the multivariate
Gaussian PDF (the matrix generalization of the scalar
$\frac{1}{\sqrt{2\pi}\,\sigma}e^{-(x-\bar{x})^2/2\sigma^2}$) is:

$$
\text{pdf}(p) = \frac{1}{(\sqrt{2\pi})^{n_p}\,\lvert V_P^{1/2}\rvert}\,
  e^{-\frac{1}{2}(p - \hat{P})^T V_P^{-1}(p - \hat{P})}
$$

Here $2\pi$ carries an exponent (normalization in several variables) and the scalar
$\sigma$ becomes a **matrix square root** combined with a **determinant** to give a
single number. The exponent is a **quadratic form** with $V_P^{-1}$ in place of
dividing by the variance.

Shining a "torch" along the $p_1$ axis projects (marginalizes) the multidimensional
bell back to a 1-D Gaussian for $p_1$ (and likewise $p_2$). The **level sets** of
the PDF are **ellipses**; a contour plot shows that, e.g., the **spread of $p_1$ is
much larger than that of $p_2$** — the data/model determined $p_2$ more accurately.

As in the scalar case, the quadratic form follows a **chi-square** distribution
with $n_p$ degrees of freedom, giving the **confidence region** (slide):

$$
(p - \hat{P})^T V_P^{-1}(p - \hat{P}) \sim \chi^2_{n_p}
$$

$$
(p - \hat{P})^T V_P^{-1}(p - \hat{P}) \le \big(\chi^2_{n_p,\alpha}\big)^{-1}
$$

This is the matrix analogue of a circle $p_1^2 + p_2^2 = r^2$ generalized to an
ellipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$: the semi-axis lengths come from
the confidence intervals (radii), and the off-diagonal entries **tilt / rotate**
the ellipse. (Plotting this ellipse is an exercise; details next time.)

**Warning sign — interval contains zero.** If a 95% confidence interval is, e.g.,
$p \in [-1, 2]$, then all values between $-1$ and $2$ are 95% probable, **including
zero**. The model may be able to live without that parameter — the variable could
be unobservable (linear dependence), under-revealed by the data, or simply have no
causal effect on the output.

## Principal Component Analysis (PCA)

A method used very frequently in data analysis, shown by example. Take 100
black-and-white face images (Steven Tyler, George Bush, Robbie Williams, …), each
pixel valued in $[0, 1]$ (0 = black, 1 = white). With ~10,000 pixels per image, the
data matrix is

$$
X \in \mathbb{R}^{100 \times 10000}
$$

— only **100 observations** but **10,000 variables**. A pixel-wise prediction model

$$
\hat{y} = p_1 x_1 + p_2 x_2 + \dots + p_{10000}\, x_{10000}
$$

would need 10,000 parameters, but you cannot learn 10,000 parameters from 100 data
points (as fitting a line needs at least two points, 10,000 parameters need at
least 10,000 points).

**PCA** does statistics on the data and constructs a small number of **independent,
most-probable combinations** of pixels — here **36 "eigenface" components**
$\tilde{x}_1, \dots, \tilde{x}_{36}$ (e.g. the first captures the common background
color). The reduced model then needs only **36 parameters**:

$$
\hat{y} = p_1 \tilde{x}_1 + \dots + p_{36}\,\tilde{x}_{36}
$$

Reconstructing the images from these components gives recognizable approximations —
enough, for instance, to tell two people apart — **without** fitting 10,000
parameters (most of which would have a zero-containing confidence interval). The
underlying math is relatively easy and is left for next time.
