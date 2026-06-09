---
lecture: L09
title: "Identifikácia dynamických systémov"
course: Identifikácia
source: "https://www.youtube.com/watch?v=WEGsY_W654g"
---

# L09 — Identifikácia dynamických systémov

> Vzorce overené podľa prednášateľových snímok (*Identification L09 —
> Identification of dyn systems*): impulzná odozva, konvolučný integrál,
> FIR matica a prenosová funkcia ARX / forma v časovej oblasti.

## Rekapitulácia a cieľ

Filtre z minulej prednášky sú samy osebe **dynamické systémy** — filter a prenosová
funkcia sú dve strany tej istej mince. **Dolnopriepustný filter** chcel zosilnenie 1
(na reprezentáciu dlhodobých trendov) a zvolenú časovú konštantu (na filtráciu šumu),
a bol realizovaný ako model s **konečnou impulznou odozvou (FIR)**, odvodený z
(váženého) kĺzavého priemeru. FIR je jedným z prvých modelov, ktoré treba vyskúšať
pri identifikácii dynamických systémov (zosilnenie dolnopriepustného ≈ 1, zosilnenie
hornopriepustného ≈ 0).

Typická úloha identifikácie: privedenie **skokovej zmeny** na vstup v istom čase a
meranie odozvy zariadenia $y_{\text{merané}}$, potom nájdenie modelu reprezentujúceho
zariadenie. Učebnicové metódy skokovej odozvy (napr. Strejcova metóda) predpokladajú,
že vždy dostaneme čistú jedinú skokovú odozvu — čo nie je vždy prípad. Musíme
**zovšeobecniť**.

## Demystifikácia FIR: impulzná odozva

Reprezentujeme dynamický systém ako blok so vstupom a výstupom. Je lepšie pracovať v
**Laplaceovej oblasti**, kde (pre lineárnu dynamiku reprezentovateľnú prenosovou
funkciou):

$$
Y(s) = G(s)\,U(s)
$$

Čo je $G(s)$ v **časovej oblasti**, t.j. $g(t)$? Vezmime najjednoduchší príklad
(snímka):

$$
G(s) = \frac{1}{s + \frac{1}{T}} \quad\xrightarrow{\;\mathcal{L}^{-1}\;}\quad
  g(t) = e^{-t/T}
$$

(používajúc $\dfrac{1}{s+a} \to e^{-at}$). Táto $g(t)$ začína na konštante pri $t = 0$
a klesá k nule keď $t \to \infty$ (pre $T > 0$).

