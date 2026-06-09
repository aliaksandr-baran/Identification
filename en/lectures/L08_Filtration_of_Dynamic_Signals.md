---
lecture: L08
title: "Filtration of Dynamic Signals"
course: Identification
source: "https://www.youtube.com/watch?v=nAS4yAqv5ak"
---

# L08 — Filtration of Dynamic Signals

> Formulas verified against the lecturer's slide deck (*Notes_250416*): the σ-limit
> band, the covariance ellipse, the low-pass transfer function, and the
> moving-average / FIR filter and its gain.

## A bridge from static to dynamic

So far the course covered essentially **static** systems — measuring temperature,
pressure, etc., in (near) steady state, building static models, estimating a
constant. Identification is really about **dynamic systems**. Today's bridge
between static data analysis and dynamic systems is **filtration**.

A **low-pass filter** (Slovak: *dolnopriepustný filter*) "lets low through" — it
passes **low frequencies**. A signal can be decomposed into a **high-frequency**
component (the rapidly, almost periodically changing part — the noise) and a
**low-frequency** component (the trend in the data). Ideally:

- The **low-pass filter** returns the trend and leaves out the noise.
- The **high-pass filter** returns the noise — telling us (at first level) **how
  big the noise is**, or **when the signal changes**.

## Filtering in the static case — outliers

Plotting a collected time series (temperature, pressure) we may see a suspicious
value — an **outlier**. Options:

- **Remove** the affected subsection (e.g. the last 100 measurements). If we only
  want a steady-state model and other signals look normal in that window, we may
  remove that window across signals to keep them **aligned**.
- **Remove and replace.** Replace the outlier using the data — e.g. the average of
  the **last good value before** and the **first good value after** the outlier
  (interpolation), or an average of past values. Everything here is past data
  (processed a year later), so interpolation is legitimate; the replacement should
  stay in a reasonable range so as not to discard otherwise good data.

### Automatic outlier detection

Plotting is impractical for 10,000 signals, so detect automatically:

- **Rate of change of the signal** — flag a sudden change of gradient/derivative.
  **Beware the noise**, which raises the derivative; a well-tuned high-pass filter
  reports the noise but also flags an **abrupt** change (derivative higher than
  usual).
- **Out-of-limits signal** — flag values outside acceptable limits, obtained from:
  - **Physical limits** (e.g. the reactor temperature cannot be −200 K), or
  - **Statistical limits.** An outlier is something rare that does not conform to
    our assumptions about the signal. Compute the mean and standard deviation and
    use the band (slide):

$$
[\,\bar{y} - 3\sigma_y,\; \bar{y} + 3\sigma_y\,]
$$

  Good practice: after removing an outlier, **recompute** the mean and standard
  deviation; if they do not change much, the removed point was genuinely an outlier
  that did not corrupt the statistics (the outlier itself shifts the mean and σ if
  left in).

## The multi-dimensional case

One-dimensional analysis looks at one signal at a time, ignoring the others.
Consider temperature and pressure over time that **correlate**. A "bump" where both
rise together is **not** a sensor outlier — it is a normal but unusual operating
situation. In the **correlation plot** (T vs. P) it lies along the expected
correlation trend.

