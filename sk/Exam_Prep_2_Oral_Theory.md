# Identifikácia — Príprava na ústnu skúšku (teória)

> Cieľ: vedieť *slovne vysvetliť* pojmy za každým praktickým krokom,
> odpovedať na „prečo" a zapísať kľúčové vzorce na tabuľu.

## Forma skúšky
Sú vám náhodne pridelené **dve témy — jedna z každej kategórie**:

**I. Statická identifikácia**
1. Úvod do štatistiky
2. Odhad konštanty
3. Lineárna regresia
4. Praktické aspekty lineárnej regresie

**II. Dynamická identifikácia**
5. Filtrácia dynamických signálov
6. Modelovanie dynamických systémov
7. Rekurzívna identifikácia
8. Praktické aspekty identifikácie

Zvyšok tohto súboru má dve časti: **(1)** postup prezentácie pre každú tému —
čo napísať na tabuľu ku každej z 8 tém — a **(2)** podrobné otázky a odpovede
(časti A–R), ktoré ich podkladajú.

---

## Čo povedať k téme (plán na tabuľu)

### Téma 1 — Úvod do štatistiky  *(→ Časti A, B)*
1. Populácia vs. výber; náhodná premenná; meranie = signál + šum.
2. Poloha: priemer, medián, geometrický priemer — a kedy sa ktorý používa (robustnosť).
3. Rozptyl: rozptyl a smerodajná odchýlka; menovateľ **$N-1$** (nestranný).
4. **Hustota pravdepodobnosti (PDF)** (hustota, integrál = 1) vs. **distribučná funkcia (CDF)** ($P(X \le x)$) vs. **kvantil** (inverzná CDF).
5. **Normálne rozdelenie**; pravidlo 68–95–99,7 ($\pm 1/2/3\,\sigma$).
6. Histogramy; s viac dátami histogram $\to$ skutočná hustota pravdepodobnosti (zákon veľkých čísel).
7. Prečo na tom záleží: Gaussov šum je práve to, čo robí **metódu najmenších štvorcov** optimálnou.

### Téma 2 — Odhad konštanty  *(→ Časť EC, B)*
1. Zadanie: veľa zašumených meraní jednej skutočnej hodnoty, $y_i = c + e_i$.
2. Odhad konštanty metódou najmenších štvorcov = **aritmetický priemer** (odvodiť).
3. Vlastnosti odhadcu: **nestranný**, **konzistentný**; rozptyl odhadu
   $\mathrm{var}(\hat{c}) = \sigma^2/N$ $\to$ chyba klesá ako $1/\sqrt{N}$ (priemerovanie potláča šum).
4. Alternatívne odhadce: medián (robustný voči odľahlým hodnotám), geometrický priemer
   (multiplikatívne dáta); porovnanie rozptylu cez opakované pokusy / krabicové grafy.
5. Pri Gaussovom šume je priemer odhadom **maximálnej vierohodnosti**.
6. Interval spoľahlivosti odhadu; viac dát $\to$ užší interval.

### Téma 3 — Lineárna regresia  *(→ Časť C)*
1. Model **lineárny v parametroch**: $y = X p + e$ (príznaky môžu byť nelineárne
   v dátach: $\sqrt{h}$, $T^2$, $1/T$).
2. Regresná matica $X$; stĺpec absolútneho člena (posunu).
3. Metóda najmenších štvorcov: minimalizovať $\|X p - y\|^2$ $\to$ **normálne rovnice**
   $p = (X^T X)^{-1} X^T y$ = `X\y` (interne cez QR).
4. **Gauss–Markovove predpoklady** $\to$ MNŠ je najlepší lineárny nestranný odhadca (BLUE).
5. Kvalita: **RMSE**, paritný graf, intervaly spoľahlivosti parametrov.
6. Rozširuje sa na multivariátny prípad (mnoho vstupov).

### Téma 4 — Praktické aspekty lineárnej regresie  *(→ Časti C7, D, E)*
1. **Štandardizácia** (nulový priemer, jednotkový rozptyl): porovnateľné škály + lepšia
   podmienenosť $X^T X$.
2. **Korelácia vs. kovariancia**; korelácia $\in [-1, 1]$.
3. **Multikolinearita**: korelované vstupy robia $X^T X$ blízko singulárnou $\to$ nestabilné
   koeficienty $\to$ odstrániť redundantné príznaky (výber príznakov).
4. **Analýza hlavných komponentov (PCA)** na dekoreláciu / redukciu dimenzie (pravidlo lakťa).
5. **Trénovacie vs. testovacie** dáta; preučenie/podučenie; výber rádu/štruktúry modelu.
6. Odľahlé hodnoty a čistenie dát.

### Téma 5 — Filtrácia dynamických signálov  *(→ Časť F)*
1. Prečo filtrovať: oddeliť užitočný signál od šumu podľa **frekvenčného obsahu**.
2. **Dolnopriepustný filter** (zachová pomalý trend), **hornopriepustný filter** (zachová rýchlu zložku), pásmový filter;
   medzná frekvencia.
3. **Kĺzavý priemer** = FIR dolnopriepustný filter; veľkosť okna určuje mieru vyhladzovania.
4. **Kauzálny** (`filter`, vnáša oneskorenie) vs. **s nulovou fázou** (`filtfilt`, bez fázového posunu).
5. Kompromis: väčšie vyhladzovanie odstraňuje šum, ale aj ničí skutočnú dynamiku.

### Téma 6 — Modelovanie dynamických systémov  *(→ Časť G)*
1. Dynamický vs. statický: výstup má **pamäť** (závisí od minulosti).
2. **Impulzná odozva** a **konvolúcia** $y(t) = \int g(\tau)\,u(t-\tau)\,d\tau$.
3. Diskrétne modely: **FIR** $y_k = \sum b_i u_{k-i}$ (všetky nuly, vždy stabilný, vysoký rád).
4. **ARX** $y_k = -\sum a_i y_{k-i} + \sum b_i u_{k-i}$ (póly+nuly, málo parametrov).
5. **ARMAX** = ARX + člen kĺzavého priemeru na minulých **chybách** (modeluje poruchy).
6. ARX aj FIR sú **lineárne v parametroch** $\to$ metóda najmenších štvorcov (regresná matica z oneskorení).
7. **Prenosová funkcia** v $z^{-1}$ (jednotkové oneskorenie); porovnanie FIR vs. ARX; stabilita.

