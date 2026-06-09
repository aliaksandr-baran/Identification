---
lecture: L01
title: "Introduction to Identification. Data Visualization."
course: Identification
source: "https://www.youtube.com/watch?v=PZz7OA9_4Gw"
---

# L01 — Introduction to Identification. Data Visualization.

## About this lecture

The lecturer introduces the subject of **identification** and frames this first
lecture as a relatively brief, "cartoon" overview — lots of pictures and **no
mathematical formulas whatsoever**. The goal is to look at how our world works
at the moment, how it used to work, what changed, and why we should look at the
subject of system identification. Some of the material was already shown in the
"modeling in process industry" class, but here it goes a bit deeper.

## The accelerating world

The first message is that our world is really accelerating — everything is
happening faster and faster. The lecturer illustrates this with a sequence of
big events in human history and the shrinking gaps between them:

- The **Agricultural Revolution** — when mankind stopped wandering around the
  Earth and settled down somewhere with a field of crops (vegetables, fruit,
  and so on).
- It then took **8,000 years** until the **Industrial Revolution**, where we
  realized we can divide jobs in society and make some jobs automated or at
  least mechanized — using a steam engine or other engines to help us.
- From the Industrial Revolution to the **invention of the light bulb**.
- Only **120 years** passed between the invention of the light bulb and the
  **moon landing**.
- Only **20 years** from the moon landing to the **World Wide Web** (the
  lecturer first says "90 years" then corrects to about 20).
- And **9 years** to the **sequencing of the human genome**.

These events are somewhat arbitrary, but they are big events in human history.
The interesting part is that the gap between them keeps shortening — we are
speeding up in development. This speed-up in the 20th and 21st century was also
observed in something called **Moore's law** (Slovak: *Moorov zákon*).

## Moore's law

Mr Moore was an engineer (the lecturer believes at Bell Laboratories in the US).
He made a **data-based observation**: he took some data, used a time axis, and
marked several points representing the **number of transistors** on different
computer processors (nowadays we might say "on chips") — basically how much
computing power a processor holds. He plotted ("depicted, drew") this data and
found out that **roughly each 10 years the number of transistors is doubling**.

When something is doubling, that is **exponential growth**.

### The chess-and-rice story (example of exponential growth)

The standard first example of exponential growth: a story about a shah/king in
Iran or Persia who was playing chess with one of his servants. He lost the game
and asked the servant what he wanted as a reward. The servant said: put **one**
grain of rice on the first square of the chessboard, **two** grains on the next
square, then keep **doubling**. On the third square there are four grains, on
the fourth square eight grains, and it keeps doubling. By the time you reach the
end (about $2^{64}$ grains of rice), you have about the same number of grains as the
number of atoms in the universe, or even more. So it is quite scary.

### The logarithmic axis

On the Moore's-law plot, the y-axis is **not a linear scale** — it is
**logarithmic**. One step in that direction does not mean adding the same amount
each time (1, 2, 3, 4, 5, 6); it means adding **powers of 10**. Here one step
corresponds to increasing the scale by $10^5$, i.e. by 100,000 (for example,
from 1 to 100,000). Because of this, **if you get a straight line on such a
plot, that already indicates exponential growth** — which is exactly what Moore
observed.

With further evolution, Moore's law was actually getting **violated**: we have
been seeing even more rapid development and even higher numbers of transistors
on a chip. The graph the lecturer shows is from 2011; it predicts we will reach
the **singularity** at some point — that in 2023 the computing power of a chip
will surpass the human brain. Maybe we are somewhere around it.

## The growth of data

The same trend, in slightly different numbers, is happening with the **amount of
data**. Cheaper, more available, and more reliable sensors give rise to more
sensing capacity: we can sense more data, store more data, at a much smaller
price. The problem now is that **we need to make sense of the data** — the world
is extremely rich with data.

The lecturer stresses that **data by itself does not tell us what happened** —
it just sits in some database. It is good to plot the data and have at least
basic statistics for an overview, but **making sense out of data is a much
harder problem.** The rest of the lecture goes through example datasets.

## Examples of data in the world

### Dog breed prices during COVID

A news item (around 2022) reported that the prices of dog breeds rapidly changed
during the COVID pandemic in the UK / Great Britain. The reason discussed: the
**demand rose** — during the pandemic, in some places only people with dogs were
allowed to go outside, and people stuck at home wanted some company/friends.

