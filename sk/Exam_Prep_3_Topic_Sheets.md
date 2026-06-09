# Identifikácia — Tematické listy na ústnu skúšku

Jedna strana na tému. Dostanete **2 témy, jednu z každej kategórie**. Ku každému listu:
**Čo povedať** = plán na tabuľu · **Vzorce** = čo napísať ·
**Doplňujúce otázky** = pravdepodobné doplňujúce otázky · **Ak zaseknem** = čo bezpečne dodať.

*(Každá téma je oddelená zlomom strany pre tlač do PDF.)*

---

# I — STATICKÁ IDENTIFIKÁCIA

## Téma 1 — Úvod do štatistiky
*Prednáška L02 · zálohy: časti A, B*

**Čo povedať (plán na tabuľu)**
1. Meráme so šumom: **meranie = skutočný signál + šum**. Štatistika
   opisuje šum a umožňuje nám extrahovať signál.
2. **Poloha** dát: priemer, medián, geometrický priemer.
3. **Rozptyl** dát: rozptyl a smerodajná odchýlka.
4. **Hustota pravdepodobnosti** vs **distribučná funkcia** vs **kvantil** (inverzná distribučná funkcia).
5. **Normálne (Gaussovo)** rozdelenie a pravidlo 68–95–99,7.
6. Histogram → skutočná hustota pravdepodobnosti s rastúcim počtom vzoriek (zákon veľkých čísel).
7. Prečo nám na tom záleží: Gaussov šum robí **metódu najmenších štvorcov optimálnou**.

**Vzorce**

$$
\begin{aligned}
\text{priemer}\quad &\mu = \frac{1}{N}\sum_i x_i \\
\text{rozptyl}\quad &\sigma^2 = \frac{1}{N-1}\sum_i (x_i-\mu)^2 \quad(N-1=\text{nestranný}) \\
\text{sm. odch.}\quad &\sigma = \sqrt{\sigma^2} \\
\text{CDF}\quad &F(x) = P(X \le x) = \int \mathrm{pdf}, \qquad \text{kvantil} = F^{-1}(p) \\
\text{normálne}\quad &\pm1\sigma \approx 68\%,\ \ \pm2\sigma \approx 95\%,\ \ \pm3\sigma \approx 99.7\%
\end{aligned}
$$

**Doplňujúce otázky**
- *Prečo $N-1$?* → robí výberový rozptyl nestranným odhadom skutočného rozptylu.
- *Hustota pravdepodobnosti vs distribučná funkcia?* → hustota vs kumulatívna; distribučná funkcia je integrál hustoty, rastie od 0 do 1.
- *Priemer vs medián?* → medián je odolný voči odľahlým hodnotám; priemer je citlivý.

**Ak zaseknem:** zmienime, že celá identifikácia stojí na týchto základoch — každý
parameter, ktorý odhadujeme, je štatistika vypočítaná zo zašumených dát.

<div style="page-break-after: always"></div>

## Téma 2 — Odhad konštanty
*Prednášky L03–L04 · zálohy: časti EC, B*

**Čo povedať (plán na tabuľu)**
1. Najjednoduchšia identifikácia: odhadnúť jednu skutočnú hodnotu $c$ z $N$ zašumených meraní
   $y_i = c + e_i$. Je to regresia s $X = \mathbf 1_N$ (stĺpec jednotiek).
2. Metóda najmenších štvorcov → odhad **je aritmetický priemer** (odvoďte).
3. Kvalita odhadovača: **nestranný**, **konzistentný**, $\mathrm{var}(\hat{c}) = \sigma^2/N$.
4. **Zákon $\sqrt{N}$**: chyba $\propto \sigma/\sqrt{N}$ → 4-násobok dát na polovičnú
   chybu. Preto priemerujeme opakované merania.
5. Alternatívy: **medián** (odolný voči odľahlým hodnotám), **geometrický priemer**
   (multiplikatívne dáta). Porovnanie rozptýlenia pomocou škatuľových grafov (nádrž $k_{11}$, Seminár 4).
6. Gaussov šum → priemer je odhad **maximálnej vierohodnosti**.

**Vzorce**