### Téma 7 — Rekurzívna identifikácia  *(→ Časť R)*
1. Dávková vs. **rekurzívna**: aktualizácia odhadu pri každej novej vzorke (online / v reálnom čase).
2. **Štruktúra RLS**: $\theta_k = \theta_{k-1} + K_k (y_k - \phi_k^T \theta_{k-1})$
   = starý odhad + zisk × inovácia.
3. Kovariancia $P$ a zisk $K$ (= Kalmanov zisk); inicializácia ($P_0$ veľké).
4. **Faktor zabúdania $\lambda$**: $1$ = štandardný RLS (= dávková MNŠ); $<1$ sleduje
   časovo premenné parametre (kompromis sledovanie vs. šum).
5. RLS je špeciálny prípad **Kalmanovho filtra**.
6. Najjednoduchší špeciálny prípad: **aktualizácia posunu** (prispôsobenie iba offsetu $b$
   podľa chyby predikcie, voliteľne filtrovaného faktorom dôvery $\delta$).

### Téma 8 — Praktické aspekty identifikácie  *(→ Časti G6, H, E)*
1. **Návrh experimentu / vstupného signálu**: potreba **perzistentného buzenia** (bohaté spektrum).
2. Typy vstupov: skok (málo frekvencií) → náhodný → **PRBS** (blízky bielemu šumu, preferovaný).
3. Výber **periódy vzorkovania** (predchádzanie aliasingu / tuhosti).
4. **Výber rádu modelu** z **ACF/PACF** výstupu.
5. **Validácia**: trénovacie vs. testovacie RMSE, predikcia o jeden krok dopredu vs. voľná simulácia,
   kontrola reziduí; preučenie.
6. Skutočný postup (Flexy², Zadanie 2): čistenie → štandardizácia → rozdelenie → FIR/ARX →
   porovnanie.

---

## Časť A — Základy

### A1. Čo je identifikácia systémov?
Zostavenie **matematického modelu** systému z **nameraných vstupno-výstupných
dát** namiesto z fyzikálnych princípov. Zvolíme *štruktúru modelu*
(triedu rovníc) a následne *odhadneme jeho parametre* tak, aby model reprodukoval
dáta. Je to dátami riadené (empirické / čierna skrinka) modelovanie — protiklad
bieleho boxu (fyzikálneho) modelovania. Sivá skrinka kombinuje oba prístupy.

### A2. Čierna skrinka vs. sivá skrinka vs. biela skrinka?
Tieto tri sa líšia tým, **koľko vnútorných vedomostí o systéme máte/použijete** —
spektrum od „žiadne" až po „úplné":

- **Biela skrinka** (úplná vnútorná znalosť): model odvodený z fyzikálnych zákonov
  (bilancia hmotnosti/energie, zachovanie); štruktúra *aj* parametre majú fyzikálny
  zmysel. *Najväčší vhľad, najväčšie úsilie/odbornosť.*
- **Čierna skrinka** (žiadna vnútorná znalosť): štruktúra zvolená len pre pohodlnosť
  (FIR, ARX); parametre sú len fitované čísla bez fyzikálneho zmyslu — vidíme
  len vstupy a výstupy. *Najrýchlejší prístup, ale žiadny fyzikálny vhľad; nevieme vysvetliť
  *prečo* to funguje.*
- **Sivá skrinka** (čiastočná vnútorná znalosť): známa štruktúra z fyziky s
  neznámymi parametrami fitovanými na dáta — vyvážený hybrid kombinujúci oba prístupy.

**Analógia s predajným automatom:**
- *Čierna skrinka* = **používateľ** automatu: vhodí peniaze, dostane nápoj, netuší
  ako funguje vnútorný mechanizmus.
- *Biela skrinka* = **technik**: preskúma každú vnútornú súčiastku, aby pochopil,
  ako každá časť prispieva.
- *Sivá skrinka* = **operátor**: pozná základné mechanické princípy, ale nie každý detail.

| Aspekt | Biela skrinka | Sivá skrinka | Čierna skrinka |
|--------|---------------|--------------|----------------|
| Vnútorná znalosť | Úplná | Čiastočná | Žiadna |
| Parametre | Fyzikálne | Zmiešané | Len fitované |
| Úsilie / odbornosť | Vysoké | Stredné | Nízke |
| Fyzikálny vhľad | Úplný | Čiastočný | Žiadny |
| Príklady z kurzu | Fyzikálne modely nádrže/plynu | Známa štruktúra + MNŠ | FIR, ARX |

*Poznámka:* rovnaká terminológia biela/čierna/sivá skrinka sa používa aj pri **testovaní softvéru**
(testovanie bez znalosti kódu vs. prehliadanie zdrojového kódu vs. čiastočný prístup) —
základná myšlienka je rovnaká: **miera vnútornej viditeľnosti do skúmaného objektu.** Pri *identifikácii* opisuje **model**; pri testovaní opisuje **testovaný kód**.

### A3. Všeobecný postup identifikácie (kroky)?
1. Navrhnúť experiment a zbierať dáta (zvoliť vstupný signál).
2. Preskúmať / vizualizovať / vyčistiť dáta.
3. Zvoliť štruktúru modelu (statický/dynamický, FIR/ARX, rád).
4. Odhadnúť parametre (metóda najmenších štvorcov).
5. Validovať model (RMSE na nezávislých testovacích dátach, kontrola reziduí).
6. Ak nie je výsledok uspokojivý, revidovať štruktúru/rád a opakovať.

