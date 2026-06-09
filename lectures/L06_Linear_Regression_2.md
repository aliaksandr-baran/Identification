---
lecture: L06
title: "Lineárna regresia #2"
course: Identifikácia
source: "https://www.youtube.com/watch?v=DLTnS_SWr_k"
---

# L06 — Lineárna regresia #2

> Maticové vzorce overené podľa prednášateľových snímok (*Ident 17 03 2026 /
> 24 03 2026*): odvodenie metódy najmenších štvorcov vo vektorovom tvare, normálne
> rovnice / pseudoinverzná matica a kovariančná matica / matica korelácie.

## Rekapitulácia: maticový tvar

Hľadáme **koreláciu** medzi nezávislými a závislými nameranými dátami a smerujeme
k pochopeniu toho, že niektoré experimenty sú lepšie ako iné a niektoré premenné sú
pre model vhodnejšie ako iné.

Dáta zoradíme do **regresnej matice** $X$ — každý **stĺpec** je jedna premenná
(alebo jej nelineárna transformácia), každý **riadok** je jeden experiment ($N$
experimentov, $n_p$ parametrov/premenných). **Rovnica predikcie** je

$$
\hat{y} = X p
$$

kde $p$ je vektor parametrov a $\hat{y}$ obsahuje jednu predikciu na experiment.
Pripomenieme kľúčovú identitu: $x^T x$ sa rovná **súčtu štvorcov** zložiek $x$.

## Metóda najmenších štvorcov vo vektorovom tvare

Zapíšeme účelovú funkciu metódy najmenších štvorcov pomocou vektora $(y - \hat{y})$
(transponovaný súčin so sebou dáva súčet štvorcov):

$$
\min_{p}\; \frac{1}{2}\,(\hat{y} - y)^T(\hat{y} - y)
$$

Rozviňme súčin do štyroch členov:

$$
\min_{p}\; \frac{1}{2}\Big(\hat{y}^T\hat{y} - \hat{y}^T y - y^T\hat{y} + y^T y\Big)
$$

