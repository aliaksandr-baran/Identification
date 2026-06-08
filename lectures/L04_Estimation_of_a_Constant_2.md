---
lecture: L04
title: "Estimation of a Constant #2"
course: Identification
source: "https://www.youtube.com/watch?v=PXgpgTrh07Y"
---

# L04 — Estimation of a Constant #2

## Recap of the setup

We continue the statistical approach to estimating a constant. We have measured
data assumed to come from a **normal distribution** with some constant mean and
some standard deviation, whose values we do not know. From this we recall the
**PDF** — how likely it is to observe $y_k$ if we knew the mean and standard
deviation — and its sister function, the **likelihood function** $L$, which swaps
the roles: with $y_k$ given (e.g. we measured 1.6 or 1.1), the mean and standard
deviation become the parameters, and we ask how likely those parameter values are.

Because all data $y_k$ come from the same process (the same two parameters), the
**joint probability** is the **product** of the likelihoods.

## Maximizing the likelihood — the log trick

We maximize the joint likelihood over $\bar{y}$ and $\sigma$:

$$\max_{\bar{y},\,\sigma}\;\prod_{k=1}^{N}
  \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(y_k-\bar{y})^2}{2\sigma^2}}$$

Differentiating a **product** (product rule, with $N-1$ undifferentiated terms) is
unpleasant. The trick: take the **logarithm**, which turns a product into a sum,
because $\ln(a\cdot b) = \ln a + \ln b$. The natural logarithm is convenient since
$\ln(e^x) = x$, so the exponential disappears. Applying $\ln$ turns the product
$\prod$ into a sum $\sum$:

$$\max_{\bar{y},\,\sigma}\;\sum_{k=1}^{N}
  \left[\ln\!\frac{1}{\sigma\sqrt{2\pi}}
        - \frac{(y_k-\bar{y})^2}{2\sigma^2}\right]$$

**Does the log change the location of the optimum?** No — applying a **monotonic
(increasing)** function preserves which value is larger, so the extrema stay at the
same place (the curve looks different but the argmax/argmin is unchanged). If the
transforming function were decreasing we would need a minus sign. The original
objective need not be monotonic; only the transforming function must be.

**Convert max to min** (as in the optimization class) by negating the objective —
this has nothing to do with monotonicity. Rewriting $\frac{1}{\sigma\sqrt{2\pi}}
= (\sigma\sqrt{2\pi})^{-1}$, the inner $\ln$ contributes $-\ln(\sigma\sqrt{2\pi})$,
and after the overall minus we get $+\ln(\sigma\sqrt{2\pi})$:

$$\min_{\bar{y},\,\sigma}\;\sum_{k=1}^{N}
  \left[\ln\!\big(\sigma\sqrt{2\pi}\big)
        + \frac{(y_k-\bar{y})^2}{2\sigma^2}\right]$$

This already contains the familiar **sum of squares** $\sum (y_k - \bar{y})^2$
from the optimization-based (least-squares) approach.

## Estimating the mean

Call the objective $F$. Take $\dfrac{\partial F}{\partial \bar{y}} = 0$. The first
term does not involve $\bar{y}$, so (same as last lecture, with constant
$\tfrac{1}{2\sigma^2}$ that cancels against the zero right-hand side):

$$0 = \sum_{k=1}^{N} (y_k - \bar{y})
  \quad\Longrightarrow\quad
  \hat{y} = \frac{1}{N}\sum_{k=1}^{N} y_k$$

So the **arithmetic mean is also the maximum-likelihood (statistically most
probable) estimate**, not just the least-squares optimum — which is why the
function $L$ is called the *likelihood* function.

## Estimating the standard deviation

Now take $\dfrac{\partial F}{\partial \sigma} = 0$. Split the log of the product
$\ln(\sigma\sqrt{2\pi}) = \ln\sqrt{2\pi} + \ln\sigma$, so

$$F = \sum_{k=1}^{N}\Big[\ln\sqrt{2\pi} + \ln\sigma
      + \tfrac{1}{2}(y_k-\bar{y})^2\,\sigma^{-2}\Big]$$