### A4. Statický vs. dynamický model?
- **Statický:** výstup závisí len od *aktuálneho* vstupu — $y = f(u)$
  (napr. nádrž $q = k\sqrt{h}$, plynová nádrž $V = f(T)$). Bez pamäti.
- **Dynamický:** výstup závisí od *minulých* vstupov a/alebo výstupov — má pamäť /
  časový vývoj (FIR, ARX). Potrebný, keď má systém zotrvačnosť/oneskorenie.

---

## Časť B — Štatistika a dáta

### B1. Priemer, rozptyl, smerodajná odchýlka — definície?
- Priemer (stredná hodnota): $\mu = \frac{1}{N}\sum_{i} x_i$.
- Výberový rozptyl: $\sigma^2 = \frac{1}{N-1}\sum_{i}(x_i - \mu)^2$.
- Smerodajná odchýlka: $\sigma = \sqrt{\sigma^2}$, rovnaké jednotky ako dáta; rozptyl okolo priemeru.
- **Menovateľ $N-1$** (Besselova korekcia) robí výberový rozptyl *nestranným*
  odhadom skutočného rozptylu.

### B2. Hustota pravdepodobnosti (PDF) vs. distribučná funkcia (CDF)?
- **PDF** $f(x)$: hustota pravdepodobnosti; plocha pod ňou na nejakom intervale =
  pravdepodobnosť, že sa hodnota nachádza na tom intervale; integrál = 1.
- **CDF** $F(x) = P(X \le x)$: monotónne rastúca od 0 do 1; je to integrál hustoty pravdepodobnosti.
- **Kvantil / inverzná CDF** odpovedá na otázku „ktoré $x$ má kumulatívnu pravdepodobnosť $p$".

### B3. Normálne (Gaussovo) rozdelenie — prečo je dôležité?
Definované pomocou $\mu$ a $\sigma$. Asi 68 % dát leží v rozsahu $\pm 1\sigma$, 95 % v rozsahu
$\pm 2\sigma$, 99,7 % v rozsahu $\pm 3\sigma$. Merací šum sa bežne predpokladá
Gaussov, čo je práve to, čo robí **metódu najmenších štvorcov** štatisticky optimálnym
(odhadom maximálnej vierohodnosti) odhadcom.

### B4. Zákon veľkých čísel (videný na seminári 2)?
S rastúcim rozsahom výberu empirický histogram konverguje k skutočnej hustote pravdepodobnosti a
výberový priemer konverguje k skutočnému priemeru. Viac dát → spoľahlivejšia štatistika.

### B5. Priemer vs. medián vs. geometrický priemer — kedy ktorý použiť? (Seminár 4)
- **Aritmetický priemer:** najlepší pre symetrický šum; citlivý na odľahlé hodnoty.
- **Medián:** robustný voči odľahlým hodnotám / asymetrii.
- **Geometrický priemer:** pre multiplikatívne / log-normálne dáta (napr. miery rastu).
Krabicový graf porovnáva ich rozptyl v opakovaných odhadoch.

---

## Časť EC — Odhad konštanty (Téma skúšky 2 / Prednášky L03–L04)

### EC1. Čo je „odhad konštanty"?
Najjednoduchší identifikačný problém: odhadnúť jednu neznámu skutočnú hodnotu $c$
z $N$ zašumených meraní $y_i = c + e_i$, kde $e_i$ je merací šum
(s nulovým priemerom). Je to jednoparametrický špeciálny prípad lineárnej regresie s
regresnou maticou $X = \mathbf{1}_{N}$ (stĺpec jednotiek).

### EC2. Ukažte, že odhad konštanty metódou najmenších štvorcov je priemer.
Minimalizujeme $J(c) = \sum_{i}(y_i - c)^2$. Položíme deriváciu rovnú nule:

$$
\frac{dJ}{dc} = -2\sum_{i}(y_i - c) = 0 \quad\Longrightarrow\quad
\sum_{i} y_i = N c \quad\Longrightarrow\quad \hat{c} = \frac{1}{N}\sum_{i} y_i .
$$

Odhad metódou MNŠ konštanty **je presne aritmetický priemer** — v súlade
s `X\y`, keď $X = \mathbf{1}_{N}$.

### EC3. Vlastnosti odhadcu priemeru?
- **Nestranný:** $E[\hat{c}] = c$ (v priemere správny).
- **Rozptyl:** $\mathrm{var}(\hat{c}) = \sigma^2/N$ — klesá s viac dátami.
- **Konzistentný:** pre $N \to \infty$ platí $\hat{c} \to c$ (rozptyl $\to 0$).
- **Štandardná chyba** $= \sigma/\sqrt{N}$: na znásobenie chyby dvakrát treba **4× viac
  dát** (zákon $\sqrt{N}$). Preto priemery opakovaných meraní potláčajú šum.
- Pri **Gaussovom** šume je priemer aj odhadom **maximálnej vierohodnosti**.

### EC4. Kedy je priemer zlý odhadca — a čo použiť namiesto neho?
- Pri **odľahlých hodnotách / asymetrii** použite **medián** (robustný — niekoľko zlých bodov
  ho takmer neovplyvní).
- Pri **multiplikatívnych / log-normálnych** dátach (pomery, miery rastu) použite
  **geometrický priemer**.

Porovnanie troch odhadcov v mnohých opakovaných pokusoch (krabicové grafy) ukazuje, že
priemer má najmenší rozptyl pre čistý Gaussov šum, medián najväčšiu odolnosť voči odľahlým hodnotám
(Seminár 4, konštanta nádrže $k_{11}$).

### EC5. Interval spoľahlivosti odhadu?
$\hat{c} \pm t\cdot\hat{\sigma}/\sqrt{N}$ ($t$ z Studentovho/normálneho
rozdelenia pre zvolenú spoľahlivosť, napr. 95 %). Viac meraní → užší
interval. Kvantifikuje, nakoľko možno odhadu dôverovať.

---

## Časť C — Metóda najmenších štvorcov a regresia