A **moving average** makes the limits **dynamic**: small when the signal is steady,
larger when the signal is changing. (Within a sliding window we assume far-past
transients are over and do not influence the present; the mean and σ are computed
from the window's recent values.) A point flagged as an outlier against rigid
historical limits may be fine against the moving band.

Using the **covariance matrix** (as for the regression parameters), a point's
normalized deviation follows a chi-square distribution, giving a **confidence
ellipse**. The test criterion (slide):

$$
(x - \bar{x})^T V^{-1} (x - \bar{x}) \le \chi^2_{N,\alpha},
  \qquad V = \frac{1}{N-1} X^T X
$$

Here $x$ is the vector of temperature and pressure for a data point. If the
inequality holds, the point lies **inside the ellipse** — consistent with the
historical data, even when temperature and pressure are both high together.
Contrast with **rigid box limits** on each variable separately: a point with **low
temperature but ordinary pressure** can be inside the box yet **off the expected
correlation trend** — caught by the ellipse but not by the box. This goes beyond
constant narrow limits, using past correlations, and is easy to apply and test.

## The real dynamic case

A "fairy tale": an innocent **original signal** (the real temperature inside a
reactor — what a *perfect* sensor would measure) is poisoned by a villain,
**measurement (sensor) noise**. The two combine into the **measured response** —
and we do not directly know either component. Even so, the signal is often still
visible to the eye in the measurement.

Passing a real signal through filters:

- The **high-pass filter** reconstructs an approximation of the noise (never
  perfect — the two pieces of information were combined), and still carries some
  information about **changes** of the original signal.
- The **low-pass filter** reconstructs an approximation of the trend — better than
  no filtering, but it lags where the original signal changes **fast** (the filter
  says "you cannot pass if you change that fast"), missing rapid features.

## Filters as transfer functions

Moving from means/averages to **discrete-time transfer functions**.

### The low-pass filter as a first-order system

Consider a raw input that steps from 0 to 1. The filter should **not** jump
immediately (a single sample might be just an impulse we do not want to follow) —
it should respond smoothly, like a **step response**. This is a first-order system
with **gain 1** (slide):

$$
G(s) = \frac{1}{T s + 1}
$$

The gain is 1 because in the long run, if the signal is constant, the filter must
return that same signal (0 → 0, sustained 1 → 1). There is **one parameter**, the
**time constant** $T$: changing it makes the filter arbitrarily slow or fast,
controlling how much of the high frequencies are cut off. Any dynamic system acts
as a filter (a two-tank level does not react immediately to an inlet change). With
**higher order** it is better to work in the **frequency domain** — that is how
audio filtering damps specific frequencies.

### Connection to statistics: the COVID example

The blue curve is the number of **daily PCR cases** with sampling time of **one
day**. It is very **spiky**: not because cases really swung from 7,000 to 2,000,
but because of **accumulation** — testing/reporting was low on weekends (Sunday
lowest) and piled up on **Monday** (the evenly-spaced big spikes). For decisions
(closing businesses, the "traffic-light" system) the **red curve** — a **7-day
moving average** (Slovak: *kĺzavý priemer*) — was used, not the raw blue numbers.

(Aside: average vs. median depends on the assumed noise distribution — the average
is optimal for **Gaussian** noise, the median for **Laplacian**; the median is also
preferred for skewed data like salaries, where many earn the minimum.)

## The moving-average filter

For an $m$-day moving average, the output $y_k$ at the current time $k$ averages
$m$ values. Including the current value (slide):

$$
y_k = \frac{1}{m}\sum_{i=0}^{m-1} u_{k-i}
$$

Excluding the current value gives a **prediction** (using only past values, before
today's number is known):

$$
y_k = \frac{1}{m}\sum_{i=1}^{m} u_{k-i}
$$

(Care with the index count: summing $m+1$ values but dividing by $m$ would not be
an average; hence the limits above.)

Generalize the equal weights $\tfrac{1}{m}$ to arbitrary weights $b_i$:

$$
y_k = \sum_{i=1}^{m} \frac{1}{m}\, u_{k-i}
  \qquad\longrightarrow\qquad
  y_k = \sum_{i=1}^{m} b_i\, u_{k-i}
$$

- **Moving-average filter:** all weights equal, $b_1 = b_2 = \dots = b_m$, with
  $\sum_{i=1}^{m} b_i = 1$. (For $m = 3$: $b_1 + b_2 + b_3 = 1$ with all equal
  forces $b_i = \tfrac{1}{3}$ — i.e. $\tfrac{1}{m}$.)
- **Weighted moving-average filter:** keep $\sum_{i=1}^{m} b_i = 1$ but allow
  unequal weights with $b_i \ge 0$ for all $i$. Example ($m = 3$): $b_1 =
  \tfrac{1}{4}$, $b_2 = \tfrac{1}{2}$, $b_3 = \tfrac{1}{4}$ — weight the middle (or
  most accurate) day more.

## Finite Impulse Response (FIR)

The model

$$
y_k = \sum_{i=1}^{m} b_i\, u_{k-i}
$$

is called a **Finite Impulse Response (FIR)** filter.

### Its transfer function

Using the backward-shift operator $z^{-i}$ (so $u_{k-i} \leftrightarrow z^{-i}$;
note $u_k$ corresponds to $z^0 = 1$, not shifted):

$$
Y(z^{-1})\,z^{0} = \left(\sum_{i=1}^{m} b_i\, z^{-i}\right) U(z^{-1})
$$

Dividing the left and right sides by $z^0$ gives the transfer function (numerator
the weighted shifts, denominator 1):

$$
G(z^{-1}) = \frac{Y(z^{-1})}{U(z^{-1})} = \frac{\sum_{i=1}^{m} b_i\, z^{-i}}{z^{0}}
  = \sum_{i=1}^{m} b_i\, z^{-i}
$$

### Gain

The gain is found by substituting $z = 1$ (the discrete-time equivalent of $s = 0$
in continuous time, via $z = e^{T s}$):

$$
\text{gain} = \sum_{i=1}^{m} b_i
$$

Because the moving-average and weighted-moving-average filters impose
$\sum b_i = 1$, their **gain is 1** — exactly the gain of a good low-pass filter.

**Teaser for next time:** we will break the rule $\sum b_i = 1$, so the filter can
represent **any gain**, and also represent **any time constant** and **any order**
of system.