The derivative of a sum is the sum of derivatives: the constant $\ln\sqrt{2\pi}$
gives 0, $\ln\sigma$ gives $\tfrac{1}{\sigma}$, and the last term gives
$-\dfrac{(y_k-\bar{y})^2}{\sigma^3}$:

$$\frac{\partial F}{\partial \sigma}
  = \sum_{k=1}^{N}\left[\frac{1}{\sigma}
      - \frac{(y_k-\bar{y})^2}{\sigma^{3}}\right] = 0$$

Multiply through by $\sigma^3$. The term $\sum_{k=1}^{N}\sigma^2 = N\sigma^2$
(summing a $k$-independent term $N$ times), while the sum of squares must stay
inside the sum (it depends on $k$):

$$N\sigma^2 = \sum_{k=1}^{N}(y_k-\bar{y})^2
  \quad\Longrightarrow\quad
  \sigma^2 = \frac{1}{N}\sum_{k=1}^{N}(y_k-\bar{y})^2$$

equivalently $\sigma = \sqrt{\dfrac{1}{N}\sum_{k=1}^{N}(y_k-\bar{y})^2}$ (Slovak:
*rozptyl* = variance). This is essentially the **recycled definition of the
variance** (the average distance of the data from the mean), which gives the
Gaussian bell its width.

### Bessel's correction

This estimate of $\sigma^2$ is **not quite good**: we already "spent" one **degree
of freedom** by estimating the mean from the same data (using the arithmetic
average). So out of $N$ data points, one is already gone, and the proper estimate
divides by $N-1$:

$$\sigma^2 = \frac{1}{N-1}\sum_{k=1}^{N}(y_k-\bar{y})^2$$

Dividing by $N-1$ instead of $N$ makes the number slightly **bigger**, so as not
to **underestimate** the noise (the "standardized error" you may recall from high
school). This is called **Bessel's correction**.

## Statistics of the estimation error — unbiasedness

Now we ask the question optimization cannot answer: from one set of measurements,
**how far off is the estimate?** Define the **estimation error** as the difference
between the true constant $\bar{y}$ and the estimate $\hat{y}$. This error $e$ also
has a **normal distribution**; we seek its **mean** and **standard deviation**.

The **expected-value operator** $E[\cdot]$ just returns the mean and is **linear**,
so it splits over sums and pulls out constants. The true mean of a constant is the
constant itself, $E[\bar{y}] = \bar{y}$, and each measurement has $E[y_k] =
\bar{y}$:

$$E[e] = E[\bar{y} - \hat{y}]
  = \bar{y} - \frac{1}{N}\sum_{k=1}^{N} E[y_k]
  = \bar{y} - \frac{1}{N}\,N\,\bar{y} = 0$$

So as the number of measurements increases, the **estimation error converges to
zero** and the estimate converges to the true value. This property is named: the
arithmetic mean is an **unbiased estimate**
<!-- unclear: lecturer says "in Slovak it's called very nice wording" but the Slovak term is not captured -->.
The **geometric mean**, by contrast, is a **biased** estimate (it has a certain
offset).

## Variance of the estimation error — consistency

Next, the **variance of the estimation error**:

$$\operatorname{var}(e) = E\!\left[(\bar{y} - \hat{y})^2\right]
  = E\!\left[\Big(\bar{y} - \tfrac{1}{N}\textstyle\sum_{k=1}^{N} y_k\Big)^2\right]$$

Factor $\tfrac{1}{N}$ out of the square: using $\bar{y} = \tfrac{N}{N}\bar{y}$,
write $\bar{y} - \tfrac{1}{N}\sum y_k = \tfrac{1}{N}\sum_{k=1}^{N}(\bar{y}-y_k)$,
so the square gives $\tfrac{1}{N^2}\big(\sum_{k=1}^{N}(\bar{y}-y_k)\big)^2$.

The obstacle: this is the **square of a sum**, not the sum of squares — and in
general $(a+b)^2 \ne a^2 + b^2$ because of the **cross terms** (e.g. $y_1 y_2$).
But here we take the **expectation** (average), and we invoke an **independence
assumption** (★): the expected product of any two distinct measurements is zero,

$$E[y_i\,y_j] = 0 \quad (i \ne j),$$