$$
\begin{aligned}
J(c) &= \sum_i (y_i - c)^2 \\
\frac{dJ}{dc} = -2\sum_i (y_i - c) = 0 \;&\Rightarrow\; \hat{c} = \frac{1}{N}\sum_i y_i = \text{priemer} \\
\mathrm{var}(\hat{c}) &= \frac{\sigma^2}{N}, \qquad \text{štandardná chyba} = \frac{\sigma}{\sqrt{N}} \\
\text{95\% CI:}\quad &\hat{c} \pm t\cdot\frac{\hat{\sigma}}{\sqrt{N}}
\end{aligned}
$$

**Doplňujúce otázky**
- *Prečo je priemer „najlepší"?* → odhad s minimálnym rozptylom spomedzi nestranných odhadov pri Gaussovom šume.
- *Kedy zlyhá?* → odľahlé hodnoty/skosenie → použiť medián; pomery → geometrický priemer.
- *Ako sa chyba zmenšuje?* → ako $1/\sqrt{N}$, nie $1/N$ — klesajúce výnosy.

**Ak zaseknem:** zdôrazníme zákon $\sqrt{N}$ a to, že „odhad konštanty" =
jednoparametrový prípad lineárnej regresie.

<div style="page-break-after: always"></div>

## Téma 3 — Lineárna regresia
*Prednášky L05–L06 · zálohy: časť C*

**Čo povedať (plán na tabuľu)**
1. Model **lineárny v parametroch**: $y = X p + e$. Príznaky môžu byť nelineárne
   v dátach ($\sqrt{h}$, $T^2$, $1/T$) — lineárna je len závislosť od *parametrov*.
2. **Regresná/návrhová matica** $X$ (stĺpce = príznaky); stĺpec pre konštantný člen.
3. Metóda najmenších štvorcov minimalizuje $\|X p - y\|^2$ → **normálne rovnice**; MATLAB `X\y`.
4. **Gauss–Markovove** predpoklady → MNŠ je **BLUE** (najlepší lineárny nestranný odhadovač).
5. Posúdenie zhody: **RMSE**, paritný graf, intervaly spoľahlivosti parametrov.
6. Zovšeobecňuje sa na mnoho vstupov (multivariátna regresia).

**Vzorce**

$$
\begin{aligned}
&\min_p \|X p - y\|^2 \;\Rightarrow\; p = (X^T X)^{-1} X^T y \quad(= X\backslash y,\ \text{interne cez QR}) \\
&\hat{y} = X p \\
&\mathrm{RMSE} = \sqrt{\mathrm{mean}\big((\hat{y}-y)^2\big)}
\end{aligned}
$$

Gauss–Markovove predpoklady (šum s nulovou strednou hodnotou, konštantným rozptylom, nekorelovaný) $\Rightarrow$ **BLUE**.

**Doplňujúce otázky**
- *Prečo štvorcová chyba?* → diferencovateľná, uzavretý tvar, = MLE pri Gaussovom šume.
- *Lineárny v čom?* → v parametroch, nie nevyhnutne v dátach.
- *Čo je konštantný člen?* → stĺpec `ones`; umožňuje nenulový posun.

**Ak zaseknem:** nakreslím priamku cez rozptýlené body a reziduá, ktoré minimalizuje.

<div style="page-break-after: always"></div>

## Téma 4 — Praktické aspekty lineárnej regresie
*Prednáška L07 · zálohy: časti C7, D, E*

**Čo povedať (plán na tabuľu)**
1. **Štandardizácia** vstupov ($(x-\mu)/\sigma$): porovnateľné mierky + lepšie podmienená matica $X^T X$.
2. **Korelácia vs kovariancia**; korelácia $\in [-1, 1]$, bezrozmerná.
3. **Multikolinearita**: korelované vstupy → takmer singulárna $X^T X$ → nestabilné, obrovské
   koeficienty → odstrániť redundantné príznaky (výber príznakov).
4. **PCA**: otočenie na ortogonálne smery maximálneho rozptylu → dekorelujeme /
   znižujeme dimenziu (počet PC vyberieme podľa pravidla lakťa).
5. **Trénovanie vs testovanie**; pretrénovanie vs podtrénovanie; zvolíme rád modelu, ktorý
   minimalizuje *testovaciu* chybu.
6. Pozor na odľahlé hodnoty a najskôr vyčistiť dáta.

**Vzorce**

