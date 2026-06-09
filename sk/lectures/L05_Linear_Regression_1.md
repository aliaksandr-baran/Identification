---
lecture: L05
title: "Lineárna regresia #1"
course: Identifikácia
source: "https://www.youtube.com/watch?v=J6QAT6-BkDY"
---

# L05 — Lineárna regresia #1

> Vzorce overené podľa prednášateľových snímok (*Ident 17 03 2026 / 24 03
> 2026*); kde popis na snímke obsahoval chybu (najmä interval spoľahlivosti
> sklonu a štandardizácia), boli rekonštruované zo snímky a poznamenané.

## Od odhadu konštanty k lineárnej regresii

Na minulej prednáške sme vykonali tisíc experimentov, pri ktorých sme merali jednu
konštantnú veličinu so šumom merania, a zistili sme, že **aritmetický priemer** je
najlepší odhadovač, ktorý sa s rastúcim počtom meraní aproximuje k skutočnej hodnote.
V inom pohľade sme zostavili **histogram** dát a **nafitovali normálne (Gaussovo)
rozdelenie** (dva parametre: priemer a smerodajná odchýlka), čím sme odhadli
konštantu a odrazili neistotu.

Dnes sa obraz mierne mení: stále vykonávame niekoľko experimentov, ale teraz existuje
merateľný **rozdiel medzi experimentmi**, zachytený nezávislou premennou $x$.
Praktický príklad (aj v cvičeniach): meriame nejaký plyn pri rôznych
**teplotách** $x$ a zaznamenávame zodpovedajúce **tlaky** $y$. Ak predchádzajúci
obraz otočíme, úloha je podobná — hľadáme **strednú hodnotu, teraz ale krivku**
závislú od $x$. Pozdĺž tejto priamky si opäť predstavíme „mini-Gaussovku", berieme
každé meranie do úvahy a hľadáme **odhad maximálnej vierohodnosti**, ktorý, ako vieme,
sa rovná **odhadu metódou najmenších štvorcov**.

## Model lineárnej regresie

Každé $k$-té pozorovanie je vysvetlené **modelom / predikciou** plus
**neistotou** (šum merania). Pri lineárnej regresii je model čo najjednoduchší —
**priamka** parametrizovaná dvomi hodnotami:

$$
\hat{y}_k = a\,x_k + b
$$

- $a$ — **sklon**.
- $b$ — **absolútny člen (posun)**. Ak je sklon nula, redukuje sa to na
  **odhad konštanty** z minulej prednáška.

(Vo všeobecnosti snímka tiež píše $\hat{y} = \hat{p}\,f(x)$.) Predpoklad z minulého
týždňa zostáva: bez chyby by sme merali body presne na priamke; chyba je
**Gaussovsky / normálne rozdelená** s **nulovou strednou hodnotou** (senzor je
v priemere správny) a nejakou smerodajnou odchýlkou:

$$
e \sim N(0, \sigma^2)
$$

## Prečo „regresia"? (Galton)

„Regresia" znamená úpadok / niečo, čo sa pokazí. Názov pochádza od
**Galtona**, biológa, ktorý vykreslil **výšku rodiča** oproti **výške dieťaťa**.
Čakalo by sa $y = x$ (vysokí rodičia → vysoké deti, nízki rodičia → nízke deti),
ale skutočné dáta ukázali **odchýlku**: vysokí rodičia mali deti mierne **nižšie**
a nízki rodičia deti mierne **vyššie**, ako sa čakalo. Dospel k záveru, že výška
populácie smeruje k priemeru — výška detí sa **„regresuje k priemeru,"** a termín
zostal.

## Metóda najmenších štvorcov: dve normálne rovnice

Dáta sú dvojice $(x_k, y_k)$, $k = 1, \dots, N$. Nájdeme $a$ a $b$ metódou
najmenších štvorcov (multiplikátor $\tfrac{1}{2}$ je zahrnutý pre pohodlie):

$$
\min_{a,b}\; \frac{1}{2}\sum_{k=1}^{N}\big(a\,x_k + b - y_k\big)^2
$$

Derivujeme podľa $a$ a $b$ ($x_k, y_k$ sú čísla) a nastavíme na nulu. Derivácia
sumy je suma derivácií; pre druhú mocninu dostaneme dvojnásobok zátvorky krát derivácia
vnútra zátvorky:

$$
\frac{\partial}{\partial a} = 0 = \frac{1}{2}\sum_{k=1}^{N} 2\,x_k\,(a\,x_k + b - y_k)
$$

$$
\frac{\partial}{\partial b} = 0 = \frac{1}{2}\sum_{k=1}^{N} 2\,(a\,x_k + b - y_k)
$$

