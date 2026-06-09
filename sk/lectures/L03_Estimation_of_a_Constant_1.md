---
lecture: L03
title: "Odhad konštanty #1"
course: Identifikácia
source: "https://www.youtube.com/watch?v=G6Auo4Mw_V0"
---

# L03 — Odhad konštanty #1

## Rozcvička: odhadovanie parametrov vygenerovaných dát

Nadväzujúc na predchádzajúce cvičenia (generovanie náhodných čísel a ich
vykresľovanie): máme niekoľko vzoriek — hody kockou, meranie teploty, tlaku, čohokoľvek —
každý experiment je označený svojou hodnotou. Pozrieme sa na takto vygenerované dáta
(1 000 vzoriek) — aká stredná hodnota a smerodajná odchýlka ich vygenerovala?

- **Priemer** vyzerá, že by mal byť okolo **1**.
- Pre **smerodajnú odchýlku** použijeme **pás 3σ**: z minulého týždňa, v rámci
  $\pm 3\sigma$ leží asi **99,73 %** hodnôt, teda takmer všetky hodnoty by mali ležať
  v tomto páse. Ak je celkový rozptyl asi **0,6** (polovica je **0,3**) a to sa
  rovná **trom** smerodajným odchýlkam, potom **jedna** smerodajná odchýlka je
  **0,1** — čo je presne to, čo rozdelenie vygenerovalo.

## Problém: odhad konštanty

Ide o **odhad konštanty** (v podstate nájdenie **priemeru**) a súčasne o skúmanie
**vlastností** tohto priemeru pri **čoraz väčšom počte vzoriek**.

Meriame dáta a chceme vypočítať jednu konštantu. Priemer môžeme odhadovať
„za behu": vezmeme prvých 10 vzoriek a odhadneme priemer, potom 50 vzoriek atď., a
sledujeme, ako sa odhad blíži k pravej strednej hodnote. Zápis: pravá konštanta
$\bar{y}$ (resp. $\hat{y}$, strieška označuje **odhad**), ktorá sa mení v čase
s pribúdajúcimi vzorkami.

### Štatistický model

Ak sa dáta riadia normálnym rozdelením — t. j. každá odchýlka/chyba pochádza
z Gaussovho/normálneho rozdelenia — model je jednoduchý **štatistický model**: pravá
konštanta sa rovná odhadovanej strednej hodnote plus nejaká chyba (lebo sme
nevykonali milión experimentov):

$$
y = \bar{y} + e
$$

Merania sú normálne rozdelené okolo strednej hodnoty $\bar{y}$ (ktorej pravú hodnotu
možno nikdy nedosiahneme) s nejakým rozptylom/smerodajnou odchýlkou. Keď sa
postaráme o strednú hodnotu (odhadneme ju), **chyba** je potom normálna s **nulovou
strednou hodnotou** a nejakou smerodajnou odchýlkou:

$$
e \sim N(0, \sigma^2)
$$

### Zápis vzoriek v čase

Merania prichádzajú v časoch $t_1, t_2, t_3, \dots$; používajúc indexovú notáciu,
ktorú čoskoro uvidíte v Teórii automatického riadenia (diskrétne systémy v čase),
vypustíme explicitný čas a jednoducho píšeme číslo experimentu 1, 2, 3, …

Keby **nebol žiadny šum**, každý experiment by konzistentne meral pravú konštantu
(napr. aktuálnu teplotu v miestnosti). So šumom sa body rozptyľujú a priemer povedzme
troch meraní nepristane presne na $\bar{y}$ — ak dva body ležia nad pravou hodnotou,
odhadovaný priemer je mierne posunutý.

## Kde sa to používa

- **Torricelliho zákon / konštanta ventilu.** S nádržou môžeme merať výšku
  $H$ a odtok $Q$. Konštantu ventilu nepoznáme, preto nastavíme niekoľko experimentov,
  zakaždým zmeráme $H$ a $Q$ a konštantu vypočítame ako

$$
C = \frac{Q}{\sqrt{H}}
$$

  Rôzne experimenty dávajú rôzne hodnoty; chceme štatisticky najlepšiu z nich.

- **Statické zosilnenie / časové konštanty prenosovej funkcie.** Z niekoľkých
  schodových testov (alebo dvojíc vstup/výstup v ustálenom stave) je **statické
  zosilnenie**

$$
Z = \frac{\Delta y}{\Delta u}
$$

  t. j. stĺpec zmien vstupu a stĺpec zmien výstupu. Pre nelineárny systém časová
  konštanta nie je ani jedinečná, a so šumom merania dáta opäť neukazujú jednu
  konzistentnú hodnotu.

## Tri spôsoby, ako získať jedno reprezentatívne číslo

Máme dáta $y_1, y_2, \dots, y_N$ a chceme jedno číslo, ktoré ideálne predpovedá
výsledok. Uvažujeme tri „priemery".