### C1. Sformulujte problém metódy najmenších štvorcov.
Daná regresná matica $X$ (riadky = merania, stĺpce = príznaky) a výstupy
$y$, nájdeme parametre $p$ minimalizujúce súčet štvorcov reziduí
$\min_{p}\|X p - y\|^2$. Riešenie = **normálne rovnice**:

$$
p = (X^T X)^{-1} X^T y .
$$

MATLAB to počíta ako `X\y` — interne pomocou QR faktorizácie, nie výpočtom
$X^T X$, čo je numericky stabilnejšie (rovnaký výsledok, lepší algoritmus).

### C2. Prečo štvorcové chyby (nie absolútne)?
- Diferencovateľné → uzavretá lineárna forma riešenia.
- Viac penalizuje veľké chyby.
- Odhad maximálnej vierohodnosti pri Gaussovom šume.

(Absolútna chyba → robustná regresia, ale bez uzavrenej formy.)

### C2b. Kedy je metóda najmenších štvorcov *najlepší* odhadca? (Gauss–Markov)
Za **Gauss–Markovových predpokladov** je odhad MNŠ **najlepší lineárny nestranný odhadca (BLUE)** —
minimálny rozptyl spomedzi všetkých lineárnych nestranných odhadcov:
1. Model je **lineárny v parametroch** a správne špecifikovaný.
2. Šum má **nulový priemer** ($E[e] = 0$).
3. Šum je **homoskedastický** (konštantný rozptyl).
4. Šum je **nekorelovaný** naprieč meraniami.

(Ak je navyše šum **Gaussov**, MNŠ = maximálna vierohodnosť.) Keď tieto predpoklady
nie sú splnené — napr. korelovaný šum v dynamických dátach — prostá MNŠ sa stáva
zaujatou/suboptimálnou, čo motivuje metódy nad rámec ARX.

### C3. Čo je regresná matica?
Matica, ktorej stĺpce sú bázové funkcie modelu vyhodnotené v každom dátovom
bode. Model musí byť **lineárny v parametroch**, aby sa dalo použiť `X\y` — všimnite si,
že *samotné príznaky* môžu byť nelineárne ($\sqrt{h}$, $T^2$, $1/T$); lineárna
musí byť iba závislosť na parametroch.

### C4. Úloha absolútneho člena (posunu)?
Stĺpec `ones(size(...))` umožňuje fitu mať nenulový offset
($y = p_1 x + p_0$). Jeho vynechanie núti priamku prechádzať cez počiatok (používa sa pre
$q = k\sqrt{h}$, čo musí byť 0 keď $h = 0$).

### C5. RMSE — čo to je a prečo sa používa?

$$
\mathrm{RMSE} = \sqrt{\tfrac{1}{N}\sum_{k}(\hat{y}_k - y_k)^2} .
$$

Priemerná chyba predikcie v **rovnakých jednotkách ako $y$**; rovná sa smerodajnej
odchýlke reziduí, keď ich priemer je $\approx 0$ (platí pre MNŠ s absolútnym členom). Nižšia = lepšia. Používa sa na porovnanie konkurenčných modelov.

### C6. Paritný graf — čo ukazuje?
Predikovaná hodnota oproti nameranej s referenčnou priamkou 45°. Body na uhlopriečke = dokonalé
predikcie; systematická odchýlka odhalí posun alebo chybu štruktúry modelu.

### C7. Prečo štandardizovať dáta? (nulový priemer, jednotková smerodajná odchýlka)
- Stavia premenné rôznych jednotiek/škál na rovnaký základ.
- Zlepšuje numerickú podmienenosť $X^T X$.
- Robí regresné koeficienty porovnateľnými z hľadiska dôležitosti.
- Potrebné pred koreláciou/PCA, aby premenné s veľkou hodnotou neprevládali.

Vzorec: $x_s = (x - \mu)/\sigma$. Konštantný signál sa nedá štandardizovať
($\sigma = 0$).

---

## Časť D — Korelácia, kovariancia, PCA

### D1. Kovariancia vs. korelácia?
- **Kovariancia** $\mathrm{cov}(x,y)$: spoločná variabilita, jednotky =
  jednotky($x$)·jednotky($y$), neohraničená.
- **Korelácia** (Pearsonove $r$): kovariancia normalizovaná dvoma smerodajnými odchýlkami →
  bezrozmerná, v rozsahu **$[-1, 1]$**. $r = +1$ dokonalá kladná lineárna, $-1$ dokonalá
  záporná, $0$ žiadna *lineárna* závislosť.
- Korelácia je len kovariancia **štandardizovaných** premenných.

### D2. „Korelácia neznamená príčinnosť" — relevancia?
Dve premenné sa môžu pohybovať spoločne z dôvodu spoločnej príčiny alebo náhody. Pri
identifikácii to má vplyv na **výber vstupov**: silne korelovaný vstup nemusí byť nutne *príčinným faktorom* výstupu.

### D3. Čo je multikolinearita a prečo odstrániť korelované vstupy? (Semináre 6/7)
Ak sú dva stĺpce regresnej matice silne korelované, $X^T X$ sa stáva blízko singulárnou →
nestabilné, veľké, nespoľahlivé koeficienty. Odstrániť redundantné (lineárne
závislé) vstupy dáva lepšie podmienený, zovšeobecniteľnejší model. Toto je
krok „výberu príznakov".

### D4. Čo je PCA a na čo slúži?
**Analýza hlavných komponentov** rotuje dáta na ortogonálne smery
(vlastné vektory kovarianční matice) zoradené podľa vysvetleného rozptylu
(vlastné čísla). Využitia: redukcia dimenzie, dekorelácia, vizualizácia.
Prvý hlavný komponent je smer maximálneho rozptylu.

### D5. Geometrický zmysel vlastných vektorov kovariancie?
Sú to **osi elipsy rozptylu dát**; vlastné čísla = rozptyl pozdĺž
každej osi (poloosi elipsy $\propto \sqrt{\text{vlastné číslo}}$). Kreslenie
$1\sigma/2\sigma/3\sigma$ elíps vizualizuje kovarianční štruktúru.