Konštanta $\tfrac{1}{2}$ a dvojka sa vykrátia. Rozkladom každej zátvorky na
samostatné sumy (a s použitím $\sum_{k=1}^{N} b = N b$):

$$
0 = a\sum_{k=1}^{N} x_k + bN - \sum_{k=1}^{N} y_k
$$

$$
0 = a\sum_{k=1}^{N} x_k^2 + b\sum_{k=1}^{N} x_k - \sum_{k=1}^{N} y_k x_k
$$

### Absolútny člen má jednoduchý tvar

Z prvej rovnice, izoláciou $b$ (prenesieme $-Nb$ na druhú stranu, vydelíme $N$)
dostaneme iba **aritmetické priemery**:

$$
b = \frac{1}{N}\sum_{k=1}^{N} y_k - a\,\frac{1}{N}\sum_{k=1}^{N} x_k
    = \bar{y} - a\,\bar{x}
$$

„Keď raz uvidíte aritmetický priemer, nedokážete ho nevidieť."

### Maticový tvar $Mp = r$

Obe rovnice majú štruktúru konštanta $+\,a\cdot(\text{konšt.}) +
b\cdot(\text{konšt.})$, teda zapíšeme ich ako lineárny algebraický systém $Mp = r$
s $p = \binom{a}{b}$, riešený v MATLABe ako `p = M\r` (potvrdené na snímke):

$$
\begin{pmatrix}
\sum_{k=1}^{N} x_k & N \\
\sum_{k=1}^{N} x_k^2 & \sum_{k=1}^{N} x_k
\end{pmatrix}
\begin{pmatrix} a \\ b \end{pmatrix} =
\begin{pmatrix}
\sum_{k=1}^{N} y_k \\
\sum_{k=1}^{N} y_k x_k
\end{pmatrix}
$$

Matica $M$ obsahuje iba dáta ($x$); pravá strana mieša $y$ a $x$.

## Centrovanie a štandardizácia dát

Vychádzajúc z $y = a x + b$ a dosadením $b = \bar{y} - a\bar{x}$:

$$
y = a x + \bar{y} - a\bar{x}
  \quad\Longrightarrow\quad
  y - \bar{y} = a\,(x - \bar{x})
$$

Ak teda **transformujeme dáta vopred**, absolútny člen zmizne. Definujeme (snímka):

- **Centrované dáta:** $\tilde{x} = x - \bar{x}$, $\tilde{y} = y - \bar{y}$
  (odčítame priemer — posunieme mrak bodov tak, aby bol počiatok v jeho strede).
  Potom $\tilde{y} = a\,\tilde{x}$ (bez absolútneho člena).
  Príklad: $x = 1,2,3,4,5 \Rightarrow \tilde{x} = -2,-1,0,1,2$.
- **Štandardizované (normalizované) dáta:** navyše vydelíme smerodajnou odchýlkou

$$
\tilde{x} = \frac{x - \bar{x}}{\sigma_x}, \qquad
    \tilde{y} = \frac{y - \bar{y}}{\sigma_y}
$$

  kde $\sigma = \sqrt{\dfrac{1}{N-1}\sum_{k=1}^{N}(x_k - \bar{x})^2}$ (Besselova
  korekcia). Štandardizované premenné majú **nulovú strednú hodnotu a smerodajnú
  odchýlku jedna**. <!-- unclear: V popise bol algebrický výraz skomolený; snímka dáva čisté centrované/štandardizované definície použité vyššie. -->

**Prečo centrovať?** Priamo vidíme, či je korelácia **kladná alebo záporná**
(kladné $x$ spárované s kladným $y$ → kladný sklon), čo je ťažké odčítať zo surových
osí ako Kelvin (250–350) oproti pascalom.

**Prečo štandardizovať?** Rôzne premenné majú veľmi rozdielne rozptyly — tlak v
pascaloch ($10^5$–$10^6$) oproti teplote (rozpätie 100 K) — čo robí sklon ťažko
porovnateľným. Po štandardizácii normalizovaný sklon $a_n$ leží v rozsahu $[-1, 1]$,
takže pri viacerých nezávislých premenných môžeme **porovnávať silu korelácie**:
čím bližšie je $|a_n|$ k 1, tým silnejšie závisí meraná premenná od tej nezávislej.
Prednášateľ zdôrazňuje, že **normalizácia / štandardizácia** šetrí obrovské množstvo
času v každej dátovej úlohe (nielen pri identifikácii); „štandardizácia" konkrétne
znamená nulový priemer a jednotková smerodajná odchýlka.

## Interval spoľahlivosti sklonu

Podobne ako minulý týždeň (kde sme štandardizovali chybu odhadu na použitie
chí-kvadrát štatistiky), môžeme zostrojiť interval spoľahlivosti pre sklon. S
odhadom $\hat{a}$ získaným z `M\r`, hladinou pravdepodobnosti $\alpha$ (napr. 95%) a
kvantilom chí-kvadrát leží skutočný sklon $a^*$ v (snímka):

