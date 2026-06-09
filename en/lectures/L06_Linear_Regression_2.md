---
lecture: L06
title: "Linear Regression #2"
course: Identification
source: "https://www.youtube.com/watch?v=DLTnS_SWr_k"
---

# L06 — Linear Regression #2

> Matrix formulas verified against the lecturer's slide deck (*Ident 17 03 2026 /
> 24 03 2026*): the vector-form least-squares derivation, the normal equations /
> pseudoinverse, and the variance-covariance / correlation matrices.

## Recap: the matrix form

We are looking for a **correlation** between independent and dependent measured
data, and heading toward understanding that some experiments are better conducted
than others and some variables are better chosen for a model than others.

We stack the data into the **regressor matrix** $X$ — each **column** a variable
(or a nonlinear transformation of one), each **row** an experiment ($N$
experiments, $n_p$ parameters/variables). The **prediction equation** is

$$
\hat{y} = X p
$$

where $p$ is the parameter vector and $\hat{y}$ holds one prediction per
experiment. Recall the key identity that $x^T x$ equals the **sum of squares** of
the components of $x$.

## Least squares in vector form

Write the least-squares objective with the vector $(y - \hat{y})$ (the
transpose-times-itself gives the sum of squares):

$$
\min_{p}\; \frac{1}{2}\,(\hat{y} - y)^T(\hat{y} - y)
$$

Expand the product into four terms:

$$
\min_{p}\; \frac{1}{2}\Big(\hat{y}^T\hat{y} - \hat{y}^T y - y^T\hat{y} + y^T y\Big)
$$

The two cross terms are **"same but different but still the same"**: $\hat{y}^T y$
and $y^T \hat{y}$ are both scalars and equal because $a^T b = b^T a$. (There is no
well-defined notion of "squaring a vector," which is why we keep the
transpose-product form.) Grouping them:

$$
\min_{p}\; \frac{1}{2}\hat{y}^T\hat{y} - y^T\hat{y} + \frac{1}{2}y^T y
$$

Substitute $\hat{y} = X p$, using $\hat{y}^T = p^T X^T$:

$$
\min_{p}\; \frac{1}{2}\,p^T X^T X\, p - y^T X p + \frac{1}{2}y^T y
$$

## Differentiating with respect to a vector

Two rules from matrix/vector calculus are needed (the "Matrix Cookbook" has all
such formulas):

- **Linear term:** $\dfrac{\partial\,(a^T x)}{\partial x} = a$. Here the constant
  row is $y^T X$, so its derivative gives the vector $X^T y$ — the contribution
  (slope in each dimension of $x$) for each element.
- **Quadratic form:** $\dfrac{\partial\,(x^T A x)}{\partial x} = (A + A^T)\,x$, and
  if $A$ is **symmetric** ($A = A^T$) this is simply $2 A x$ — the analogue of the
  scalar $\dfrac{d}{dx}(x^2) = 2x$.

**Is $X^T X$ symmetric?** Direct proof using $(AB)^T = B^T A^T$:

$$
(X^T X)^T = X^T (X^T)^T = X^T X \qquad \text{q.e.d.}
$$

So it is symmetric, and we may use the simpler $2 A x$ rule.

Differentiate the objective with respect to $p$ and set to zero. The constant
$\tfrac{1}{2}y^T y$ vanishes:

$$
\frac{\partial}{\partial p} = 0 = X^T X\, p - X^T y
$$

## The normal equations and the pseudoinverse

