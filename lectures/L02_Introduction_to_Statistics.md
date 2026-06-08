---
lecture: L02
title: "Introduction to Statistics"
course: Identification
source: "https://www.youtube.com/watch?v=laEQig6EanE"
---

# L02 — Introduction to Statistics

> Formulas and the Slovak terminology below are typeset as stated in the
> lecture; where the caption garbled them they were reconstructed from the
> lecturer's own slide deck (*Ident 24 02 2026*), noted inline.

## Why statistics — modelling noisy data

Last time we saw that our world is rich with data, but **this data is not always
reliable** — there is always some noise in the measurements (seen in many lab
exercises). Sometimes it is a **systematic error** (e.g. somebody did not
calibrate a device); there is also the standard error that comes from many small
errors accumulating into measurement noise. Despite these problems we should be
able to make sense of the data — to find a **model**, some function or algorithm
that makes sense of the data.

This is what **data-based modelling** is about, and **system identification** is
part of it (hence the course title). System identification specifically concerns
**dynamic systems**; we will not start with dynamic systems right away but move
into them slowly.

Recap of model types (from the "modeling in process industry" class): the
**first-principles models** come from the principles of physics. In this course
we live in the world of **data-based models** — static and dynamic, linear and
nonlinear — and a little about **state estimation** (a technique that processes
the data and removes some noise).

Today's question: **how can we model the noise / uncertainty in the data**, and
make sense of the data even before building a model? One way is to understand
**probability** and do some **statistics**. (The lecturer notes these slides were
originally made for the European Researchers' Night to show school kids how
probability works.)

The lecturer also mentions a talk by a Slovak scientist
<!-- unclear: name in caption "mikal vco"; described as a co-founder of Google DeepMind -->
about **large language models (LLMs)**, making the point that **LLMs are just
applied statistics** — trained with mean values, standard deviations and
probability. A side remark: if we could train such a model multiple times, we
could even get a **confidence** in its answers; today there is no one telling you
that a ChatGPT output is, say, 80% vs 20% likely to be correct.

## Probability and the dice experiment

**Probability** (known from high school) expresses that an event can happen with
a certain likelihood, in mathematical terms from **0 to 1**. A good testing
device is a **dice**.

Building on the histogram idea from last week, the lecturer builds a histogram of
dice outcomes (1–6):

- A few **physical** rolls in class do **not** look uniform (e.g. several twos, a
  couple of ones). The reason is that **the number of experiments is not
  sufficient** — this points toward the **law of large numbers**.
- In **MATLAB**, simulating a *fair* dice:
  - **20** attempts: still very uneven (six may appear in almost half the cases).
  - **100** attempts: a different picture, no single number dominant.
  - **1,000 / 10,000 / 100,000 / 1,000,000 / 6,000,000** attempts: the columns
    progressively even out. At **6 million** rolls each number appears about
    **1 million** times — every outcome is equally likely.

We then **normalize** the histogram — we do not care about absolute counts, only
about the **proportions / ratios**. The probability of an event (e.g. throwing a
three) is the **number of successful occurrences divided by the number of
attempts**. The lecturer notes that if the dice were **unfair**, some numbers
would occur more frequently, but you cannot tell that from a small number of
experiments.

## Sum of several dice → the bell curve

A standard detour: throw **two dice at the same time** and look not at the
individual numbers but at their **sum**.

- One dice gives 6 outcomes; two dice give **36 possible outcomes** for the pair.
- The sums are **not** uniform: e.g. a sum of **3** occurs only twice, but a sum
  of **7** dominates because it can be made as 6+1, 5+2, 4+3, … So the model of
  this game is no longer uniform — **7** is the most likely sum.

Continuing the game with **three dice**: lowest sum is 1+1+1 = **3**, highest is
6+6+6 = **18**; sums of 10 and 11 become most likely. With **four, five, six, …,
up to ~20 dice**, a clear **shape appears**. With ~20 dice, the most probable sum
is around **70** (ten times the two-dice peak of 7).

This shape is the **bell curve** — the **Gaussian curve**, with a known equation.
The Germans even put it on their currency: **Carl Friedrich Gauss** and the bell
curve appeared on the **10 Deutsche Mark** note.

## The probability density function (PDF)

The bell curve is a **probability density function**, abbreviated **PDF** (not
"portable document format"). A PDF exists for any distribution — even the
**uniform distribution** (the dice), which is not the "e-to-the-power" function.