$$
\begin{aligned}
\text{štandardizácia:}\quad &x_s = \frac{x-\mu}{\sigma} \\
\text{korelácia:}\quad &r = \frac{\mathrm{cov}(x,y)}{\sigma_x\,\sigma_y} \in [-1,1]
\end{aligned}
$$

- PCA: $\mathrm{eig}\big(\mathrm{cov}(X)\big)$ → vlastné vektory (smery), vlastné čísla (rozptyl).
- Pretrénovanie: $\mathrm{RMSE_{\text{train}}}\downarrow \text{ ale } \mathrm{RMSE_{\text{test}}}\uparrow$.

**Doplňujúce otázky**
- *Prečo odstrániť korelované vstupy?* → zlé podmienenie, nespoľahlivé koeficienty.
- *Prečo štandardizovať pred PCA?* → aby premenné s veľkou mierkou nedominovali.
- *Ako odhaliť pretrénovanie?* → rozdiel medzi trénovacím a testovacím RMSE.

**Ak zaseknem:** „matematika je rovnaká ako v Téme 3 — toto sú veci, ktoré to
spravia funkčným na skutočných, neporiadnych dátach."

<div style="page-break-after: always"></div>

# II — DYNAMICKÁ IDENTIFIKÁCIA

## Téma 5 — Filtrácia dynamických signálov
*Prednáška L08 · zálohy: časť F*

**Čo povedať (plán na tabuľu)**
1. Skutočné signály = užitočná dynamika + šum, oddelené **frekvenčným obsahom**.
2. **Dolnopriepustný** filter zachováva pomalý trend (vyhladzovanie); **hornopriepustný** zachováva rýchlu
   zložku; pásmový priepust zachováva stredné pásmo. **Medzná frekvencia** určuje delenie.
3. **Kĺzavý priemer** je FIR dolnopriepustný filter; väčšie okno = viac vyhladzovania.
4. **Kauzálny** (`filter`) používa len minulé vzorky → pridáva **časové oneskorenie**;
   **nulová fáza** (`filtfilt`, dopredu+dozadu) → bez oneskorenia.
5. Kompromis: viac vyhladzovania odstraňuje šum, ale zároveň sploští skutočnú dynamiku.

**Vzorce**

$$
y_{s,k} = \frac{1}{n}\sum_{i=0}^{n-1} y_{k-i} \quad(\text{kĺzavý priemer — FIR, dolnopriepustný})
$$

- Kauzálny `filter` → fázové oneskorenie; `filtfilt` → nulová fáza (bez oneskorenia).
- Dolnopriepustný: zachová nízke frekvencie; hornopriepustný: zachová vysoké frekvencie.

**Doplňujúce otázky**
- *Prečo nulová fáza?* → zachováva časovú synchronizáciu vyhladzeného výstupu (používa sa pre testovací
  výstup v Zadaní 2).
- *Dolno- vs hornopriepustný pre šum?* → šum je vysokofrekvenčný → dolnopriepustný na jeho odstránenie.
- *Nevýhoda silného vyhladzovanie?* → stratíme rýchlu dynamiku, ktorú chceme identifikovať.

**Ak zaseknem:** načrtnem zašumenú krivku a hladkú čiaru cez ňu; poznamenám oneskorenie,
ktoré by kauzálny filter pridal.

<div style="page-break-after: always"></div>

## Téma 6 — Modelovanie dynamických systémov
*Prednáška L09 · zálohy: časť G*

**Čo povedať (plán na tabuľu)**
1. **Dynamický** = výstup má **pamäť** (závisí od minulých vstupov/výstupov), na rozdiel od
   statického zobrazenia.
2. LTI systémy: výstup = **konvolúcia** vstupu s **impulznou odozvou**.
3. **FIR** model: $y_k = \sum b_i u_{k-i}$ — váhy = impulzná odozva; len nuly,
   **vždy stabilný**, potrebuje **vysoký rád**.
4. **ARX** model: $y_k = -\sum a_i y_{k-i} + \sum b_i u_{k-i}$ — používa minulé výstupy
   (spätná väzba); **málo parametrov**, môže byť nestabilný.
5. **ARMAX** = ARX + člen kĺzavého priemeru na minulých **chybách** → zachytáva
   poruchy a online sa samo-koriguje.
6. Všetky sú **lineárne v parametroch** (ARMAX potrebuje nelineárnu optimalizáciu pre časť
   $c$) → metóda najmenších štvorcov s regresiou posunutých vzoriek (`X\y`).
