---
lecture: L04
title: "Odhad konštanty #2"
course: Identifikácia
source: "https://www.youtube.com/watch?v=PXgpgTrh07Y"
---

# L04 — Odhad konštanty #2

## Rekapitulácia nastavenia

Pokračujeme v štatistickom prístupe k odhadovaniu konštanty. Namerali sme dáta,
o ktorých predpokladáme, že pochádzajú z **normálneho rozdelenia** s nejakou
konštantnou strednou hodnotou a nejakou smerodajnou odchýlkou, ktorých hodnoty
nepoznáme. Z toho si pripomenieme **PDF** — ako pravdepodobné je pozorovanie $y_k$,
keby sme poznali strednú hodnotu a smerodajnú odchýlku — a jej sesterskú funkciu,
**funkciu vierohodnosti** $L$, ktorá vymieňa úlohy: keď je $y_k$ zadané (napr.
sme namerali 1,6 alebo 1,1), stredná hodnota a smerodajná odchýlka sa stávajú
parametrami a pýtame sa, aká vierohodná je tá-ktorá hodnota parametrov.

Keďže všetky dáta $y_k$ pochádzajú z rovnakého procesu (rovnaké dva parametre),
**spojená pravdepodobnosť** je **súčin** vierohodností.

## Maximalizácia vierohodnosti — trik s logaritmom

Maximalizujeme spojenú vierohodnosť vzhľadom na $\bar{y}$ a $\sigma$:

$$
\max_{\bar{y},\,\sigma}\;\prod_{k=1}^{N}
  \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(y_k-\bar{y})^2}{2\sigma^2}}
$$

Derivovanie **súčinu** (pravidlo súčinu s $N-1$ nediferencovanými členmi) je
nepríjemné. Trik: vezmeme **logaritmus**, ktorý premení súčin na súčet, lebo
$\ln(a\cdot b) = \ln a + \ln b$. Prirodzený logaritmus je výhodný, keďže
$\ln(e^x) = x$, takže exponenciála zmizne. Aplikovaním $\ln$ sa súčin $\prod$
premení na sumu $\sum$:

$$
\max_{\bar{y},\,\sigma}\;\sum_{k=1}^{N}
  \left[\ln\!\frac{1}{\sigma\sqrt{2\pi}}
        - \frac{(y_k-\bar{y})^2}{2\sigma^2}\right]
$$

**Mení logaritmus polohu optima?** Nie — aplikovanie **monotónnej (rastúcej)**
funkcie zachováva, ktorá hodnota je väčšia, takže extrémy zostávajú na rovnakom
mieste (krivka vyzerá inak, ale argmax/argmin je nezmenený). Keby bola transformujúca
funkcia klesajúca, museli by sme pridať znamienko mínus. Pôvodná účelová funkcia
nemusí byť monotónna; monotónna musí byť len transformujúca funkcia.

**Prevod max na min** (ako na predmete optimalizácie) negovaním účelovej funkcie —
to nemá nič spoločné s monotónnosťou. Prepísaním $\frac{1}{\sigma\sqrt{2\pi}}
= (\sigma\sqrt{2\pi})^{-1}$ vnútorný $\ln$ prispieva $-\ln(\sigma\sqrt{2\pi})$,
a po celkovom mínuse dostaneme $+\ln(\sigma\sqrt{2\pi})$:

$$
\min_{\bar{y},\,\sigma}\;\sum_{k=1}^{N}
  \left[\ln\!\big(\sigma\sqrt{2\pi}\big)
        + \frac{(y_k-\bar{y})^2}{2\sigma^2}\right]
$$

Toto už obsahuje dobre známy **súčet štvorcov** $\sum (y_k - \bar{y})^2$
z optimalizačného (metóda najmenších štvorcov) prístupu.

## Odhadovanie strednej hodnoty