### Nitrogen dioxide levels over China

Satellite images show the **nitrogen dioxide (NO₂) levels** over China in
**January 2020** and again in **February 2020**. In February the levels are much
lower. The reason: **factories shut down** because of the COVID-19 pandemic.
The lecturer notes that COVID-19 acts like a great source of data — it was
effectively a **step change in many inputs in the world** (analogous to a step
change in some input applied to a device).

### Fossil fuel prices

Around **March 2020** there is a big step change in **fossil fuel prices** —
oil, naphta/natural gas, even coal. The point: if, back in January 2020, you
could predict what would happen to oil prices, you could adapt your company's
strategy (buy more oil, empty reservoirs while the price is down, etc.) and
make money. Money is a big driver of these problems.

### Kyoto aquarium penguin relationships

A cartoon-like **flow chart of complicated romantic relationships between
penguins** at the Kyoto aquarium. Data was tracked on how the penguins like each
other (including possible "cheating" on partners) and then depicted. One possible
use: the aquarium staff could avoid fights between the penguins by managing
"love triangles."

### Facebook blocking a French city

Around April 2021, Facebook blocked the web page of a French city
<!-- unclear: city name, caption reads "Bish"; sounds like the town "Bitche" -->.
Statistically, the combination of letters in the name mostly resembles a swear
word. Facebook apparently has a policy that swear words should not be names of
websites / Facebook pages / users, and runs an algorithm comparing swear words
against names. With statistical evidence (more than **95% confidence**), the
algorithm claimed the website was violating the rules.

### Google Maps eco-friendly routing

Google Maps was supposed to offer the most ecological / environmentally friendly
route for your car. It is unclear whether this fully materialized; it still seems
to offer mainly the fastest (and lowest-distance) route. A discussed limitation:
the route choice does not really take into account whether you go up or down, and
suggesting a route through a traffic jam is not ecological because you end up
running your engine while stuck.

### Data breach headline / data privacy

A news headline (jokingly: if you listen to Nickelback
<!-- unclear: caption reads "Nickel Beck" -->, be aware of this threat) points to
**data privacy**: how do we encrypt and cipher data to make them inexposable to
third parties. The lecturer notes (without naming countries, to stay politically
correct) that you may not want to share your data with anybody, yet we are doing
it quite often.

### Bitcoin price (the lecturer's favourite trend)

A series of newspaper headlines is shown, deliberately out of order at first,
then chronological: Bitcoin price over \$30,000; could go long-term to \$140,000;
over \$40,000; in three days the price is down; value below \$30,000; then up 20%
in seven days. The span of these headlines is just **one month** — so it is hard
to keep track of from headlines alone. Hence the idea: **plot the data to
visualize it.**

Walking through the Bitcoin price plot over time:

- The trend starts around **2013**. There was an initial hype, then the price
  went down (around August 2015 someone who bought near \$1,000 would be sad).
- But if you just waited two years, even buying at that price would put you about
  **300% in plus** in four years — investments take some time.
- Extending the graph (a red line marks where the previous graph ended), we enter
  a volatile period; the price kept increasing through 2017–2018.
- If you caught the trend late and bought at about \$12,500, within half a year to
  a year you would be back to about \$2,500. Should you sell? Probably not,
  because it would change again.
- By 2021 (the year the shown headlines came from) it got another big impulse —
  possibly due to milder regulations and better acceptance with merchants, more
  public access to the market, people not travelling and having "free money"
  (stimulus checks) to invest.