which holds when the **samples / noise are independent** — the noise now does not
influence the noise later (and vice versa), a reasonable assumption (to be
justified in a later lecture). With independence, the cross terms vanish, so the
square of the sum equals the sum of the squares inside the expectation:

$$\operatorname{var}(e)
  = \frac{1}{N^2}\sum_{k=1}^{N} E\!\left[(\bar{y}-y_k)^2\right]
  = \frac{1}{N^2}\,N\,\sigma^2
  = \frac{\sigma^2}{N}$$

because $\sum_{k=1}^{N} E[(\bar{y}-y_k)^2] = \sum \sigma^2 = N\sigma^2$ (the
variance of the measurement noise). So:

$$\sigma_e^2 = \frac{\sigma^2}{N}, \qquad \sigma_e = \frac{\sigma}{\sqrt{N}}$$

**Interpretation — consistency.** $\sigma$ is how noisy the sensor is; $\sigma_e$
is how far off the estimate of the constant is. The **more samples we take, the
smaller the error** — this is not automatic, it is a **property of the arithmetic
mean**, and the estimator is then called **consistent** (with 100 measurements the
error is smaller than with 10). This is the smooth shrinking of the arithmetic
mean's oscillations seen last time, unlike the median's sudden jumps.

**Practical rule.** Since $\sigma_e = \sigma/\sqrt{N}$, the error in physical units
improves with the **square root** of the number of measurements. Example: a sensor
with standard deviation $\sigma = 1$, wanting an estimate precision of $0.1$ —
improving by a factor of **10** requires at least $10^2 = $ **100 measurements**.

## Distribution of the error and the chi-square distribution

We have now characterized the estimation error: $e \sim N(0, \sigma_e^2)$. Taking
more measurements keeps the mean at zero but **narrows** the Gaussian bell (more
certainty about the estimated mean).

One more distribution: if a variable $X$ is normally distributed (say zero mean),
what is the distribution of $X^2$? Negative values play no role (a square cannot be
negative), so the distribution is one-sided. This is the **chi-square**
distribution (Slovak: *chí kvadrát*). It has a parameter: summing $n$ squared
normal variables,

$$\sum_{i=1}^{n} X_i^2 \sim \chi^2 \text{ with } n \text{ degrees of freedom},$$

where $n$ counts how many normal variables were squared and summed. This will be
useful later when estimating several parameters (not just one constant).

## Confidence interval for the constant

Normalize the error so it has zero mean and unit standard deviation, then square
it — a single squared normal value has a chi-square distribution with **1** degree
of freedom:

$$\left(\frac{\bar{y} - \hat{y}}{\sigma_e}\right)^2 \sim \chi^2_{1}$$

Using the **cumulative distribution function** of the chi-square distribution we
can build a **confidence interval**, exactly as in the statistics introduction.
For an $\alpha$ confidence level, let the **quantile** (inverse CDF) be denoted
$\chi^2_{\alpha}$ (a number obtained from one MATLAB command). Then

$$\left(\frac{\bar{y} - \hat{y}}{\sigma_e}\right)^2 \le \chi^2_{\alpha}$$

Taking the square root of the inequality (as $x^2 \le 4 \Rightarrow |x| \le 2$):

$$-\sqrt{\chi^2_{\alpha}} \;\le\; \frac{\bar{y} - \hat{y}}{\sigma_e}
  \;\le\; \sqrt{\chi^2_{\alpha}}$$

and rearranging gives the interval for the true constant $\bar{y}$:

$$\hat{y} - \sigma_e\sqrt{\chi^2_{\alpha}} \;\le\; \bar{y}
  \;\le\; \hat{y} + \sigma_e\sqrt{\chi^2_{\alpha}}$$

Every quantity on the left and right is computable **from data**: $\hat{y}$ is the
arithmetic average, $\sigma_e$ is the estimated standard deviation of the error
(the one with $\sqrt{N}$), and $\chi^2_{\alpha}$ is a statistical-function value
from MATLAB. So we can easily find how far the estimate is from reality (e.g. the
true value lies between $-0.01$ and $+0.01$ around the estimate), and **taking more
measurements makes this interval smaller and smaller**.