Označme účelovú funkciu $F$. Nastavíme $\dfrac{\partial F}{\partial \bar{y}} = 0$.
Prvý člen $\bar{y}$ neobsahuje, takže (rovnako ako na minulej prednáške, s konštantou
$\tfrac{1}{2\sigma^2}$, ktorá sa skráti s pravou stranou rovnicou nula):

$$
0 = \sum_{k=1}^{N} (y_k - \bar{y})
  \quad\Longrightarrow\quad
  \hat{y} = \frac{1}{N}\sum_{k=1}^{N} y_k
$$

Teda **aritmetický priemer je zároveň odhad maximálnej vierohodnosti (štatisticky
najpravdepodobnejší odhad)**, nielen optimum metódy najmenších štvorcov — preto sa
funkcia $L$ nazýva funkciou *vierohodnosti*.

## Odhadovanie smerodajnej odchýlky

Teraz nastavíme $\dfrac{\partial F}{\partial \sigma} = 0$. Rozložíme logaritmus
súčinu $\ln(\sigma\sqrt{2\pi}) = \ln\sqrt{2\pi} + \ln\sigma$, takže

$$
F = \sum_{k=1}^{N}\Big[\ln\sqrt{2\pi} + \ln\sigma
      + \tfrac{1}{2}(y_k-\bar{y})^2\,\sigma^{-2}\Big]
$$

Derivácia sumy je suma derivácií: konštanta $\ln\sqrt{2\pi}$ dáva 0, $\ln\sigma$
dáva $\tfrac{1}{\sigma}$ a posledný člen dáva $-\dfrac{(y_k-\bar{y})^2}{\sigma^3}$:

$$
\frac{\partial F}{\partial \sigma}
  = \sum_{k=1}^{N}\left[\frac{1}{\sigma}
      - \frac{(y_k-\bar{y})^2}{\sigma^{3}}\right] = 0
$$

Vynásobíme $\sigma^3$. Člen $\sum_{k=1}^{N}\sigma^2 = N\sigma^2$
(sčítame $k$-nezávislý člen $N$-krát), zatiaľ čo súčet štvorcov musí zostať
vo vnútri sumy (závisí od $k$):

$$
N\sigma^2 = \sum_{k=1}^{N}(y_k-\bar{y})^2
  \quad\Longrightarrow\quad
  \sigma^2 = \frac{1}{N}\sum_{k=1}^{N}(y_k-\bar{y})^2
$$

ekvivalentne $\sigma = \sqrt{\dfrac{1}{N}\sum_{k=1}^{N}(y_k-\bar{y})^2}$ (po slovensky:
*rozptyl* = variance). Ide v podstate o **znovu použitú definíciu rozptylu**
(priemerná vzdialenosť dát od strednej hodnoty), ktorá dáva Gaussovmu zvonu jeho šírku.

### Besselova korekcia

Tento odhad $\sigma^2$ **nie je celkom správny**: jeden **stupeň voľnosti** sme
už „minuli" odhadovaním strednej hodnoty z tých istých dát (pomocou aritmetického
priemeru). Takže z $N$ dátových bodov jeden už odpadol a správny odhad delí $N-1$:

$$
\sigma^2 = \frac{1}{N-1}\sum_{k=1}^{N}(y_k-\bar{y})^2
$$