Dva krížové členy sú „rovnaké, ale rôzne, a predsa rovnaké": $\hat{y}^T y$ aj
$y^T \hat{y}$ sú skaláre a rovnajú sa, pretože $a^T b = b^T a$. (Pre vektor neexistuje
zmysluplný pojem „umocnenie vektora", preto zachovávame tvar transponovaný súčin.)
Zoskupením:

$$
\min_{p}\; \frac{1}{2}\hat{y}^T\hat{y} - y^T\hat{y} + \frac{1}{2}y^T y
$$

Dosadíme $\hat{y} = X p$ a použijeme $\hat{y}^T = p^T X^T$:

$$
\min_{p}\; \frac{1}{2}\,p^T X^T X\, p - y^T X p + \frac{1}{2}y^T y
$$

## Derivovanie podľa vektora

Potrebujeme dve pravidlá maticovo-vektorového počtu (všetky takéto vzorce obsahuje
„Matrix Cookbook"):

- **Lineárny člen:** $\dfrac{\partial\,(a^T x)}{\partial x} = a$. Tu je konštantný
  riadok $y^T X$, takže jeho derivácia dáva vektor $X^T y$ — príspevok (sklon v každom
  rozmere $x$) pre každý prvok.
- **Kvadratická forma:** $\dfrac{\partial\,(x^T A x)}{\partial x} = (A + A^T)\,x$, a
  ak je $A$ **symetrická** ($A = A^T$), toto je jednoducho $2 A x$ — analógia skalárneho
  $\dfrac{d}{dx}(x^2) = 2x$.

**Je $X^T X$ symetrická?** Priamy dôkaz pomocou $(AB)^T = B^T A^T$:

$$
(X^T X)^T = X^T (X^T)^T = X^T X \qquad \text{q.e.d.}
$$

Teda je symetrická a môžeme použiť jednoduchšie pravidlo $2 A x$.

Derivujeme účelovú funkciu podľa $p$ a nastavíme na nulu. Konštanta
$\tfrac{1}{2}y^T y$ zmizne:

$$
\frac{\partial}{\partial p} = 0 = X^T X\, p - X^T y
$$

## Normálne rovnice a pseudoinverzná matica

Toto je lineárny systém $X^T X\, p = X^T y$ — zámerne tvar $Ax = b$
(ekvivalentne Newtonov krok pre viacdimenzionálnu kvadratiku). Vynásobíme
$(X^T X)^{-1}$:

$$
p = (X^T X)^{-1} X^T y
$$

Optimálne parametre sú **lineárna kombinácia meraní** (a obsahujú aritmetické
priemery). Keďže $X$ ($N \times n_p$) vo všeobecnosti **nie je štvorcová** (viac
experimentov ako parametrov), nemôžeme ju priamo invertovať; zostavením $X^T X$
dostaneme **štvorcovú** ($n_p \times n_p$) invertovateľnú maticu. Celá operácia
$(X^T X)^{-1} X^T$ je **pseudoinverzná matica** matice $X$, označovaná $X^{\dagger}$
(dýka, „ako malý meč"):

$$
X p = y \quad\Longrightarrow\quad p = X^{\dagger} y
$$

V MATLABe riešime pomocou **spätného lomítka**: `p = X\y`. Toto je preferované pred
explicitným zostavením `inv(X'*X)*X'*y` — MATLAB varuje pred `inv`/`^-1`, pretože
spätné lomítko analyzuje štruktúru matice (či je štvorcová, akú dekompozíciu použiť)
a je to **najefektívnejší a numericky najstabilnejší** spôsob.
„Tri stlačenia kláves, enter a máme naše parametre." Preto bolo náročné odvodenie
nakoniec hodné námahy.

## Kovariančná matica

Matica $X^T X$ je výnimočná a nesie veľa informácií — je to (až na škálovanie)
**kovariančná matica**. Pripomenieme, že $X$ je $N \times n_p$ (stĺpce = premenné,
riadky = experimenty). Jej transponovaná $X^T$ je $n_p \times N$. Vynásobením:

$$
X^T X =
\begin{pmatrix}
x_1^T x_1 & x_1^T x_2 & \cdots & x_1^T x_{n_p} \\
x_2^T x_1 & x_2^T x_2 & & \vdots \\
\vdots & & \ddots & \\
x_{n_p}^T x_1 & \cdots & & x_{n_p}^T x_{n_p}
\end{pmatrix}
$$

kde $x_i$ je vektor $i$-tej premennej naprieč všetkými $N$ experimentmi.
Diagonálne prvky sú súčty štvorcov ($\sum_k x_{k,i}^2$); mimdiagonálne prvky sú
krížové členy ($\sum_k x_{k,i}\,x_{k,j}$) so spoločným experimentálnym indexom. Matica
je symetrická (dokázané vyššie), takže prvky sú zrkadlové cez diagonálu.

Škálovaním (pre **centrované** dáta) dostaneme **kovariančnú maticu**:

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

- **Diagonála — rozptyly** (Besselova korekcia, centrované dáta):

$$
\sigma_{x_1}^2 = \frac{1}{N-1}\sum_{k=1}^{N} x_{k,1}^2
$$

  odmocninou je smerodajná odchýlka — diagonála teda obnáša rozptyly jednotlivých
  premenných.
- **Mimdiagonálne prvky — kovariancie:**

$$
\sigma_{x_1 x_2} = \frac{1}{N-1}\sum_{k=1}^{N} x_{k,1}\,x_{k,2}
$$

  **kovariancia** premennej 1 s premennou 2, vypovedajúca o ich vzájomnom vzťahu.

Hoci sa zdá, že $X^T X$ stráca informáciu obsiahnutú v $X$, v skutočnosti nám
**prináša hlbší pohľad** na dáta. (Snímka ukazuje mrak bodov $x_1$ oproti $x_2$:
ak sa mrak naklonení tak, že kladné hodnoty sa párujú s kladnými, platí
$\sigma_{x_1 x_2} > 0$.)

## Matica korelácie

Kovariancie nie sú porovnateľné naprieč premenných s rôznym škálovaním, preto
**normalizujeme** kovariančnú maticu na **maticu korelácie** $C$ (bez náročného
maticového počtu) — prvok po prvku:

$$
C_{ij} = \frac{V_{ij}}{\sigma_{x_i}\,\sigma_{x_j}}
$$

Napríklad $C_{11} = \dfrac{\sigma_{x_1}^2}{\sigma_{x_1}\,\sigma_{x_1}} = 1$, teda
**diagonála je samé jednotky** (rovnako ako pri normalizácii dát na jednotkovú
smerodajnú odchýlku). Zaujímavá je **mimdiagonála**: hodnoty $C_{ij}$ sú
**korelačné koeficienty**, garantovane ležiace medzi **−1 a 1**.

### Interpretácia korelačných koeficientov

Napríklad pri 10 premenných je $C$ matica $10 \times 10$, ktorá nám umožňuje
porovnávať premenné po pároch:

- $C_{ij} > 0$ — **kladná korelácia**: ak jedna premenná rastie, druhá tiež rastie
  (napr. teplota ↑ → tlak ↑).
- $C_{ij} < 0$ — **záporná korelácia**: jedna rastie, kým druhá klesá.
- Podľa absolútnej hodnoty (hrubé hranice): $|C_{ij}| \ge 0.8$ → **silná** korelácia;
  medzi $0.5$ a $0.8$ → **mierna / predpokladaná** korelácia; pod $0.5$ → veľa sa
  tvrdiť nedá (záleží na kvalite dát). Malý koeficient nedokazuje úplnú nezávislosť,
  ale koreláciu premenných tiež nemôžeme reálne tvrdiť.

V príklade destilačnej kolóny (z cvičení) sa zistí napríklad, že tlaky na vrchu a
dne kolóny sú kladne korelované — čo potvrdzuje intuícia zo separačných procesov,
ale pri neznámych dátach je to oveľa ťažšie posúdiť.

## Korelácia nie je kauzalita

Varovný príklad z fakultnej správy: graf počtu študentov fakulty
**odchádzajúcich do zahraničia** oproti počtu **zahraničných študentov prichádzajúcich**
na fakultu za niekoľko akademických rokov (iba päť čísel). Vypočítaný korelačný
koeficient je asi **0,7**, čo naznačuje určitú koreláciu. Ale dáva zmysel, že menej
odchádzajúcich študentov *spôsobuje* viac prichádzajúcich? Žiadna takáto „magická
sila" neexistuje. Namiesto toho existuje **spoločný faktor** ovplyvňujúci obe čísla —
**pandémia COVID**, ktorá znížila obe hodnoty. Záverečné ponaučenie: **buďte opatrní
s koreláciami — nie každá z nich znamená kauzalitu**; korelácia nemusí naznačovať,
že jedna premenná skutočne ovplyvňuje druhú.