### D6. Ako vybrať počet hlavných komponentov?
Vykresliť kumulatívny/vysvetlený rozptyl oproti indexu hlavného komponentu a nájsť **lakeť (koleno)** —
bod klesajúcich výnosov — zachovať hlavné komponenty do tohto bodu.

### D7. Elipsa spoľahlivosti parametrov a „interval obsahuje nulu" (L07)?
Kovariancia parametrov je $V_p = \sigma^2 (X^T X)^{-1}$ (rozptyl šumu ×
inverzná informácia). S predpokladom $p \sim \mathcal{N}(\hat{p}, V_p)$, kvadratická
forma $(p-\hat{p})^T V_p^{-1}(p-\hat{p})$ sleduje **chi-kvadrát** rozdelenie s $n_p$
stupňami voľnosti, takže jej množina úrovní $\le \chi^2_{n_p,\alpha}$ je
**elipsa spoľahlivosti** — multivariátna generalizácia skalárneho intervalu.
Dĺžky poloosí vychádzajú z intervalov spoľahlivosti parametrov; mimidiagonálne členy nakláňajú
elipsu. Praktický test: ak interval spoľahlivosti parametra **obsahuje nulu**
(napr. $[-1, 2]$ pri 95 %), model môže fungovať **bez** tohto parametra — môže
byť nepozorovateľný (kolinearita), nedostatočne budený, alebo jednoducho nekausálny. Čistý spôsob
orezania preučených členov.

---

## Časť E — Trénovanie/testovanie a kvalita modelu

### E1. Prečo rozdeliť dáta na trénovaciu a testovaciu množinu?
Trénovanie odhaduje parametre; testovanie poskytuje **poctivý, nestranný** odhad
predikčnej presnosti na dátach, ktoré model nikdy nevidel. Posudzovanie presnosti len na
trénovacích dátach je prílišne optimistické.

### E2. Preučenie vs. podučenie?
- **Preučenie:** model príliš zložitý (príliš veľa parametrov/príliš vysoký rád) — fituje šum;
  nízke trénovacie RMSE, ale vysoké testovacie RMSE.
- **Podučenie:** model príliš jednoduchý — vysoká chyba všade.

Cieľom je rád, ktorý minimalizuje **testovacie** RMSE (kompromis rozptyl–posun).

### E3. Ako súvisí rád modelu s preučením/podučením?
Zvyšovanie rádu vždy znižuje *trénovaciu* chybu, ale nakoniec zvyšuje *testovaciu*
chybu. Zvoliť najmenší rád, ktorý zachytí dynamiku (parsimónia /
Occamova britva).

---

## Časť F — Signály a filtrácia

### F1. Dolnopriepustný vs. hornopriepustný filter?
- **Dolnopriepustný filter** zachová pomalé zložky (trend), odstraňuje rýchly šum → vyhladzovanie.
- **Hornopriepustný filter** zachová rýchle zložky (šum/hrany), odstraňuje pomalý trend.

Medzná (normalizovaná) frekvencia určuje hranicu.

### F2. Filter kĺzavého priemeru — čo to je?
FIR filter s rovnakými váhami $1/n$; priemery posledných $n$ vzoriek. Väčšie $n$
→ hladšie, ale väčšie oneskorenie a väčšie skreslenie na okrajoch. Je to doslova dolnopriepustný
filter.

### F3. Kauzálny filter vs. filter s nulovou fázou?
- **Kauzálny** (`filter`) používa len minulé vzorky → vnáša **časové oneskorenie**.
- **S nulovou fázou** (`filtfilt`, dopredu+dozadu) odstraňuje oneskorenie → výstup
  zarovnaný v čase. Používa sa na zostavenie *vyhladzeného testovacieho výstupu* v Zadaní 2,
  aby zostal časovo zarovnaný so vstupom.

### F4. Prečo filtrovať / vyhladzovať pred identifikáciou?
Šum narúša odhady parametrov; vyhladzovanie poskytuje čistejší referenčný výstup.
Nadmerné vyhladzovanie však ničí skutočnú dynamiku — kompromis.

---

## Časť G — Dynamická identifikácia (jadro)

### G1. Čo opisuje konvolúcia? (Seminár 9)
Výstup lineárneho časovo invariantného systému je konvolúcia jeho **impulznej
odozvy** $g(t)$ so vstupom:

$$
y(t) = \int_0^{t} g(\tau)\,u(t-\tau)\,d\tau .
$$

V diskrétnom čase sa toto stáva váženou sumou minulých vstupov — základ modelu FIR.

### G2. Definujte model FIR a jeho zmysel.
**Finite Impulse Response (konečná impulzná odozva):** $y_k = \sum_{i=1}^{m} b_i\,u_{k-i}$. Výstup je
vážená suma posledných $m$ vstupov; váhy $b_i$ *sú* (vzorkovanou)
impulznou odozvou. Bez spätnej väzby → vždy stabilný. Zapísané ako $X p = y$ a riešené
metódou najmenších štvorcov; $X$ je (dolno-trojuholníková, posunutá) matica minulých vstupov.

### G3. Definujte model ARX.
**Auto-Regressive with eXogenous input (autoregresívny s exogénnym vstupom):**

$$
y_k = -\sum_{i=1}^{n} a_i\,y_{k-i} + \sum_{i=1}^{m} b_i\,u_{k-i} .
$$

Výstup závisí od minulých **výstupov** (AR časť, $a$) a minulých **vstupov** (exogénna časť, $b$). Prenosová funkcia v $z$:

$$
G(z^{-1}) = \frac{\sum_i b_i z^{-i}}{1 + \sum_i a_i z^{-i}} .
$$

Stále **lineárny v parametroch** → metóda najmenších štvorcov. $n$ = rád výstupu, $m$ = rád vstupu,
pričom $n \ge m$.