Čo predstavuje $G(s)$ **samotné**? So vstupom **jednotkového skoku** $u(t) = 1(t)$
dostaneme **prechodovú charakteristiku**. Ale s idealizovaným **impulzom** $u(t) = \delta(t)$
— ktorého Laplaceov obraz je $U(s) = 1$ — výstup je $Y(s) = G(s)$. Teda $g(t)$ je
**impulzná odozva** (odtiaľ „impulzná odozva" vo FIR). Intuitívne: nádrž napájaná
konštantným prietokom, krátko narušená náhlym otočením ventilu a vrátená späť —
systém prvého rádu reaguje okamžite na impulz a efekt pomaly mizne v priebehu času.

## Konvolučný integrál

Na výpočet výstupu v časovej oblasti používame **konvolúciu** (nevinne vyzerajúce
„$*$"):

$$
y(t) = g(t) * u(t)
  = \int_0^t g(\tau)\,u(t-\tau)\,d\tau
  = \int_0^t g(t-\tau)\,u(\tau)\,d\tau
$$

(dve ekvivalentné formy). Integrál je infinitezimálny **súčet cez minulý čas**. Dynamický
systém si uchováva **pamäť** o minulých vstupoch: výstup v aktuálnom čase $t_k$ silno
reaguje na nedávne vstupy ($t_{k-1}, t_{k-2}, \dots$), ale takmer vôbec na vstupy
dávno v minulosti (prietok pred rokom teraz nezáleží). Funkcia $g$ pôsobí ako
**váha**, ktorá, otočená v čase (záporné znamienko v $g(t-\tau)$), váži nedávne vstupy
oveľa viac než vzdialené — „včerajšie počasie ovplyvňuje dnešné počasie oveľa viac
ako počasie pred rokom." Konvolúcia má mnoho aplikácií (konvolučné neurónové siete,
spracovanie obrazu, riadenie/modelovanie).

### FIR ako diskretizovaná konvolúcia

Model FIR je diskrétny náprotivok, kde integrál sa stáva konečným súčtom a koeficienty
$b_i$ sú **vzorky $g$** v diskrétnych bodoch:

$$
y_k = \sum_{i=1}^{m} b_i\, u_{k-i}
$$

Výstup v čase $k$ je akumulovaný vplyv minulých vstupov.

## Trénovanie modelu FIR na skokovej odozve

Predpokladajme **skokovú odozvu** so skokom v čase 0 (bez predpokladu, že zosilnenie
je 1). Zapíšme rovnice predikcie. Pred skokom sú všetky vstupy nulové, teda:

$$
y_0 = 0 = b_1\cdot 0 + b_2\cdot 0 + \dots + b_m\cdot 0
$$

$$
y_1 = b_1 u_0 + b_2 u_{-1} + \dots + b_m u_{1-m} \quad(\text{minulé členy} = 0)
$$

$$
y_2 = b_1 u_1 + b_2 u_0 + \dots + b_m u_{2-m}
$$

$$
\vdots
$$

$$
y_m = b_1 u_{m-1} + b_2 u_{m-2} + \dots + b_m u_0
$$

$$
\vdots
$$

$$
y_N = b_1 u_{N-1} + b_2 u_{N-2} + \dots + b_m u_{N-m}
$$

Keďže tieto sú **lineárne v parametroch** $b_i$ ($y$ a $u$ sú známe dáta), zostavíme
maticovú rovnicu presne ako pri lineárnej regresii, $y = X p$ s
$p = (b_1, \dots, b_m)^T$:

$$
\begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_m \\ \vdots \\ y_N \end{pmatrix} =
\begin{pmatrix}
u_0 & 0 & 0 & \cdots & 0 \\
u_1 & u_0 & 0 & \cdots & 0 \\
\vdots & & & & \\
u_{m-1} & u_{m-2} & \cdots & & u_0 \\
\vdots & & & & \\
u_{N-1} & u_{N-2} & \cdots & & u_{N-m}
\end{pmatrix}
\begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_m \end{pmatrix}
$$

Každý riadok zostavíme tak, že vezmeme vstupný „pás" $\dots, 0, 0, u_0, u_1, u_2, \dots$,
otočíme ho a vložíme na správne miesto. Matica sa prvýkrát stáva **štvorcovou**
v riadku $m$ (vždy má $m$ stĺpcov), čo je dôležité, pretože chceme inverznú
(alebo pseudoinverznú) maticu. Tu:

- $m$ = **rád modelu** (počet parametrov na identifikáciu);
- $N$ = počet dátových bodov, kde $N \ge m$ (viac, ideálne oveľa viac, ak je šum veľký).

Ako vedľajší produkt, začatie matice od neskoršieho riadku (vynechanie úvodných
nulových riadkov) funguje pre **všeobecný** vstupný signál, nielen pre skok —
ustálený stav v minulosti je dobrý, ale nie vždy nevyhnutný predpoklad.

## Model ARX

Aby sme dosiahli typy modelov oboznámené z automatického riadenia, pripomeňme, že
prenosová funkcia FIR bola len **čitateľom** s $1$ v menovateli. Rozšírime menovateľ
(snímka) — **AutoRegressívny model s eXogénnym vstupom (ARX)**:

$$
G(z^{-1}) = \frac{\sum_{i=1}^{m} b_i\, z^{-i}}{1 + \sum_{i=1}^{n} a_i\, z^{-i}}\;
  z^{-n_k}
$$

Voliteľný člen $z^{-n_k}$ predstavuje **časové oneskorenie vstupu** $n_k$ krokov —
rovnaká idea ako blok jednotkového oneskorenia $z^{-1}$ v Simulinku, ktorý robí
z aktuálneho výstupu vstup v nasledujúcom kroku, $y(t) \to y(t+1)$. Oneskorenie
v diskusii odložíme nabok. (Hranice súm $n, m, n_k$ sledujú notáciu MATLABu.)

### Forma v časovej oblasti pomocou spätného posunu

Vyčistením zlomku:

$$
Y(z^{-1})\Big(1 + \sum_{i=1}^{n} a_i z^{-i}\Big)
  = U(z^{-1})\sum_{i=1}^{m} b_i z^{-i}
$$

Spätný posun $z^{-i} \leftrightarrow y_{k-i}$ (a $z^0 = 1$ je bez posunu,
$y_k$) dáva priamo:

$$
y_k = -\sum_{i=1}^{n} a_i\, y_{k-i} + \sum_{i=1}^{m} b_i\, u_{k-i}
$$

Toto je **ARX model rádu $m/n$**.

### Prečo „autoregresívny s exogénnym vstupom"

- Časť **menovateľa / $a_i$** spôsobuje, že aktuálny výstup závisí od svojich **vlastných
  minulých výstupov** $y_{k-i}$ — model **regreduje sám na sebe**, teda
  *autoregresívny (AR)*.
- Časť **čitateľa / $b_i$** je to, čo sme skôr nazývali model FIR, ale tu je to
  **exogénny vstup** (vonkajší vplyv; „exogénny" nie „externý" z historických dôvodov).
- Bez vstupnej časti, $y_k = -\sum a_i y_{k-i}$ je len **AR model**. Forma ARX dokáže
  reprezentovať všetky bežné prenosové funkcie (póly, nuly).

## Trénovanie modelu ARX na skokovej odozve

Ako pri FIR, predpokladajme dáta skokovej odozvy s ustáleným stavom (všetko nula)
pred skokom. Rozložíme súčty na zložky. Rovnice predikcie:

$$
y_1 = -a_1 y_0 - a_2 y_{-1} - \dots - a_n y_{1-n}
        + b_1 u_0 + b_2 u_{-1} + \dots + b_m u_{1-m}
$$

$$
y_2 = -a_1 y_1 - a_2 y_0 - \dots - a_n y_{2-n}
        + b_1 u_1 + b_2 u_0 + \dots + b_m u_{2-m}
$$

$$
\vdots
$$

$$
y_m = -a_1 y_{m-1} - a_2 y_{m-2} - \dots - a_n y_{m-n}
        + b_1 u_{m-1} + b_2 u_{m-2} + \dots + b_m u_0
$$

$$
\vdots
$$

$$
y_N = -a_1 y_{N-1} - a_2 y_{N-2} - \dots
        + \dots + b_m u_{N-m}
$$

(všetky členy so zápornými alebo nulovými indexmi „minulosti" sú nulové na základe
predpokladu ustáleného stavu).

### Prečo $n \ge m$

Zvyčajne ráde spĺňajú $n \ge m$. V spojitej/časovej oblasti je to podmienka
„fyzikálnej realizovateľnosti"; v diskrétnej oblasti by mať $m > n$ bolo
**plytvaním koeficientmi**, pretože minulé informácie sú efektívnejšie uložené v
**stavoch / výstupoch** než v ďalších vstupných členoch.

### Maticová forma

Zložíme rovnice do $y = X p$, kde vektor parametrov obsahuje **obe** sady, napr.
$p = (a_1, \dots, a_n,\, b_1, \dots, b_m)^T$. Regresná matica je
**široká**, s $n + m$ stĺpcami, jej ľavý blok je zostavený z posunutých **výstupov**
$-y_{k-i}$ a pravý blok z posunutých **vstupov** $u_{k-i}$:

$$
\begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_m \\ \vdots \\ y_N \end{pmatrix} =
\begin{pmatrix}
-y_0 & 0 & \cdots & u_0 & 0 & \cdots \\
-y_1 & -y_0 & \cdots & u_1 & u_0 & \cdots \\
\vdots & & & \vdots & & \\
-y_{N-1} & -y_{N-2} & \cdots & u_{N-1} & u_{N-2} & \cdots & u_{N-m}
\end{pmatrix}
\begin{pmatrix} a_1 \\ \vdots \\ a_n \\ b_1 \\ \vdots \\ b_m \end{pmatrix}
$$

Poznáme $y$ a $u$ a riešime pre $a$ a $b$ (póly a nuly), opäť metódou najmenších
štvorcov / pseudoinverznou maticou — presne ako pri lineárnej regresii.
(Študenti zostavujú tieto matice automaticky v cvičeniach.)