$$
\hat{a} - \frac{\hat{\sigma}}{\sqrt{N}}\,\chi^{-1}_{\alpha}
  \;\le\; a^* \;\le\;
  \hat{a} + \frac{\hat{\sigma}}{\sqrt{N}}\,\chi^{-1}_{\alpha}
$$

kde $\chi^{-1}_{\alpha}$ je inverzná distribučná funkcia (kvantil) chí-kvadrát
rozdelenia (jeden príkaz v MATLABe) a $\hat{\sigma}$ je smerodajná odchýlka toho,
ako model fituje dáta:

$$
\hat{\sigma} = \sqrt{\frac{1}{N-1}\sum_{k=1}^{N}(\hat{y}_k - y_k)^2}
$$

Toto je **odmocnina strednej kvadratickej chyby (RMSE)** (niekedy len MSE, stredná
kvadratická chyba, bez odmocniny). RMSE je praktická, pretože rovnako ako smerodajná
odchýlka žije v rovnakých jednotkách ako dáta — „náš model sa mýli o 0,01 bar."

## Smerom k viacrozmernej regresii — maticový/vektorový zápis

Pri viacerých parametroch matice založené na sumách rastú, preto prechádzame na
**maticový/vektorový zápis**. Vo všeobecnosti meriame niekoľko nezávislých premenných —
napr. teplotu $T$, koncentráciu $C$ a dokonca transformáciu ako $T^2$. Model ako

$$
\hat{y} = a_1 T + a_2 C + a_3 T^2 + \dots
$$

je stále **lineárny v parametroch**, teda lineárna regresia stále platí (**model
lineárny v parametroch**). Ale prenášanie súm $T$, $C$, $T^2$, $T\cdot y$ atď.
rýchlo prestáva byť praktické.

### Regresná matica

Usporiadame dáta tak, aby každý **stĺpec** bol jedna nezávislá premenná (alebo jej
transformácia) a každý **riadok** jeden experiment. Pre $N$ experimentov a $P$
premenných má **regresná matica** $X$ rozmery $N \times P$ (prednášateľ zámerne píše
stĺpce ako prvé, pretože v praxi môže byť ~200 premenných, ale ~16 000 meraní (napr.
15-minútové dáta za rok), takže stĺpce, reprezentujúce každú fyzikálnu premennú, majú
väčší význam). Malé $x$ označuje jeden dátový **vektor** (jeden stĺpec); veľké $X$ je
celá matica. Výstup $y$ sa predpokladá ako jedna meraná veličina, takže zostáva
**vektorom**.

### Užitočné vektorové identity (potvrdené na snímke)

Pre $x = (x_1, \dots, x_N)^T$ a vektor samých jednotiek $\mathbf{1}$:

$$
x^T x = x_1^2 + x_2^2 + \dots + x_N^2 = \sum_{k=1}^{N} x_k^2
$$

$$
\mathbf{1}^T x = x^T \mathbf{1} = \sum_{k=1}^{N} x_k, \qquad
  \mathbf{1}^T y = \sum_{k=1}^{N} y_k, \qquad
  x^T y = \sum_{k=1}^{N} x_k y_k
$$

Poznámka: násobenie matíc nie je komutatívne, $A B \ne B A$, ale pre vektory
$a^T b = b^T a$.

Pomocou týchto identity dve normálne rovnice splynú: $\sum x_k^2 \to x^T x$,
$\sum y_k x_k \to y^T x$, $\sum x_k \to \mathbf{1}^T x$, $\sum y_k \to
\mathbf{1}^T y$ a $N$ zostáva $N$.

### Maticový model a problém metódy najmenších štvorcov

Model v maticovom tvare používa regresnú maticu $X$ ($N \times P$) a vektor
parametrov $p$ ($P \times 1$):

$$
\hat{y} = X p
$$

takže $\hat{y}$ je $N \times 1$ — jedna predikcia na experiment, rovnaký rozmer ako
merané dáta. Hľadanie $p$ formulujeme ako problém metódy najmenších štvorcov, pričom
sumu štvorcov rozdielov zapíšeme vo vektorovom tvare (transponovaný súčin so sebou,
keďže $x^T x = \sum x_k^2$):

$$
\min_{p}\; \frac{1}{2}\,(y - \hat{y})^T (y - \hat{y})
$$

**Nabudúce** dosadíme $\hat{y} = X p$ a odvodíme riešenie, ktoré bude mať tvar
$p = (\text{matica})^{-1}(\text{matica})\,(\text{vektor})$ — normálne rovnice.
(Užitočná prerekvizita: transponovaný súčin, $(AB)^T = B^T A^T$.)