### G4. FIR vs. ARX — porovnanie.
| | FIR | ARX |
|---|---|---|
| Používa minulé výstupy | Nie | Áno (spätná väzba) |
| Štruktúra | Všetky nuly (len čitateľ) | Póly + nuly |
| Stabilita | Vždy stabilný | Môže byť nestabilný (póly) |
| Počet potrebných parametrov | Veľa (vysoký rád ~50) | Málo |
| Zachytáva pomalé doznievanie | Potrebuje dlhý chvost | Implicitne cez póly |
| Typická presnosť | Nižšia | Vyššia (menej parametrov, nižšie RMSE) |

ARX je *parsimoniálnejší*: spätná väzba modeluje doznievanie impulznej odozvy niekoľkými
pólmi, zatiaľ čo FIR musí vypísať celý chvost.

### G5. Prečo FIR potrebuje tak vysoký rád (napr. 50)?
Nemá rekurziu, takže každá vzorka impulznej odozvy potrebuje vlastný koeficient.
Systém, ktorého odozva doznievava pomaly, potrebuje veľa členov $b$ na reprezentáciu
„pamäte". ARX dosahuje rovnakú pamäť lacno cez rekurzívne členy $a_i y_{k-i}$.

**Kvantitatívna verzia (dobrý bod na tabuľu):** FIR rádu $m$ si pamätá len
posledných $m$ vzoriek — **pamäťové okno $\tau = m\cdot T_s$**. To musí pokryť
**čas ustálenia** systému. Príklad (Zadanie 2): $m = 50$, $T_s = 0{,}02$ s $\to$
$\tau = 1$ s pamäte; ak sa systém ustáľuje pomalšie, FIR je podučený.
Zvyšovanie $m$ až na ~1000 takmer nezníži RMSE — dôkaz, že pridávanie FIR koeficientov
je neefektívna náhrada spätnej väzby ARX.

### G6. Ako vybrať rády ARX $n$ a $m$? (ACF/PACF)
- **ACF** (autokorelačná funkcia): ako výstup koreluje so svojou vlastnou minulosťou →
  indikuje celkovú pamäť / správanie MA ($b$).
- **PACF** (parciálna autokorelačná funkcia): korelácia pri danom oneskorení s odstránenými
  medziľahlými oneskoreniami → oneskorenie, po ktorom PACF klesne do pásma spoľahlivosti, dáva
  **AR rád $n$**. Zvoliť $m \le n$, aby sa predišlo preučeniu.

### G7. Čo je Z-transformácia / operátor $z^{-1}$?
$z^{-1}$ je operátor **jednotkového (jednvzorkovacieho) oneskorenia**: $z^{-1} y_k = y_{k-1}$. Mení
diferenčné rovnice na algebraické prenosové funkcie $G(z^{-1}) = Y/U$.
$z^{-n_k}$ predstavuje čisté **časové oneskorenie vstupu** o $n_k$ vzoriek.

### G7b. Čo je model ARMAX a kedy ho potrebujeme?
**Auto-Regressive Moving Average with eXogenous input** — ARX plus
člen kĺzavého priemeru na minulých **chybách predikcie**:

$$
y_k = -\sum_i a_i\,y_{k-i} + \sum_i b_i\,u_{k-i} + \sum_i c_i\,e_{k-i} .
$$

Tri časti: AR (minulé výstupy, $a$), exogénny vstup (minulé vstupy, $b$) a
nová MA časť (minulé chyby $e_{k-i}$, váhy $c$). Prečo pomáha: prostý ARX/FIR
**ignoruje poruchy** (netesniaci ventil, zmenená kvalita suroviny). MA člen
umožňuje koeficientom $c$ **absorbovať systematické chyby poruchy**, čím oslobodzuje
$a$ a $b$ na naučenie sa *skutočnej* dynamiky zariadenia. Na rozdiel od jednorazovo natrénovaného ARX, ARMAX
**sám sa opravuje online** (kĺzavý priemer nedávnych chýb). Cena: zvyčajne
vyžaduje **nelineárnu optimalizáciu** na fitovanie; na predikciu dopredu (budúce $e_k$ neznáme)
predpokladáme, že $e_k$ je Gaussov šum s nulovým priemerom a zostavujeme scenáre poruchy $\pm\sigma$.

### G8. Predikcia o jeden krok dopredu vs. simulácia?
- **O jeden krok dopredu (OSA):** predikuje $y_k$ pomocou *nameraných* minulých výstupov $y_{k-i}$
  (regresná matica používa skutočné dáta) — čo počíta `Phi*theta`.
- **Simulácia (voľný beh):** model spätne dostáva vlastné minulé predikcie; zadaný je len
  vstup (`lsim`/`sim`). Simulácia je náročnejší, poctivejší test.
- **Prečo na tom záleží pri porovnávaní modelov:** OSA vyzerá vždy lepšie ako
  simulácia (dostáva skutočný nedávny výstup zadarmo). Veľmi nízke ARX *testovacie*
  RMSE (napr. 0,02 v Zadaní 2) čiastočne odráža OSA na vyhladených dátach. Na férové
  porovnanie FIR a ARX vyhodnoťte **oba rovnakým spôsobom** — inak ARX-cez-OSA vs. FIR-cez-simuláciu zvýhodňuje ARX.

---

## Časť R — Rekurzívna identifikácia (Prednáška L11)

### R1. Čo je rekurzívna identifikácia a prečo sa používa?
Aktualizácia odhadu parametrov **vzorku po vzorke** pri príchode nových dát, namiesto
opakovaného riešenia plnej dávkovej metódy najmenších štvorcov. Motivácia:
- **Online / v reálnom čase** identifikácia (adaptívne riadenie).
- **Časovo premenné systémy** — sledovanie parametrov, ktoré sa menia.
- **Pamäť/výpočet** — nie je potrebné uchovávať ani znova spracovávať všetky minulé dáta.

### R2. Sformulujte aktualizáciu rekurzívnej metódy najmenších štvorcov (RLS) slovne.
Pre každú novú vzorku: vypočítame **chybu predikcie (inováciu)**
$e_k = y_k - \phi_k^T \theta_{k-1}$ (namerané mínus predikované), potom opravíme
odhad $\theta_k = \theta_{k-1} + K_k e_k$, kde **zisk** $K_k$ vychádza z
aktuálnej kovariancia $P$. Nakoniec aktualizujeme $P$. Štruktúra = **„starý odhad +
zisk × chyba predikcie."**