### Aritmetický priemer

$$
\hat{y} = \frac{1}{N}\sum_{i=1}^{N} y_i
$$

(rovnaký vzorec ako minule).

### Geometrický priemer

Namiesto sčítavania čísla **násobíme** a beriete $N$-tu odmocninu (aby jednotka
odhadu zodpovedala):

$$
\hat{y} = \sqrt[N]{\,y_1 \cdot y_2 \cdots y_N\,}
$$

Vlastnosť využívaná v Teórii automatického riadenia (či môže byť odozva na skok
dvoch nádrží periodická): **aritmetický priemer je vždy väčší alebo rovný
geometrickému priemeru** ($\text{AM} \ge \text{GM}$).

### Medián

**Medián** (ktorý sa dostal do médií ako *7-dňový medián* výskytu COVID-19) sa
nachádza algoritmicky, nie uzavretým vzorcom:

1. **Zoradiť** merania do $\tilde{y}_1, \tilde{y}_2, \dots$
2. Ak je $N$ **nepárne**, vezmeme stredný prvok na pozícii $\dfrac{N+1}{2}$.
   (Kontrola: $N = 3 \Rightarrow (3+1)/2 = 2$, druhý prvok.)
3. Ak je $N$ **párne**, vezmeme **priemer dvoch stredných prvkov** na pozíciách
   $\dfrac{N}{2}$ a $\dfrac{N}{2}+1$:

$$
y_m = \frac{\tilde{y}_{N/2} + \tilde{y}_{N/2 + 1}}{2}
$$

## Porovnanie troch odhadov

### Jeden beh („za behu")