This is the linear system $X^T X\, p = X^T y$ — the familiar $Ax = b$ form
(equivalently Newton's step for a multidimensional quadratic). Multiply by
$(X^T X)^{-1}$:

$$
p = (X^T X)^{-1} X^T y
$$

The optimal parameters are a **linear combination of the measurements** (and
contain arithmetic averages). Because $X$ ($N \times n_p$) is **not square** in
general (more experiments than parameters), we cannot invert it directly; forming
$X^T X$ makes a **square** ($n_p \times n_p$) invertible matrix. The whole
operation $(X^T X)^{-1} X^T$ is the **pseudoinverse** of $X$, denoted $X^{\dagger}$
(a dagger, "like a little sword"):

$$
X p = y \quad\Longrightarrow\quad p = X^{\dagger} y
$$

In MATLAB, solve it with the **backslash**: `p = X\y`. This is preferred over
explicitly forming `inv(X'*X)*X'*y` — MATLAB warns against `inv`/`^-1` because the
backslash analyses the structure of the matrix (whether it is square, which
decomposition to use) and is the **most efficient and numerically stable** way.
"Three hits of the keyboard, enter, and we have our parameters." This is why the
tedious derivation was worth it.

## The variance-covariance matrix

The matrix $X^T X$ is special and holds a lot of information — it is (up to
scaling) the **covariance matrix**. Recall $X$ is $N \times n_p$ (columns =
variables, rows = experiments). Its transpose $X^T$ is $n_p \times N$. Multiplying:

$$
X^T X =
\begin{pmatrix}
x_1^T x_1 & x_1^T x_2 & \cdots & x_1^T x_{n_p} \\
x_2^T x_1 & x_2^T x_2 & & \vdots \\
\vdots & & \ddots & \\
x_{n_p}^T x_1 & \cdots & & x_{n_p}^T x_{n_p}
\end{pmatrix}
$$

where $x_i$ is the vector of the $i$-th variable across all $N$ experiments. The
diagonal entries are sums of squares ($\sum_k x_{k,i}^2$); the off-diagonal entries
are cross terms ($\sum_k x_{k,i}\,x_{k,j}$) sharing the same experiment index. The
matrix is symmetric (proven above), so entries mirror across the diagonal.

Scale it (for **centered** data) to get the **variance-covariance matrix**:

$$
V_p = \frac{1}{N-1}\,X^T X
$$

$$
V =
\begin{pmatrix}
\sigma_{x_1}^2 & \sigma_{x_1 x_2} & \cdots & \sigma_{x_1 x_{n_p}} \\
\sigma_{x_1 x_2} & \sigma_{x_2}^2 & & \\
\vdots & & \ddots & \\
\sigma_{x_1 x_{n_p}} & & & \sigma_{x_{n_p}}^2
\end{pmatrix}
$$

- **Diagonal — variances** (Bessel correction, centered data):

$$
\sigma_{x_1}^2 = \frac{1}{N-1}\sum_{k=1}^{N} x_{k,1}^2
$$

  the square root being the standard deviation — so the diagonal recovers the
  variances of each variable.
- **Off-diagonal — covariances:**

$$
\sigma_{x_1 x_2} = \frac{1}{N-1}\sum_{k=1}^{N} x_{k,1}\,x_{k,2}
$$

  the **covariance** of variable 1 with variable 2, telling us about their
  relationship.

So even though $X^T X$ looks like it loses the information in $X$, it actually
**gains insight** into the data. (The slide shows a scatter of $x_1$ vs. $x_2$:
when the cloud tilts so positives pair with positives, $\sigma_{x_1 x_2} > 0$.)

## The correlation matrix

Covariances are not comparable across differently-scaled variables, so
**normalize** the covariance matrix into the **correlation matrix** $C$
(no heavy matrix calculus needed) — element by element:

$$
C_{ij} = \frac{V_{ij}}{\sigma_{x_i}\,\sigma_{x_j}}
$$

For example $C_{11} = \dfrac{\sigma_{x_1}^2}{\sigma_{x_1}\,\sigma_{x_1}} = 1$, so
the **diagonal is all ones** (same as normalizing the data to unit standard
deviation). The interesting part is **off-diagonal**: the $C_{ij}$ are the
**correlation coefficients**, guaranteed to lie between **−1 and 1**.

### Interpreting correlation coefficients

With, say, 10 variables, $C$ is a $10 \times 10$ matrix letting us compare
variables pairwise:

- $C_{ij} > 0$ — **positive correlation**: if one variable increases, the other
  increases (e.g. temperature ↑ → pressure ↑).
- $C_{ij} < 0$ — **negative correlation**: one increases while the other
  decreases.
- By absolute value (rough thresholds): $|C_{ij}| \ge 0.8$ → **strong**
  correlation; between $0.5$ and $0.8$ → **mild / suspected** correlation; below
  $0.5$ → not much can be claimed (depends on data quality). A small coefficient
  does not prove complete independence, but you cannot really claim the variables
  are correlated.

In a distillation-column example (from the exercises) one finds, e.g., the
pressures at the top and bottom of the column are positively correlated — which
intuition from separation processes confirms, but for unknown data it is much
harder to judge.

## Correlation is not causality

A cautionary example from a faculty report: a plot of the number of students from
the faculty **going abroad** vs. the number of **foreign students coming** to the
faculty over several academic years (only five numbers). The computed correlation
coefficient is about **0.7**, suggesting some correlation. But does it make sense
that fewer outgoing students *causes* more incoming students? There is no such
"magical power." Instead there is a **common factor** influencing both — the
**COVID pandemic**, which reduced both numbers. The closing lesson: **be careful
with correlations — not all of them mean causality**; a correlation need not
indicate that one variable actually influences another.