Vzorce:

$$
\begin{aligned}
K_k &= \frac{P_{k-1}\,\phi_k}{\lambda + \phi_k^T P_{k-1}\,\phi_k} \\[4pt]
\theta_k &= \theta_{k-1} + K_k\,(y_k - \phi_k^T \theta_{k-1}) \\[4pt]
P_k &= \frac{1}{\lambda}\bigl(P_{k-1} - K_k\,\phi_k^T P_{k-1}\bigr)
\end{aligned}
$$

### R3. Čo je faktor zabúdania $\lambda$?
Váha $\lambda \in (0, 1]$, ktorá exponenciálne diskontuje staršie dáta.
- $\lambda = 1$: štandardný RLS — všetky dáta sú rovnako vážené; konverguje k
  **rovnakému výsledku ako dávková MNŠ**.
- $\lambda < 1$ (typicky 0,95–0,99): staré dáta sú „zabudnuté" → odhadca môže
  **sledovať časovo premenné parametre**. Menšie $\lambda$ = rýchlejšie sledovanie, ale
  väčší šum (rozptyl ↑).

Toto je kompromis posun–rozptyl / sledovanie–šum.

### R4. Čo je matica $P$ a zisk $K$?
- $P$ = **kovariancia odhadu parametrov** (úmerná $(X^T X)^{-1}$);
  klesá, keď viac dát buduje dôveru. Inicializovaná veľko (napr. $10^6 I$), aby
  signalizovala nízku počiatočnú dôveru a umožnila rýchlu konvergenciu.
- $K$ = **zisk** (Kalmanov zisk): škáluje, nakoľko najnovšia chyba predikcie
  opravuje odhad. Veľký keď sme neistí, malý keď sme istí.

### R5. Vzťah RLS k dávkovej metóde najmenších štvorcov a Kalmanovmu filtru?
- S $\lambda = 1$, RLS po $N$ vzorkách = dávková MNŠ `X\y` presne — rovnaký
  výsledok, vypočítaný inkrementálne.
- RLS je **špeciálnym prípadom Kalmanovho filtra** (odhad konštantných parametrov
  namiesto pohybujúceho sa stavu); zisk $K$ je Kalmanov zisk.

### R6. Čo je „inovácia"?
$e_k = y_k - \phi_k^T \theta_{k-1}$ — časť novej vzorky **nepredikovaná**
aktuálnym modelom, t.j. skutočne nová informácia. RLS posúva odhad v pomere k nej.

### R7. Aktualizácia posunu — najjednoduchšia rekurzívna schéma (L11).
Ak nasadený model vykazuje takmer **konštantnú systematickú chybu** (napr. zmenená
surovina/dodávateľ, mierna nelinearita), ale **smernice sú stále správne**, prispôsobíme
len **offset $b$**, nie overené smernice — priemysel to preferuje.
Aktualizácia podľa chyby predikcie: $b_k = b_{k-1} + (y_{k-1} - \hat{y}_{k-1})$.
Reagovanie na jeden bod je krátkozraké, preto ho filtrujeme faktorom dôvery
$\delta \in [0,1]$:

$$
b_k = \delta\,b_{k-1} + (1-\delta)\,(\text{nový posun}) .
$$

$\delta \to 1$ = nedôverovať meraniam (pomalý drift k novému pracovnému bodu);
$\delta = 0$ = nasledovať posledný bod úplne. Rovnaký tvar ako P regulátor
(odhad ← odhad + zisk × chyba); skalárna verzia pre smernici (RLS s $b = 0$)
je $a_N = a_{N-1} + \frac{x_N}{\sum_k x_k^2}(y_N - a_{N-1}x_N)$, ktorej zisk sa automaticky zmenšuje
s akumuláciou dát — pridať **okno zabúdania** na zachovanie adaptácie.

---

## Časť H — Návrh experimentu

### H1. Čo robí identifikačný vstupný signál dobrým?
Musí byť **perzistentne budiaci** — dostatočne bohatý vo frekvenciách, aby vzbudil všetky
módy systému. Konštanta alebo jediný skok odhalí málo; potrebná je varieta v
amplitúde a frekvencii.

### H2. Porovnajte skok, náhodný a PRBS vstup. (Semináre 9–11)
- **Skok / schodový priebeh:** jednoduchý, ukazuje zosilnenie a časové konštanty, ale buzí málo
  frekvencií.
- **Náhodné rovnomerné úrovne:** široké budenie, ale výkon rozložený nerovnomerne.
- **PRBS (pseudonáhodná binárna sekvencia):** prepína medzi dvomi úrovňami
  pseudonáhodne; blízko biele spektrum, optimálny výkon, **reprodukovateľný** → preferovaný vstup pri dynamickej identifikácii.

### H3. Perióda vzorkovania $T_s$ — prečo je dôležitá?
Príliš veľká → aliasing, zmeškanie rýchlej dynamiky; príliš malá → numericky stiff,
dominancia šumu, obrovské množstvo dát. Mala by rozlišovať dominantnú časovú konštantu systému
(pravidlo palca: niekoľko vzoriek na časovú konštantu).

### H4. Aká je úloha `rng(100)`?
Fixuje náhodné semeno, aby simulácie s náhodným vstupom/šumom boli
**reprodukovateľné** — nevyhnutné na porovnávanie výsledkov a hodnotenie.

### H5. Prečo odstrániť „zlé" úseky dát pred identifikáciou?
Metóda najmenších štvorcov predpokladá **konzistentný vzťah vstup→výstup naprieč celým
záznamom**. Úseky, kde to nie je splnené — napr. nulový štart, kde je vstup aktívny,
ale výstup ešte nereagoval, alebo nasýtená/nulová oblasť senzora na konci — vkladajú
**štrukturálny posun do regresnej matice**: model je nútený vysvetľovať výstup, ktorý vstup nespôsobil.
Výsledok: horší fit, vyššie RMSE. Orezanie týchto nepredstaviteľných regiónov (zachovanie len čistého,
vstupom riadeného správania) je dôvodom, prečo čistenie dát prichádza pred fitovaním modelu.

