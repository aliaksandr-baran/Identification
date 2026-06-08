---
lecture: L09
title: "Identification of Dynamic Systems"
course: Identification
source: "https://www.youtube.com/watch?v=WEGsY_W654g"
---

# L09 — Identification of Dynamic Systems

> Formulas verified against the titled slide deck (*Identification L09 —
> Identification of dyn systems*): the impulse response, convolution integral, the
> FIR matrix, and the ARX transfer function / time-domain form.

## Recap and goal

Last lecture's filters are themselves **dynamic systems** — a filter and a transfer
function are two sides of the same coin. The **low-pass filter** wanted gain 1 (to
represent long-term trends) and a chosen time constant (to filter noise), and was
realized as a **finite impulse response (FIR)** model, established from the
(weighted) moving average. FIR is one of the first models to try when identifying
dynamic systems (low-pass gain ≈ 1, high-pass gain ≈ 0).

A typical identification task: apply a **step** to the input at some time and
measure the plant's response $y_{\text{measured}}$, then find a model representing
the plant. Textbook step-response methods (e.g. Strejc's method) assume you always
get a clean single-step response — which is not always the case. We need to
**generalize**.

## Demystifying FIR: the impulse response

Represent a dynamic system as an input–output box. It is better to work in the
**Laplace domain**, where (for linear dynamics representable by a transfer
function):

$$Y(s) = G(s)\,U(s)$$

What is $G(s)$ in the **time domain**, i.e. $g(t)$? Take the simplest example
(slide):

$$G(s) = \frac{1}{s + \frac{1}{T}} \quad\xrightarrow{\;\mathcal{L}^{-1}\;}\quad
  g(t) = e^{-t/T}$$

(using $\dfrac{1}{s+a} \to e^{-at}$). This $g(t)$ starts at a constant at $t = 0$
and decays to zero as $t \to \infty$ (for $T > 0$).

What does $G(s)$ **alone** represent? With a **unit step** input $u(t) = 1(t)$ we
get a **step response**. But with an idealized **impulse** $u(t) = \delta(t)$ —
whose Laplace image is $U(s) = 1$ — the output is $Y(s) = G(s)$. So $g(t)$ is the
**impulse response** (hence the "impulse response" in FIR). Intuitively: a tank fed
at a constant flow rate, briefly disturbed by a sudden valve twist and returned —
a first-order system responds immediately to the impulse, and the effect slowly
disappears over time.

## The convolution integral

To compute the time-domain output we use the **convolution** (the innocent-looking
"$*$"):

$$y(t) = g(t) * u(t)
  = \int_0^t g(\tau)\,u(t-\tau)\,d\tau
  = \int_0^t g(t-\tau)\,u(\tau)\,d\tau$$

(two equivalent forms). An integral is an infinitesimal **sum over past time**. A
dynamic system keeps **memory** of past inputs: the output at the current time
$t_k$ reacts strongly to recent inputs ($t_{k-1}, t_{k-2}, \dots$) but barely to
inputs long ago (the flow rate a year ago does not matter now). The function $g$
acts as a **weight** that, flipped in time (the minus sign in $g(t-\tau)$), weights
recent inputs much more than distant ones — "the weather yesterday influences
today's weather much more than the weather a year ago." Convolution has many
applications (convolutional neural networks, image processing, control/modelling).

### FIR as a discretized convolution

The FIR model is the discrete counterpart, where the integral becomes a finite sum
and the coefficients $b_i$ are **samples of $g$** at discrete points:

$$y_k = \sum_{i=1}^{m} b_i\, u_{k-i}$$

The output at time $k$ is the accumulated influence of the past inputs.

## Training the FIR model on a step response

Assume a **step response** with a step at time 0 (no assumption that the gain is
1). Write the prediction equations. Before the step all inputs are zero, so:

$$y_0 = 0 = b_1\cdot 0 + b_2\cdot 0 + \dots + b_m\cdot 0$$
$$y_1 = b_1 u_0 + b_2 u_{-1} + \dots + b_m u_{1-m} \quad(\text{past terms } = 0)$$
$$y_2 = b_1 u_1 + b_2 u_0 + \dots + b_m u_{2-m}$$
$$\vdots$$
$$y_m = b_1 u_{m-1} + b_2 u_{m-2} + \dots + b_m u_0$$
$$\vdots$$
$$y_N = b_1 u_{N-1} + b_2 u_{N-2} + \dots + b_m u_{N-m}$$

Since these are **linear in the parameters** $b_i$ (the $y$'s and $u$'s are known
data), we build a matrix equation exactly as in linear regression, $y = X p$ with
$p = (b_1, \dots, b_m)^T$:

$$\begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_m \\ \vdots \\ y_N \end{pmatrix}
=
\begin{pmatrix}
u_0 & 0 & 0 & \cdots & 0 \\
u_1 & u_0 & 0 & \cdots & 0 \\
\vdots & & & & \\
u_{m-1} & u_{m-2} & \cdots & & u_0 \\
\vdots & & & & \\
u_{N-1} & u_{N-2} & \cdots & & u_{N-m}
\end{pmatrix}
\begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{pmatrix}$$

Build each row by taking the input "strip" $\dots, 0, 0, u_0, u_1, u_2, \dots$,
flipping it, and pasting it at the right place. The matrix first becomes **square**
at row $m$ (it always has $m$ columns), which matters because we want an inverse
(or pseudoinverse). Here:

- $m$ = **order of the model** (number of parameters to identify);
- $N$ = number of data points, with $N \ge m$ (more, ideally much more, if the
  noise is high).

As a byproduct, starting the matrix from a later row (dropping the leading-zero
rows) works for a **general** input signal, not just a step — a steady state in the
past is a good but not always necessary assumption.

## The ARX model

To reach the model types familiar from automatic control, recall the FIR transfer
function was just a **numerator** with $1$ in the denominator. Extend the
denominator (slide) — the **AutoRegressive model with eXogenous input (ARX)**:

$$G(z^{-1}) = \frac{\sum_{i=1}^{m} b_i\, z^{-i}}{1 + \sum_{i=1}^{n} a_i\, z^{-i}}\;
  z^{-n_k}$$

The optional $z^{-n_k}$ term represents an **input (time) delay** of $n_k$ steps —
the same idea as the unit-delay block $z^{-1}$ in Simulink, which makes the current
output become the input at the next step, $y(t) \to y(t+1)$. We set the delay aside
in the discussion. (The sum limits $n, m, n_k$ follow MATLAB's notation.)

### Time-domain form via the backward shift

Clearing the fraction:

$$Y(z^{-1})\Big(1 + \sum_{i=1}^{n} a_i z^{-i}\Big)
  = U(z^{-1})\sum_{i=1}^{m} b_i z^{-i}$$

The backward shift $z^{-i} \leftrightarrow y_{k-i}$ (and $z^0 = 1$ is no shift,
$y_k$) gives directly:

$$y_k = -\sum_{i=1}^{n} a_i\, y_{k-i} + \sum_{i=1}^{m} b_i\, u_{k-i}$$

This is an **$m/n$-order ARX model**.

### Why "autoregressive with exogenous input"

- The **denominator / $a_i$** part makes the current output depend on its **own
  past outputs** $y_{k-i}$ — the model **regresses on itself**, hence
  *autoregressive (AR)*.
- The **numerator / $b_i$** part is what we earlier called the FIR model, but here
  it is the **exogenous input** (an external influence; "exogenous" not "external"
  for historical reasons).
- Without the input part, $y_k = -\sum a_i y_{k-i}$ is just an **AR model**. The
  ARX form can represent all the usual transfer functions (poles, zeros).

## Training the ARX model on a step response

As with FIR, assume step-response data with steady state (all zero) before the
step. Break the sums into components. The prediction equations:

$$y_1 = -a_1 y_0 - a_2 y_{-1} - \dots - a_n y_{1-n}
        + b_1 u_0 + b_2 u_{-1} + \dots + b_m u_{1-m}$$
$$y_2 = -a_1 y_1 - a_2 y_0 - \dots - a_n y_{2-n}
        + b_1 u_1 + b_2 u_0 + \dots + b_m u_{2-m}$$
$$\vdots$$
$$y_m = -a_1 y_{m-1} - a_2 y_{m-2} - \dots - a_n y_{m-n}
        + b_1 u_{m-1} + b_2 u_{m-2} + \dots + b_m u_0$$
$$\vdots$$
$$y_N = -a_1 y_{N-1} - a_2 y_{N-2} - \dots
        + \dots + b_m u_{N-m}$$

(all terms with negative-or-zero "past" indices are zero by the steady-state
assumption).

### Why $n \ge m$

Typically the orders satisfy $n \ge m$. In the continuous/time domain this is the
"physically realizable" condition; in the discrete domain, having $m > n$ would be
a **waste of coefficients**, because past information is more effectively stored in
the **states / outputs** than in extra input terms.

### Matrix form

Stack the equations into $y = X p$, with the parameter vector containing **both**
sets, e.g. $p = (a_1, \dots, a_n,\, b_1, \dots, b_m)^T$. The regressor matrix is
**wide**, with $n + m$ columns, its left block built from shifted **outputs**
$-y_{k-i}$ and its right block from shifted **inputs** $u_{k-i}$:

$$\begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_m \\ \vdots \\ y_N \end{pmatrix}
=
\begin{pmatrix}
-y_0 & 0 & \cdots & u_0 & 0 & \cdots \\
-y_1 & -y_0 & \cdots & u_1 & u_0 & \cdots \\
\vdots & & & \vdots & & \\
-y_{N-1} & -y_{N-2} & \cdots & u_{N-1} & u_{N-2} & \cdots & u_{N-m}
\end{pmatrix}
\begin{pmatrix} a_1 \\ \vdots \\ a_n \\ b_1 \\ \vdots \\ b_m \end{pmatrix}$$

We know the $y$'s and $u$'s and solve for the $a$'s and $b$'s (the poles and
zeros), again by least squares / pseudoinverse — exactly as in linear regression.
(Students build these matrices automatically in the exercises.)