- The lecturer also shows the price on a **logarithmic scale** (similar to the
  Moore's-law plot). On the log scale you would be tempted to fit a **straight
  line** and start predicting whether the Bitcoin price in 2025 will be where it
  is now. Visualizing the data in a different context can reveal at least some
  information.
- Later: a steep decline until 2023, then recovery, and a recent jump around the
  **US elections** and the hype around it. Another big jump is attributed to Elon
  Musk deciding to invest \$1 billion in Bitcoin
  <!-- unclear: figure stated as "one billion / 1 billion dollars" -->.

The lecturer states this is **not** to persuade anyone to invest in Bitcoin —
he personally does not, disliking that it drains resources and (in his view) has
no value. The point is that **different aspects in the data cause changes of some
trend at some point**, and it is quite hard to find out what actually caused what
we see in the data values.

### COVID active cases in Slovakia

Another trend is given as a guessing game with day-number units (e.g. day 1 to
~33, values around 600–650; then 1 to ~100 days, with the previous trend
reversed; then peaks over almost a year). It is the **number of active COVID
cases in Slovakia**. Between March 2020 and 21 January (2021) there was a first
mild wave, but the **second wave after the summer** (around September 2020) hit
quite heavily.

### Daily PCR cases and filtering

Related data: the **number of daily PCR cases** (PCR being a method of testing
for the COVID antigen) versus days since the first case. The lecturer made this
plot in **MATLAB** from data from the National Center of Health Information.

The raw curve (yellow) shows **sharp spikes / peaks**. The reason: the number of
new cases was much higher on **Monday**, because many testing places did not work
on weekends, or people spent time at home with the flu over the weekend and got
tested on Monday.

A course topic preview: **how to reveal this kind of trend**. The blue curve
does some sort of **averaging** — similar to the **7-day median** number of
active cases used during the pandemic (which fed into the "traffic light"
status). This is nothing else than applied **filtering** (as seen, or to be seen,
in the "Technical Means of Automation" class). Even the prime minister was using
the results of this filtering.

### Germany — cases vs deaths (correlation)

COVID-19 data from **Germany** (not Slovakia). The first wave was mild, the second
much tougher, and it continued. The **top plot** shows the number of cases; the
**bottom plot** shows the number of deaths (people who passed away).

Observations from the discussion:

- The two signals share the same basic **shape**, especially at the beginning —
  the two variables (signals) are **correlated**: when one signal increases the
  other also increases (not necessarily at the same time). Treated as two
  variables, this can be seen as a **dynamic system / process** where something
  happening triggered a response. **Correlation and causality are not the same
  thing**, but the data at least shows a qualitative response.
- At a later peak (a kind of third wave in 2021) the rise is **not as pronounced
  in the number of deaths**. Possible explanations: **vaccination** (started
  around February 2021); a **mutation of the virus** that was not as deadly; and
  some **built-up resistance** in the population (people could be infected
  multiple times).

### Survivorship bias — WWII airplanes

A classic picture: in the Second World War, the engineering problem was how to
make more airplanes come back safely from battle. The graph shows, from a
collection of returning planes, **where the planes were hit and still returned**.

The paradox: should we reinforce the parts that **are** hit, or the parts that
are **not** hit? The data says we should reinforce the parts that are **not**
hit — this is **survivorship bias**. Planes hit in the marked places returned
home, so those areas can take damage; the planes that did **not** return were hit
elsewhere (e.g. the engine, the pilot, or a narrow critical part). A naive,
sentimental reaction would reinforce the visibly-hit spots, but that would not
help. This is one of the very early **data-based decision-making** problems: how
to make sense out of data and act accordingly to improve some performance.

### Medical screening data

Beyond a cardiogram, many **screening techniques** in medicine produce this sort
of data (e.g. being scanned for a tumour, X-rays for broken bones or dental
problems). The amount of data is growing, but the number of skilled doctors who
can read it is not growing as much — so we need to do something about it. (The
lecturer mentions a student looking for a summer internship at Siemens
Healthineers <!-- unclear: caption reads "seens healthy years" --> working on
this type of problem.) Steps include first **digitalizing** data that may only
exist on paper in pen/ink, and then finding trends to reason about what happened,
the patient's status, the diagnosis, and the treatment.

### Electricity generation vs CO₂ intensity per country

A plot of **electricity generation vs CO₂ intensity per country**. Each point is
sampled every **one hour**: the amount of electricity generated by the country's
power plants, and the CO₂ intensity (how much CO₂ is emitted to the atmosphere by
that production). Countries shown include France, Germany, Poland, Italy, Spain,
Belgium, Portugal (Slovakia not shown).

Conclusions from the discussion:

- **Poland** is the least efficient (highest CO₂) — it has a lot of coal and many
  coal power plants. Its electricity generation is also much **narrower** (less
  flexible).
- **France** uses a lot of **nuclear** power. It is interesting because **no
  matter how much power is needed, it emits roughly the same amount of CO₂** —
  showing the efficiency / environmental friendliness of nuclear power plants.
  France is also relatively flexible in generation while staying on the
  environmentally-friendly end.
- **Germany** shows an interesting trend along an axis with a **negative slope /
  negative derivative**: when producing a relatively **small** amount of energy
  the CO₂ emissions are **high**, but when producing a **high** amount of energy
  the CO₂ emissions are **lower**. This is somewhat paradoxical at first. The
  explanation: it is the effect of **coal power plants** running even when
  renewables are not. The high generation comes during the day — peaks of good
  wind for wind turbines and clear days for solar cells.

## Types of data visualization

The examples lead to different types of data visualization. Starting from
collected data, even just using different plots can already reveal insights. The
lecturer highlights four common types.

### Time series

Whatever signal / trend / information you have, plotted against its corresponding
**time step** on the horizontal axis. This is what was done in "Theory of
Automatic Control" and throughout this lecture.

- Sometimes there are **no time stamps** (e.g. the electricity plot), so we do
  not know exactly when each point happened — we only know the **sampling
  interval** (e.g. the points are one hour apart).
- When we **do** know the time stamp, we can reason about it. The lecturer gives
  an example of 15-minute data from a plant where the data points suddenly seemed
  to **double** (two values for one hour). The cause turned out to be the
  **daylight-saving time shift** (summer/winter time): at the switch, the times
  ran 2:00, 2:15, 2:30, 2:45, 3:00, then 2:00 again — a practical challenge you
  may encounter.
- With time series it can also be hard to observe **correlations** when there are
  only a couple of variables.

### Scatter / correlation plots

Here we take two variables and plot one against the other, **losing the sense of
time** (we no longer know when each point was collected, only that the pair
occurred together).

- **Positive correlation:** if the variable on the horizontal axis increases, the
  other variable also increases (moving right, we also move up). You can think of
  approximating the cloud of points with a line whose slope is positive. One axis
  appears as a function of the other.
- **Negative correlation:** the Germany case is an example — generating more power
  goes with emitting less CO₂.
- **Centering:** the plot can be drawn so that the origin is moved to the place of
  the most common value (the **mean**). After centering, positive deviations and
  negative deviations from the mean are directly visible, and it is easier to see,
  e.g., that increasing the horizontal value by 2 increases the vertical value by
  10. This is much harder to read from absolute numbers (what does "600 g CO₂
  equivalent" mean — is it big or small?). So visualization is not only about
  *how I plot the graph* but also *how I transform my variables* (we already saw
  the logarithmic transform with the Bitcoin price).

### Histograms

A histogram represents how **dense** the data is in certain regions — how
frequently certain values occur. It works like making **bins** ("baskets"): for a
bin in the middle, count how many points fall between, say, −0.1 and +0.1; the
count is like dropping a pebble/ball into a column. This directly shows that some
values are totally unlikely or never observed, while others are more likely. The
shape may start to look like the famous **bell curve / Gaussian curve**.

In a combined scatter+histogram view, red regions mark a very likely place for
points to occur, while blue can represent **outliers** or much less likely values
(e.g. points far from the mean, with negative deviations). A scatter plot can
show **almost no correlation**: applying the test "if we slightly increase the
horizontal variable, what happens to the vertical one?" gives no clear answer
(there are increasing and non-increasing directions). The histograms along each
axis then show the density of values in each variable separately.

### Parity plots

Parity plots are less commonly seen but useful. A problem with the previous plots
is that you must choose a relatively **small number of variables** to display
(two, or at most three dimensions), so you cannot easily visualize many
variables. One possibility a parity plot offers is to plot the **observed trend
versus how your model / understanding predicts that trend**.

The specific example: the **brightness of pixels** in two photographs of the same
object taken about **4 hours apart**, with brightness values between 0 and 0.5
(white vs black). The two variables share the same unit, but one is the **actual
observation** and the other is a **prediction** of that variable (or another
variable we try to correlate with). A histogram-like colouring shows where many
pixels lie: blue dots are less likely values, red is where many pixels are. Along
the line $y = x$ we can see the similarity between the two photos: if a pixel has
brightness 0.1 in one photo and the same situation is captured, that point lies
near the $y = x$ line. The plot shows the two photos are very similar, differing
only by some noise or small changes. (Students will do experiments with parity
plots during the exercises.)

## Closing

The lecturer skips the final slide for the day, invites questions and comments,
and asks students for their opinion on the lecture and on it being delivered in
English. He notes that the **YouTube video is post-processed** after the lecture
with **subtitles**, and that students can even **download the transcript** from
the lecture to help them.