### H6. Ako overiť, že štandardizácia nenarušila dáta?
Vykresliť štandardizovanú hodnotu oproti pôvodnej hodnote — musí to byť **priamka**
(štandardizácia je čisto *lineárna* mapa $(x-\mu)/\sigma$). Priamka potvrdzuje, že nebolo zavedené žiadne nelineárne skreslenie; numericky skontrolovať
$\mathrm{mean} \approx 0$, $\mathrm{std} \approx 1$.

### H7. Statický vs. dynamický model a kontrola linearity (L10)?
Naplánujte skokové zmeny, napr. $\tfrac13, \tfrac23, 1$ a prečítajte **ustálené**
výstupy:
- **Proporcionálne** výstupy → postačuje **statické zosilnenie** (nie je potrebný dynamický model).
- **Neproporcionálne, ale rovnaké znamienko** zosilnenia → nelineárne, ale **zvládnuteľné** (integrálne
  riadenie to zvládne).
- **Zosilnenie, ktoré mení znamienko** → **červená výstraha**: silne nelineárne, v podstate
  neriaditeľné lineárnym regulátorom (ani LQR zlyhá).
- **Okamžitý škálovaný skok, bez prechodového deja** → žiadna informácia o póloch/nulách → použiť statický
  model; fitovanie ARMAX tu dáva bezmyselné čísla, ktoré testovacie dáta odhalia.

Toto je dôvod, prečo rozhodujúce skokové zmeny musia byť súčasťou **pôvodného návrhu experimentu**.

### H8. Ako identifikovať *nestabilný* systém (identifikácia v uzavretej slučke)?
Na nestabilnom systéme nemôžete robiť experiment v otvorenej slučke a potrebujete model
na návrh stabilizujúceho regulátora — problém **sliepky a vajca**. Ak systém
už beží vo výrobe, pravdepodobne existuje stabilizujúci regulátor. Potom vložte
**regulátor + systém do jednej krabice** a identifikujte **uzavretú slučku** (referencia →
odozva), pretože údaje z ustáleného stavu v otvorenej slučke nič nehovoria o póloch/oneskoreniach.
Príklad: P regulátor $K_R$ na $K/(Ts+1)$ (kladný pól, $T < 0$) dáva
charakteristickú rovnicu uzavretej slučky $Ts + 1 + K_R K = 0$; voľba $K_R$
ho stabilizuje a vzťah referencia→odozva (dve neznáme) sa fituje ako diskrétny **ARX**
model. Zlý experiment môže nafitnúť *stabilný* model na nestabilný systém — dôvod
pre vrátenie sa a prepracovanie návrhu.

---

## Časť I — Dve zadania (buďte pripravení diskutovať o svojom)

### I1. Zadanie 1 — statická identifikácia.
Fitovanie statických vstupno-výstupných vzťahov (napr. nádrž $q = k\sqrt{h}$, plynová nádrž
$V = f(T)$) metódou najmenších štvorcov; porovnávanie kandidátnych štruktúr
(lineárna/kvadratická/inverzná) pomocou RMSE a paritných grafov; štúdium vplyvu
merací šum na odhad.

### I2. Zadanie 2 — dynamická identifikácia zariadenia Flexy².
Flexy²: $u$ = rýchlosť ventilátora (vstup), $n$ = úroveň šumu, $y$ = ohyb flexibilného senzora
(výstup). Postup: načítanie a interpolácia (ZOH) → odstrániť zlé regióny (nulový ventilátor,
nasýtený ohyb) → štandardizácia (použiť $u$, nie konštantné $n$) → trénovanie = zašumený /
testovanie = výstup vyhladený s nulovou fázou → FIR(50) → ARX (rád z ACF/PACF) → porovnanie
RMSE. Očakávaný záver: **ARX presnejší s menej parametrami**.

### I3. Prečo použiť alebo nepoužiť kanál konštanty $n$?
$n$ je (takmer) konštantné → nulový rozptyl → nenesie žiadne dynamické informácie a nedá sa
štandardizovať. Preto sa ako vstup na identifikáciu dynamiky používa $u$ (rýchlosť ventilátora).

---

## Rýchle opakovanie

- Riešenie metódy najmenších štvorcov → $p = (X^T X)^{-1} X^T y$ = `X\y`.
- RMSE = smerodajná odchýlka reziduí, jednotky $y$.
- Štandardizácia → $(x-\mu)/\sigma$; korelácia $\in [-1,1]$.
- PCA = vlastné vektory kovariancie, zoradené podľa rozptylu.
- FIR = len minulé **vstupy**, všetky nuly, vysoký rád, vždy stabilný.
- ARX = minulé vstupy **aj výstupy**, póly+nuly, nízky rád, môže byť nestabilný.
- ARMAX = ARX + MA na minulých **chybách** ($c_i e_{k-i}$) → modeluje poruchy, sám sa opravuje.
- $z^{-1}$ = jednotkové oneskorenie.
- PACF → AR rád $n$; ACF → MA/pamäť.
- PRBS = najlepší perzistentne budiaci vstup.
- Trénovanie fituje, testovanie hodnotí; rozdiel = preučenie.
- RLS = „starý odhad + zisk × inovácia"; $\lambda = 1 \Rightarrow$ dávková MNŠ; $\lambda < 1 \Rightarrow$ sleduje drift.
- Zisk RLS $K$ = Kalmanov zisk; $P$ = kovariancia odhadu (začína veľká).
- Aktualizácia posunu = najjednoduchšia rekurzívna schéma: posun iba offsetu podľa chyby predikcie.
- Nestabilný systém → identifikovať **uzavretú slučku** (regulátor + systém v jednej krabici).