Na rovnakom datasete sa aritmetický priemer (modrá), geometrický priemer (červená)
a medián (žltá) zakaždým prepočítavajú zo **všetkých doteraz videných vzoriek**
(napr. hodnota pri 40 používa prvých 400 vzoriek <!-- unclear: prednášajúci hovorí „pri 40 berieme 400 predchádzajúcich vzoriek" -->).

Pozorovania:
- Na **začiatku**, s malým počtom vzoriek, všetky tri **oscilovania** relatívne
  k mierke.
- Po čase sa všetky ustália a „robia svoju prácu"; **šum je oveľa väčší ako chyba
  odhadu**, takže aj s malým počtom vzoriek nie sú ďaleko od hodnoty.
- Priblížením (pás ~0,94 až ~1,06): podmienka $\text{AM} \ge \text{GM}$ platí —
  **červená (geometrická) krivka je vždy pod modrou (aritmetickou)**.
- **Aritmetický priemer** si počína celkovo najlepšie a **čoraz menej sa vychyľuje**
  / stáva sa istejším s pribúdajúcimi vzorkami. Naproti tomu **medián** sa ustáli,
  ale potom ho „vykoľají" poruchy (násilné správanie), ktoré aritmetický priemer
  ignoruje, pretože medián je založený len na jednom alebo dvoch číslach, kým
  aritmetický a geometrický priemer zohľadňuje **každé** číslo.

Navrhovaná celková miera kvality: **integrál rozdielu voči 1** (pravej hodnote).

### Štatistika cez mnoho behov (krabicové grafy)

Aby sme boli spravodliví, namiesto jedného „pretehu" vygenerujeme **1 000 dátových
bodov**, vypočítame tri odhady a celé to zopakujeme **1 000-krát** (kód je
v e-learningu). To sú skutočné štatistiky — 1 000 pretekov.

Výsledky sú zobrazené ako **krabicové grafy**, získané z histogramu 1 000 odhadov:
- **Stredná čiara** je najpravdepodobnejší odhad (priemer histogramu).
- **Hrany krabice** označujú, kde **distribučná funkcia** dosiahne
  **0,25** a **0,75** — t. j. 25 % výsledkov pretekov leží pod dolnou hranou a
  25 % nad hornou, takže krabica obsahuje centrálnych **50 %**.
- **Fúzy** (čierne pruhy) ukazujú rozptyl/rozsah výsledkov (napr. beh, kde medián
  skončil na 0,983 a neodhadol hodnotu 1).

Čítanie krabicových grafov:
- **Aritmetický priemer** — najlepší: najpravdepodobnejšia hodnota dosiahne **1**
  a existuje **50 % šanca**, že chyba je v rámci asi **±0,003**.
- **Geometrický priemer** — v podstate kópia aritmetického prípadu posunutá na
  mierne **nižšie** hodnoty (opäť $\text{AM} \ge \text{GM}$), podobný rozsah.
- **Medián** — najhorší v jednom ohľade: hoci jeho najpravdepodobnejšia hodnota je
  tiež 1, je pravdepodobnejšie dosiahnuť **väčšiu chybu** ako pri aritmetickom
  priemere a jeho **rozptyl je najväčší** (možno sa minúť o takmer 0,02). Tento
  veľký rozptyl sa pripisuje „zubatému" správaniu mediánu: jedna vzorka môže zmeniť,
  ktoré čísla vstúpia do vzorca.

## Prístup cez optimalizáciu: metóda najmenších štvorcov

Pred plne štatistickým prístupom formulujeme problém ako **odhad metódou najmenších
štvorcov**. Pre $N$ dátových bodov nájdeme odhad $\hat{y}$, ktorý minimalizuje
súčet štvorcov reziduálov:

$$
\min_{\hat{y}} \sum_{i=1}^{N} (y_i - \hat{y})^2
$$

Ide o **skalárnu, neobmedzenú optimalizačnú úlohu s jednou premennou**. Riešime
ju **analyticky** nastavením derivácie na nulu (nie gradient — ten je pre
multidimenzionálne problémy):

$$
\frac{d}{d\hat{y}} \sum_{i=1}^{N} (y_i - \hat{y})^2
  = \sum_{i=1}^{N} 2\,(y_i - \hat{y})(-1) = 0
$$

Derivácia súčtu je súčet derivácií. Vytkneme konštantu $2$ a $-1$ zo sumy; keďže
pravá strana je nula, môžeme deliť $-2$:

$$
\sum_{i=1}^{N} (y_i - \hat{y}) = 0
$$

Rozdelíme sumu. Člen $\sum_{i=1}^{N}\hat{y}$ sa rovná $N\hat{y}$ (pridávame $\hat{y}$
k sebe $N$-krát — „jeden banán, druhý banán, … až $N$ banánov"):

$$
\sum_{i=1}^{N} y_i - N\hat{y} = 0 \quad\Longrightarrow\quad
  \hat{y} = \frac{1}{N}\sum_{i=1}^{N} y_i
$$

Takže odpoveďou je **aritmetický priemer**. Minimalizovaná veličina
$\sum (y_i - \hat{y})^2$ je v podstate (škálovaný) **rozptyl** — minimalizácia
najmenších štvorcov je teda **minimalizáciou rozptylu odhadu**. Preto sa aritmetický
priemer správa tak dobre: minimalizuje samotnú chybu/rozptyl.

## Smerom k štatistickému prístupu: metóda maximálnej vierohodnosti

Štatistický prístup vychádza z rovnakého základu (dátové body z normálneho rozdelenia
so strednou hodnotou $\bar{y}$ a nejakým rozptylom), ale teraz **vezmeme $N$ vzoriek
a nájdeme najpravdepodobnejšiu hodnotu**, ktorá ich reprezentuje.

### Funkcia vierohodnosti

Nech $k$ je poradové číslo experimentu. Štatistici zapisujú pravdepodobnosť
pozorovania dátového bodu **za predpokladu** parametrov (zvislá čiara „|" sa číta
„za predpokladu, že") — PDF kódovaná strednou hodnotou a rozptylom. Náš prípad je
ale **opačný**: **máme dáta** a chceme nájsť parametre. Rovnaká Gaussova funkcia
sa znova použije pod iným názvom — **funkcia vierohodnosti** — pričom sa pýtame
na vierohodnosť toho, že dáta boli vygenerované rozdelením so strednou hodnotou
$\hat{y}$ a smerodajnou odchýlkou $\sigma$:

$$
L(\bar{y}, \sigma \mid y_k) = \frac{1}{\sigma\sqrt{2\pi}}\,
  e^{-\frac{(y_k - \bar{y})^2}{2\sigma^2}}
$$

Je to tá istá dobrá stará Gaussova funkcia; mení sa len názov. (Čoskoro sa objaví
**funkcia log-vierohodnosti**.) Jej vyhodnotenie pre $y_1, y_2, \dots$ dáva príspevok
každého dátového bodu k strednej hodnote a smerodajnej odchýlke.

### Odhad maximálnou vierohodnosťou

Aby sme z niekoľkých experimentov dostali **jedno** číslo, tvoríme **spojenú**
veličinu — ako pri kocke minule, pravdepodobnosť udalosti A **a** udalosti B je
**súčin** ich pravdepodobností (napr. hodenie jednotky dvakrát za sebou: $a \cdot a$).
Jednotlivé vierohodnosti sú $L$, takže **odhad maximálnou vierohodnosťou** formulujeme
ako maximalizáciu **spojenej** pravdepodobnosti — súčinu cez všetky vzorky —
vzhľadom na dva parametre:

$$
\max_{\bar{y},\,\sigma} \;\prod_{k=1}^{N} L(\bar{y}, \sigma \mid y_k)
$$

Toto „monštrum" (súčin viacerých Gaussových zlomkov/exponenciál) bude
**analyticky vyriešené nabudúce** (záves).