The PDF tells us the **likeliness of an event occurring**. For a dice (6 discrete
outcomes) this is easy to interpret, but for a continuous quantity like the
**temperature in the room** the idea of "probability of measuring exactly
25.7284…°" becomes distorted — there will be a way to handle that (the CDF).

### Normal / Gaussian distribution

"Normal" and "Gaussian" are synonyms (Germans tend to say *Gaussian*; others say
*normal*). We say a random variable $X$ (capital $X$; Slovak *premenná*) **obeys**
a normal distribution, written — note the whole world, even the Germans, write a
capital **N**, not G:

$$X \sim N(\mu, \sigma^2)$$

with two parameters $\mu$ and $\sigma$ (slide: written with $\bar{x}$;
$X \sim N(\bar{x}, \sigma^2)$ with parameters $\bar{x}$ and $\sigma^2$).

The parameters and their Slovak names (confirmed from the slide):

- $\mu$ (also written $\bar{x}$) — the **mean** / **mean value** / **expected
  value**. The lecturer likes the English "expected value," even written as an
  operator $\mu = E[X]$. Slovak: **stredná hodnota**. If the data are
  normally distributed, the expected value is the number you expect from the next
  trial (next dice throw, temperature, exam result). For the two-dice game the
  mean is **7**.
- $\sigma$ — the **standard deviation**. Slovak: **smerodajná odchýlka**.
- $\sigma^2$ — the **variance** (a very helpful concept). Slovak: **rozptyl**.

The PDF of the normal distribution (the function from the German banknote;
confirmed from the slide):

$$f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

This PDF, $f(x)$, tells us **how proportionally likely** the outcome $x$ is.

### Building the curve from simpler functions

To understand this scary-looking function, the lecturer looks at the simpler case
$\mu = 0$ and $\sigma = 1$ — the **standard normal / standard Gaussian
distribution**. Then:

$$f(x) = \frac{1}{\sqrt{2\pi}}\, e^{-\frac{1}{2}x^2}$$

He sketches it in three steps (the slide shows the same three-panel build-up):

1. Plot $x^2$ — a parabola with its minimum (value 0) at $x = 0$ (the mean).
2. Negate it: $-x^2$ — now **concave**, with a **maximum** at $x = 0$.
3. Apply the **exponential** $e^{(\cdot)}$. Since $-x^2$ takes only **negative
   values**, we stay on the part of the exponential between **1** (at the maximum,
   $e^0 = 1$) and **0** (the values tend to zero, i.e. an **infimum** at the
   tails, never actually reached). The maximum stays at $x = 0$ because the
   exponential is an increasing function. The factor $\tfrac{1}{2}$ only controls
   how fast it decays. The result is the **Gaussian curve**.

## Why the constant $\tfrac{1}{\sqrt{2\pi}}$ — integrating to 1

A PDF is **not the probability itself yet**. For the dice we can ask, e.g., "how
likely is an **even** number?" — sum the individual probabilities:
$\tfrac{1}{6} + \tfrac{1}{6} + \tfrac{1}{6} = \tfrac{1}{2}$ (an **OR** of events
→ a sum of probabilities; this is a **joint** vs. simple-sum distinction the
lecturer flags). Summing over **all** dice outcomes,
$6 \times \tfrac{1}{6} = 1$.

For a continuous PDF the analogue of "going through all possibilities and
summing" is **integration**. So a valid PDF must integrate to one. Testing the
standard-normal exponential alone in MATLAB:

$$\int_{-\infty}^{\infty} e^{-\frac{1}{2}x^2}\, dx = \sqrt{2\pi} \approx 2.5066$$

That is exactly why the normalizing constant $\tfrac{1}{\sqrt{2\pi}}$ (more
generally $\tfrac{1}{\sigma\sqrt{2\pi}}$) is there — so the **total probability is
1**. The slide states the general properties:

$$f(x) \ge 0, \qquad F(\infty) = \int_{-\infty}^{\infty} f(x)\, dx = 1$$

The interpretation: *some* event must happen — the temperature in the room is
either $-\infty$, some finite number, or $+\infty$ — so the total probability is 1.

## The cumulative distribution function (CDF)

To get a **probability** (not just a density) we use the **cumulative
distribution function**, **CDF**. Slovak: **distribučná funkcia**.

Notation contrast: the PDF written $f(x)$ (lowercase $f$) gives the density /
relative probability; the CDF written $F$ (capital) gives the **probability
itself**. The CDF is defined as the probability that $X$ is less than or equal to
some value $z$ (a particular value of $x$):