7. Prenosová funkcia v $z^{-1}$ (jednotkové oneskorenie). FIR vs ARX: ARX zvyčajne nižšie RMSE
   s oveľa menej parametrami.

**Vzorce**

$$
\begin{aligned}
\text{konvolúcia:}\quad &y(t) = \int_0^t g(\tau)\,u(t-\tau)\,d\tau \quad(g=\text{impulzná odozva}) \\
\text{FIR:}\quad &y_k = \sum_{i=1}^{m} b_i u_{k-i} \\
\text{ARX:}\quad &y_k = -\sum_i a_i y_{k-i} + \sum_i b_i u_{k-i} \\
\text{ARMAX:}\quad &y_k = -\sum_i a_i y_{k-i} + \sum_i b_i u_{k-i} + \sum_i c_i e_{k-i} \\
&G(z^{-1}) = \frac{\sum_i b_i z^{-i}}{1 + \sum_i a_i z^{-i}}, \qquad z^{-1}=\text{jednotkové oneskorenie}
\end{aligned}
$$

**Doplňujúce otázky**
- *FIR vs ARX?* → FIR len nuly/stabilný/vysoký rád; ARX póly+nuly/málo parametrov/môže byť
  nestabilný.
- *Čo pridáva ARMAX?* → MA člen na minulých chybách, ktorý absorbuje **poruchy**
  (unikajúci ventil, zmena prívodu), čím oslobodí $a,b$ na učenie skutočnej dynamiky.
- *Prečo FIR potrebuje rád ~50?* → žiadna spätná väzba; pamäťové okno $\tau = m\cdot T_s$ musí
  pokrývať dobu ustálenia ($m=50$, $T_s=0.02$ → len 1 s), a vyšší rád takmer nepomáha.
- *Čo je $z^{-1}$?* → oneskorenie o jeden vzorku: $z^{-1} y_k = y_{k-1}$.

**Ak zaseknem:** „je to stále metóda najmenších štvorcov — mení sa len regresná matica (teraz
zložená z posunutých vstupov a výstupov)."

<div style="page-break-after: always"></div>

## Téma 7 — Rekurzívna identifikácia
*Prednáška L11 · zálohy: časť R*

**Čo povedať (plán na tabuľu)**
1. **Dávková** MNŠ znovu spracuje všetky dáta; **rekurzívna** aktualizuje odhad s každým
   novým vzorkom → **online / real-time** identifikácia.
2. Štruktúra **RLS**: **nový odhad = starý odhad + zosilnenie × inovácia**, kde
   **inovácia** je chyba predikcie.
3. Kovariancia $P$ (spoľahlivosť, začína veľká) a zosilnenie $K$ (= **Kalmanov zisk**).
4. **Zabudnutý faktor $\lambda$**: $1$ = štandardné RLS ($\equiv$ dávková MNŠ); $<1$
   znevažuje staré dáta → **sleduje časovo premenné parametre** (kompromis sledovanie vs šum).
5. RLS je špeciálny prípad **Kalmanovho filtra**.
6. Najjednoduchšia verzia = **aktualizácia biasu**: keď driftuje len konštantný posun, posunieme
   $b$ o chybu predikcie (voliteľne filtrovanú dôvernostným zosilnením $\delta$).

**Vzorce**

$$
\begin{aligned}
e_k &= y_k - \phi_k^T \theta_{k-1} \quad(\text{inovácia / chyba predikcie}) \\
K_k &= \frac{P_{k-1}\,\phi_k}{\lambda + \phi_k^T P_{k-1}\,\phi_k} \quad(\text{zosilnenie}) \\
\theta_k &= \theta_{k-1} + K_k\,e_k \quad(\text{aktualizácia odhadu}) \\
P_k &= \frac{1}{\lambda}\big(P_{k-1} - K_k\,\phi_k^T P_{k-1}\big) \quad(\text{aktualizácia kovariancie}) \\
\text{bias:}\quad b_k &= b_{k-1} + (y_{k-1} - \hat{y}_{k-1}), \quad \delta \in [0,1] \\
\text{skalár:}\quad a_N &= a_{N-1} + \frac{x_N}{\sum_k x_k^2}\,(y_N - a_{N-1}x_N)
\end{aligned}
$$