Delenie $N-1$ namiesto $N$ robí číslo mierne **väčším**, aby sme **nepodcenili**
šum (tzv. „štandardizovaná chyba", ktorú si možno pamätáte zo strednej školy).
Toto sa nazýva **Besselova korekcia**.

## Štatistika chyby odhadu — nestrannosť

Teraz si kladieme otázku, na ktorú optimalizácia nedokáže odpovedať: z jednej sady
meraní, **ako ďaleko od pravdy je odhad?** Definujeme **chybu odhadu** ako rozdiel
medzi pravou konštantou $\bar{y}$ a odhadom $\hat{y}$. Táto chyba $e$ má tiež
**normálne rozdelenie**; hľadáme jej **strednú hodnotu** a **smerodajnú odchýlku**.

**Operátor strednej hodnoty** $E[\cdot]$ jednoducho vracia priemer a je **lineárny**,
teda rozkladá sa cez sumy a vyťahuje konštanty. Pravá stredná hodnota konštanty je
konštanta sama, $E[\bar{y}] = \bar{y}$, a každé meranie má $E[y_k] = \bar{y}$:

$$
E[e] = E[\bar{y} - \hat{y}]
  = \bar{y} - \frac{1}{N}\sum_{k=1}^{N} E[y_k]
  = \bar{y} - \frac{1}{N}\,N\,\bar{y} = 0
$$

Teda s rastúcim počtom meraní **chyba odhadu konverguje k nule** a odhad konverguje
k pravej hodnote. Táto vlastnosť sa pomenúva: aritmetický priemer je **nestranný
odhad**
<!-- unclear: prednášajúci hovorí „po slovensky sa to volá veľmi pekne", ale slovenský termín nebol zachytený -->.
**Geometrický priemer** je naproti tomu **zaujatý** odhad (má určitý posun).

## Rozptyl chyby odhadu — konzistentnosť

Ďalej skúmame **rozptyl chyby odhadu**:

$$
\mathrm{var}(e) = E\!\left[(\bar{y} - \hat{y})^2\right]
  = E\!\left[\Big(\bar{y} - \tfrac{1}{N}\textstyle\sum_{k=1}^{N} y_k\Big)^2\right]
$$

Vytkneme $\tfrac{1}{N}$ zo štvorca: pomocou $\bar{y} = \tfrac{N}{N}\bar{y}$
napíšeme $\bar{y} - \tfrac{1}{N}\sum y_k = \tfrac{1}{N}\sum_{k=1}^{N}(\bar{y}-y_k)$,
takže štvorec dáva $\tfrac{1}{N^2}\big(\sum_{k=1}^{N}(\bar{y}-y_k)\big)^2$.

Prekážka: ide o **štvorec sumy**, nie súčet štvorcov — a všeobecne platí
$(a+b)^2 \ne a^2 + b^2$ kvôli **krížovým členom** (napr. $y_1 y_2$).
Tu však berieme **strednú hodnotu** (priemer) a uplatňujeme **predpoklad
nezávislosti** (★): stredná hodnota súčinu akýchkoľvek dvoch rôznych meraní je nula,

$$
E[y_i\,y_j] = 0 \quad (i \ne j),
$$

čo platí, keď sú **vzorky/šum nezávislé** — šum teraz neovplyvňuje neskorší šum
(a naopak), čo je rozumný predpoklad (odôvodnený na neskoršej prednáške). Pri
nezávislosti krížové členy zmiznú, a štvorec sumy sa v rámci strednej hodnoty rovná
súčtu štvorcov:

$$
\mathrm{var}(e)
  = \frac{1}{N^2}\sum_{k=1}^{N} E\!\left[(\bar{y}-y_k)^2\right]
  = \frac{1}{N^2}\,N\,\sigma^2
  = \frac{\sigma^2}{N}
$$

lebo $\sum_{k=1}^{N} E[(\bar{y}-y_k)^2] = \sum \sigma^2 = N\sigma^2$ (rozptyl šumu
merania). Teda:

$$
\sigma_e^2 = \frac{\sigma^2}{N}, \qquad \sigma_e = \frac{\sigma}{\sqrt{N}}
$$

**Interpretácia — konzistentnosť.** $\sigma$ je mierou zašumenia senzora; $\sigma_e$
je mierou odchýlky odhadu konštanty. **Čím viac vzoriek vezmeme, tým menšia je
chyba** — to nie je automatické, je to **vlastnosť aritmetického priemeru**, a odhad
sa potom nazýva **konzistentný** (so 100 meraniami je chyba menšia ako s 10). To je
plynulé zmršťovanie osciláciía aritmetického priemeru videné minule, na rozdiel od
náhlych skokov mediánu.

**Praktické pravidlo.** Keďže $\sigma_e = \sigma/\sqrt{N}$, chyba vo fyzikálnych
jednotkách sa zlepšuje s **odmocninou** počtu meraní. Príklad: senzor so smerodajnou
odchýlkou $\sigma = 1$, požadovaná presnosť odhadu $0{,}1$ — zlepšenie desaťnásobne
vyžaduje aspoň $10^2 =$ **100 meraní**.

## Rozdelenie chyby a chí-kvadrát rozdelenie

Teraz sme charakterizovali chybu odhadu: $e \sim N(0, \sigma_e^2)$. Viac meraní
udržiava strednú hodnotu na nule, ale **zužuje** Gaussov zvon (väčšia istota o
odhadovanej strednej hodnote).

Jedno ďalšie rozdelenie: ak je premenná $X$ normálne rozdelená (povedzme nulová
stredná hodnota), aké je rozdelenie $X^2$? Záporné hodnoty nehrajú úlohu (štvorec
nemôže byť záporný), takže rozdelenie je jednostranné. Toto je **chí-kvadrát
rozdelenie** (po slovensky: *chí kvadrát*). Má parameter: po sčítaní $n$
štvorcov normálnych premenných,

$$
\sum_{i=1}^{n} X_i^2 \sim \chi^2 \text{ s } n \text{ stupňami voľnosti},
$$

kde $n$ počíta, koľko normálnych premenných bolo umocnených a sčítaných. To bude
užitočné neskôr pri odhadovaní viacerých parametrov (nielen jednej konštanty).

## Interval spoľahlivosti pre konštantu

Normalizujeme chybu tak, aby mala nulovú strednú hodnotu a jednotkovú smerodajnú
odchýlku, potom ju umocníme — jedna umocnená normálna hodnota má chí-kvadrát
rozdelenie s **1** stupňom voľnosti:

$$
\left(\frac{\bar{y} - \hat{y}}{\sigma_e}\right)^2 \sim \chi^2_{1}
$$

Pomocou **distribučnej funkcie** chí-kvadrát rozdelenia môžeme zostrojiť **interval
spoľahlivosti**, presne ako pri úvode do štatistiky. Pre hladinu spoľahlivosti
$\alpha$ označíme **kvantil** (inverznú CDF) ako $\chi^2_{\alpha}$ (číslo získané
jedným príkazom MATLAB-u). Potom

$$
\left(\frac{\bar{y} - \hat{y}}{\sigma_e}\right)^2 \le \chi^2_{\alpha}
$$

Vezmeme odmocninu nerovnosti (keďže $x^2 \le 4 \Rightarrow |x| \le 2$):

$$
-\sqrt{\chi^2_{\alpha}} \;\le\; \frac{\bar{y} - \hat{y}}{\sigma_e}
  \;\le\; \sqrt{\chi^2_{\alpha}}
$$

a úpravou dostaneme interval pre pravú konštantu $\bar{y}$:

$$
\hat{y} - \sigma_e\sqrt{\chi^2_{\alpha}} \;\le\; \bar{y}
  \;\le\; \hat{y} + \sigma_e\sqrt{\chi^2_{\alpha}}
$$

Každá veličina na ľavej a pravej strane je vypočítateľná **z dát**: $\hat{y}$ je
aritmetický priemer, $\sigma_e$ je odhadovaná smerodajná odchýlka chyby (tá s
$\sqrt{N}$) a $\chi^2_{\alpha}$ je hodnota štatistickej funkcie z MATLAB-u. Ľahko
tak zistíme, ako ďaleko je odhad od skutočnosti (napr. pravá hodnota leží medzi
$-0{,}01$ a $+0{,}01$ okolo odhadu), a **viac meraní tento interval zmenšuje a
zmenšuje**.