$$F(z) = \Pr(X \le z) = \int_{-\infty}^{z} f(x)\, dx$$

We must start the integral at one end, so we begin at $-\infty$. This computes the
**area under the PDF curve** up to $z$ — the same principle as summing
$\tfrac{1}{6}+\tfrac{1}{6}+\tfrac{1}{6}$ on the dice to get $P(X \le 3) =
\tfrac{1}{2}$, but now in the **continuous** world (thermometer, battery charge,
etc.).

Sketching the CDF point by point (slide shows the integral form):

- It is **0** at one end and **asymptotically 1** at the other (after integrating
  the whole curve, $P(X \le 10{,}000°) \approx 1$). It never goes negative because
  the PDF is always positive (no cancelling of areas).
- It is the **integral** of the PDF, so the PDF is its **derivative**: small
  slopes at the tails, **maximum slope (inflection point)** at the mean.
- For a chosen $z_1$ (e.g. 10°), $F(z_1)$ reads off, say, **0.2 (20%)** — the
  probability the temperature is $z_1$ or less. Taking $z_2 = \mu$ (the mean)
  gives about **0.5**; a higher $z_3$ gives more.

### From CDF to interval probabilities

What we usually want is the probability that $X$ falls in an **interval**, which
is the difference of two CDF values, equivalently a definite integral (slide):

$$P(a \le x \le b) = \int_{a}^{b} f(x)\, dx$$

To do this in practice you **collect data**, estimate the two parameters (mean and
variance/standard deviation) of the curve, and then ask such questions. Example
discussed: measuring everyone's **height** in the room. As with the dice we do not
get a uniform distribution — we **fit a normal distribution** to the data, get the
mean and standard deviation, and then ask questions like "who is between 174 and
178 cm?". Note the probability of **exactly** one point (e.g. exactly 25°) is
**zero**, because the integral over a single point is zero — so we always ask
about a small interval (e.g. $25 \pm 0.1$).

A unit remark: in $\frac{(x-\mu)^2}{2\sigma^2}$, $x$ and $\sigma$ must "live in the
same world" — if $x$ is temperature in Kelvin, the numerator is Kelvin² and the
denominator (via $\sigma$) is also Kelvin², so the exponent is **dimensionless**.
This lets us **standardize**: subtract the mean and measure distance in multiples
of $\sigma$.

## The 68–95–99.7 rule (sigma intervals)

Measuring distance from the mean in **standard deviations** gives the famous
interval probabilities (computed in MATLAB by integrating the standard-normal PDF
between the limits; confirmed on the slide):

$$P(\mu - \sigma \le x \le \mu + \sigma) = 68.27\%$$
$$P(\mu - 2\sigma \le x \le \mu + 2\sigma) = 95.45\%$$
$$P(\mu - 3\sigma \le x \le \mu + 3\sigma) = 99.73\%$$

So $\pm 1\sigma \approx 68\%$, $\pm 2\sigma \approx 95\%$, $\pm 3\sigma \approx
99.7\%$. The lecturer notes this is **general** — once you know the mean and
(most importantly) the standard deviation, it holds for any normal distribution.
For control design you might not care about the 5% of cases outside $\pm 2\sigma$.
He also mentions that at **CERN** a "discovery" (e.g. Higgs boson, or the
faster-than-light-neutrino claim) is declared at about **6 standard deviations**.

## Estimating the parameters from data

Finally, how to compute the parameters from $n$ samples $x_1, x_2, \dots, x_n$.
The hat denotes a **sampled** estimate (based on observations, not the exact
value):

**Sample mean** — the arithmetic average (sum the values, divide by the number of
trials), same idea as the $\tfrac{1}{6}$ dice probability:

$$\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i$$

**Variance / standard deviation** — described verbally as **the average of how
much the samples differ from the mean**, and because that difference can be
positive or negative, the **square** is used (the lecturer does not write the
explicit denominator; the slide leaves it as "$\sigma^2 = \dots$"):

<!-- unclear: lecturer states "average of the squared differences from the mean" but does not specify the denominator (n vs n-1) -->
$$\sigma^2 \approx \frac{1}{n}\sum_{i=1}^{n} (x_i - \bar{x})^2$$

The standard deviation is then the average distance of the data (heights,
temperatures, …) from their mean value.

He closes the LLM analogy: ChatGPT's answer is like **one sample** drawn from some
population (answers found online, some checked by experts) — but you cannot easily
get its variance, because each "sample" is one training of ~40 billion parameters
costing millions of dollars, so nobody pays for the multiple trainings needed.