**Doplňujúce otázky**
- *Prečo rekurzívne?* → použitie v reálnom čase; časovo premenné systémy; nie je potrebné uchovávať všetky dáta.
- *Čo robí $\lambda$?* → $\lambda<1$ zabúda staré dáta na sledovanie driftu; menší = rýchlejší, ale šumovejší.
- *Súvislosť s dávkovou MNŠ / Kalman?* → $\lambda=1 \Rightarrow$ rovnaké ako dávková MNŠ; RLS = Kalmanov filter pre konštantné parametre.
- *Najjednoduchší prípad?* → aktualizácia biasu — adaptujeme len posun; rovnaký tvar „starý + zosilnenie × chyba".

**Ak zaseknem:** napíšem jednoriadkový mantra „**starý + zosilnenie × inovácia**" a vysvetlím
každý člen.

<div style="page-break-after: always"></div>

## Téma 8 — Praktické aspekty identifikácie
*Prednáška L10 · zálohy: časti G6, H, E*

**Čo povedať (plán na tabuľu)**
1. **Návrh experimentu**: vstup musí byť **trvalo excitujúci** (bohatý na frekvencie),
   inak dynamiku nevidíme.
2. Typy vstupov: **skoková zmena** (málo frekvencií) → **náhodný** → **PRBS** (blízko bielemu, uprednostňovaný, reprodukovateľný).
3. **Interval vzorkovania** $T_s$: príliš veľký → aliasing/chýbame rýchlu dynamiku; príliš malý →
   šumový/stiff.
4. **Výber rádu modelu** z **ACF/PACF** výstupu (PACF → AR rád $n$).
5. **Statická vs dynamická / kontrola linearity**: skoková zmena $\tfrac13,\tfrac23,1$ → proporcionálna
   = statické zosilnenie; rovnaké znamienko, ale neproporcionálna = nelineárne-znesiteľné; **zmena znamienka =
   červená výstraha** (neriaditeľné lineárnym regulátorom).
6. **Nestabilná sústava** → identifikovať **uzavretú slučku** (regulátor + sústava v jednom bloku,
   referencia → odozva), potom fitovať ARX.
7. **Validácia**: trénovacie vs testovacie RMSE; predikcia o jeden krok dopredu vs voľná
   simulácia; kontrola reziduí; vyhnúť sa pretrénovaniu.
8. Reálny postup (**Flexy²**, Zadanie 2): vyčistenie → štandardizácia → rozdelenie → FIR/ARX
   → porovnanie.

**Vzorce**
- **Trvalá excitácia:** vstup dostatočne bohatý na excitáciu všetkých módov.
- **PRBS:** 2-úrovňový pseudo-náhodný, blízko bielemu spektru (najlepší dynamický vstup).
- **Rád:** PACF klesne pod hranicu spoľahlivosti pri oneskorení $n$ $\Rightarrow$ AR rád
  $n$; zachovať $m \le n$.
- **Validovať** na **testovacích** dátach; voľná simulácia je náročnejší test.

**Doplňujúce otázky**
- *Prečo PRBS namiesto skoku?* → skok excituje málo frekvencií; PRBS excituje široké pásmo.
- *Ako zvoliť rád?* → ACF/PACF; najmenší rád zachytávajúci dynamiku (princíp šetrnosti).
- *Trénovanie vs testovanie?* → trénovanie fituje parametre, testovanie dáva skutočnú presnosť; rozdiel = pretrénovanie.
- *Prečo najskôr vyčistiť dáta?* → zlé časti (mŕtva nula na začiatku, saturácia na konci) narúšajú
  vzťah vstup→výstup a znehodnocujú regresiu → vyššie RMSE.
- *Predikcia o jeden krok vs simulácia?* → predikcia o jeden krok používa skutočné minulé výstupy (jednoduchšia, nižšie RMSE);
  porovnávame modely *rovnakým* spôsobom, aby sme boli féroví.
- *Ako rozlíšiť statickú od dynamickej?* → skokové zmeny; okamžitý škálovaný výstup = statická,
  nemá zmysel fitovať dynamický model.
- *Nestabilná sústava?* → nemožno pracovať v otvorenej slučke; identifikovať uzavretú slučku s existujúcim
  stabilizujúcim regulátorom.

**Ak zaseknem:** opíšem postup Zadania 2 od začiatku do konca — pokrýva každý
praktický bod.
