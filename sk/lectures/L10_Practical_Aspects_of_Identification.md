---
lecture: L10
title: "Praktické aspekty identifikácie"
course: Identifikácia
source: "https://www.youtube.com/watch?v=uuRbAaWFfmQ"
---

# L10 — Praktické aspekty identifikácie

> Iba prepis (k tejto prednáške neexistuje zodpovedajúca sada snímok). Vzorce sú
> vysadené tak, ako boli povedané; kde hranica súčtu alebo výraz neboli plne
> uvedené, je to označené.

## Ďalší dynamický model: ARMAX

Minule sme prebrali FIR (predikuje výstup iba zo **vstupov**) a model
**ARX** (ľahko reprezentuje lineárne prenosové funkcie diskrétneho času). Ďalší
model rozširuje ARX: model **ARMAX** — **AutoRegressívny kĺzavý priemer s eXogénnym
vstupom** — kombinujúci ARX s členom **kĺzavého priemeru (MA)**. Jeho rovnica
predikcie:

$$
y_k = -\sum_{i=1}^{n} a_i\, y_{k-i}
        + \sum_{i=1}^{m} b_i\, u_{k-i}
        + \sum_{i=1}^{n_c} c_i\, e_{k-i}
$$

<!-- the upper limit of the MA (c) sum is not explicitly stated in the lecture -->

Tri časti: **autoregresívna** časť ($a_i$, minulé výstupy), časť
**exogénneho vstupu** ($b_i$, minulé vstupy) a nová časť **kĺzavého priemeru**
($c_i$, minulé **chyby** $e_{k-i}$).

### Čo robí člen chyby

Chyba $e_{k-i}$ používa iba **minulé** namerané dáta (index $k-i$). Zachytáva
**nesúlad** medzi tým, čo bolo predpovedané v minulosti, a tým, čo bolo skutočne
namerané neskôr. ARMAX teda **nie je** typ „raz natrénuj na ročných dátach a nechaj
bežať" — **koriguje sa sám počas behu**, robiac kĺzavý priemer predchádzajúcich
chýb.

**Prečo je to užitočné?** Pri identifikácii ARX/FIR z historických dát zbierame
páry vstup–výstup, ale **zanedbávame poruchy** (napr. **netesniaci ventil**). Ak je
porucha **meraná** (napr. senzor okolitej teploty), môže sa stať vstupom modelu,
predpovedaná pomocou predpovede počasia. Ak je **nemerateľná** (napr. rôzna kvalita
suroviny meniaca podmienky reaktora, ktorú nikto nehlási), ARMAX sa ju snaží
**detegovať a naučiť sa**: koeficienty $c$ absorbujú **systematické chyby** z porúch,
čím **oslobodia** koeficienty $a$ a $b$ na naučenie **skutočnej dynamiky zariadenia**.

**Trénovanie a predikcia.** ARMAX často potrebuje **nelineárnu optimalizáciu** na
fitovanie. Na predikciu do **budúcnosti** (kde chyby $e_k$ sú neznáme) sa zvyčajne
predpokladá, že $e_k$ sleduje **normálne rozdelenie s nulovou strednou hodnotou** a
nejakým rozptylom — nie nevyhnutne najlepšia voľba, ale umožňuje to zaobchádzať so
stredným prípadom ako s „bez poruchy" a budovať scenáre pre poruchy $\pm 1\sigma,
2\sigma, 3\sigma$.

## Algoritmus identifikácie systému

Daný čiernoskrinný prístroj, nájdi matematický model jeho správania. Kroky
(so spätnými väzbami):

### 1. Predchádzajúce znalosti

Pred čímkoľvek iným, získaj **predchádzajúce znalosti** — prečítaj manuál, spýtaj sa
ľudí. Zariadenia majú mnoho nezdokumentovaných vlastností. Toto hovorí, čo očakávať
(rýchly/pomalý), čím vedie experiment.

### 2. Návrh experimentu

Rozhodni vstupy, ako dlho experiment beží, kedy meniť vstupy. Toto je celý obor
(návrh experimentov). Kľúčová voľba je **tvar vstupného signálu**:

- Jednoduchý **skok** môže dosiahnuť ustálený stav a odhaliť dominantnú časovú
  konštantu, ale **rýchly pól** môže byť úplne skrytý (najmä pod šumom) a ľahko
  nedokážeš rozlíšiť prvý od druhého rádu.
- **Krátky, takmer impulzný** vstup: **pomalý** pól takmer nereaguje (nemá čas
  vzrásť), ale **rýchly** pól ukáže aspoň niečo (viditeľné pre matematiku /
  smerodajnú odchýlku, ak nie okom).
- Dlhý skok odhalí pomalý pól.

Kombinácia krátkych a dlhých skokov, ktoré skáču medzi úrovňami, je myšlienka za
**pseudonáhodnou binárnou postupnosťou (PRBS)** — skáče medzi dvoma úrovňami (napr.
0 a 1, alebo ľubovoľné dve hodnoty). Generovanie náhodných čísel a prahovaním dáva
tento tvar. PRBS budí rýchlu aj pomalú dynamiku.

### 3. Zber dát a predspracovanie

Zozbieraj a predspracuj: **štandardizácia**, kontrola veľkostí, odstraňovanie
**odľahlých hodnôt**, produkujúc čistú sadu dát.

### 4. Voľba sady modelov

Rozhodni **štruktúru** modelu pomocou predchádzajúcich znalostí:

- **Statický vs. dynamický.** Testuj so skokovými zmenami napr. $\tfrac{1}{3},
  \tfrac{2}{3}, 1$ (alebo 1, 2, 3) a skontroluj výstupy v ustálenom stave:
  - **Proporcionálne** výstupy → postačuje **statické zosilnenie** (rovnica ustáleného
    stavu).
  - **Neproporcionálne, ale rovnaké znamienko** zosilnenia → **nelineárne, ale
    zvládnuteľné** (zosilnenie mení veľkosť, ale nie znamienko) — riešiteľné
    integrálnou riadiacou akciou.
  - **Zosilnenie mení znamienko** → **červená výstraha**: silne nelineárne, v podstate
    nemožné riadiť lineárnym regulátorom (ani LQR zlyhá).
  - **Okamžitý škálovaný skok** bez prechodového deja → žiadna informácia o
    póloch/nulách; použi **statický** model (alebo je to diskrétny systém s veľkou
    periódou); nemá zmysel fitovať dynamický ARMAX — čísla by nič nereprezentovali,
    ako by čoskoro odhalili validačné/testovacie dáta.
  - (To znamená, že rozhodujúce skokové zmeny musia byť už naplánované v pôvodnom
    experimente; procesy majú často spätné väzby.)
- Taktiež rozhodni **rád modelu** a či zahrnúť **časové oneskorenie vstupu**.

#### Nestabilné systémy

Pre **stabilný** systém sme na dobre preskúmanom území. Pre **nestabilný**
systém musíme najprv **navrhnúť stabilizujúci regulátor** — problém sliepky a vajca
(potrebujeme model na návrh regulátora, potrebujeme regulátor na získanie dát).
Ak zariadenie beží vo výrobe roky, stabilizujúci regulátor môže už existovať.
Potom **dáme regulátor a zariadenie do jedného bloku** a identifikujeme
**uzavretú slučku** (referencia → odozva), pretože dáta ustáleného stavu otvorenej
slučky nič neodhaľujú o časových konštantách, oneskoreniach, póloch, nulách.

Príklad s **P regulátorom** $G_C = K_R$ a zariadením $G_S = \dfrac{K}{Ts+1}$
(kde **záporná** časová konštanta $T$, t.j. kladný pól, ho robí nestabilným).
Charakteristická rovnica uzavretej slučky (po spoločnom menovateli):

$$
T s + 1 + K_R K = 0
$$

Výberom správneho $K_R$ (tu pravdepodobne záporného, ak je $K$ kladné) možno
nestabilný pól posunúť tak, aby bol **stabilný**. Vzťah uzavretej slučky
(referencia → odozva) má dva neznáme parametre, ktoré možno transformovať na diskrétny
čas a **nafitovať ako model ARX**.

### 5. Voľba kritéria fitovania

Rozhodni, či je **metóda najmenších štvorcov** prijateľná: metóda najmenších štvorcov
je vhodná, keď je šum **Gaussovský** (normálne rozdelený). Pri mnohých odľahlých
hodnotách pomáha kritérium **súčtu absolútnych hodnôt**.

### 6. Fitovanie modelu

S troma ingredienciami — **sadou modelov**, **dátami** a **kritériom fitovania** —
nakoniec **nafituj (vypočítaj) model**.

### 7. Testovanie modelu a spätné väzby

**Testuj / validuj** model. Dobrý model by mal mať „**certifikát**":
oblasť, v ktorej bol natrénovaný, a matematiku, ktorú používa — **používaj
s opatrnosťou, nikdy mimo tej oblasti**. Ak model **nie je dostatočne dobrý**, vráť sa
späť k:

- **prenavrhnutiu experimentu** (napr. nafitovali sme stabilný model na nestabilné
  zariadenie kvôli nesprávnemu experimentu/sade modelov), alebo
- **zmene kritéria fitovania** (napr. prejdi na súčet absolútnych hodnôt, ak odľahlé
  hodnoty nemožno zahodiť).

## Voľba rádu modelu: korelačná analýza

V statickom prípade sme vyberali regresory (tlak, teplota, …) pomocou
**korelačnej analýzy** — zhruba, súčtom centrovaných súčinov vstupu s výstupom
(a normalizovaním na korelačný koeficient). V **dynamickom** prípade členy modelu
reprezentujú **minulé dáta**, takže úloha je podobná: ktoré **minulé hodnoty**
(oneskorenia) by mal model zahrnúť — prvé, druhé, …, ale možno nie tretie?

### Autokorelačná funkcia (ACF)

Porovnávame signál **sám so sebou posunutým v čase**: je $y_k$ korelované s hodnotou
o vzorku skôr? Vezmeme kópiu signálu, posunieme ju **dozadu** v čase a vypočítame
korelačný koeficient signálu s jeho posunutou kópiou —
**autokorelácia** (slovenská intuícia: „Inception"). Opakovanie pre posuny 1, 2, 3, …
vzoriek dáva **autokorelačnú funkciu (ACF)**, dostupnú v MATLABe / Pythone.
Pojmovo (centrované súčiny, normalizované):

$$
\text{ACF}(i) \;\sim\; \frac{1}{N}\sum_{k}(y_k - \bar{y})(y_{k-i} - \bar{y})
$$

<!-- the exact normalization was not fully written on the board; the function normalizes so ACF(0)=1 -->

Čítanie grafu ACF v MATLABe (stonkový graf):

- Horizontálna os = **oneskorenie** (posun $i$, intuitívne časové oneskorenie).
- **ACF(0) = 1** vždy — signál je 100% korelovaný sám so sebou (funkcia
  štandardizuje dáta).
- **Modrý pás** je interne vypočítaný interval šumu **±3σ** — ignoruj všetky stonky
  ležiace vo vnútri.

### Parciálna autokorelačná funkcia (PACF)

**Parciálna autokorelačná funkcia (PACF)** je podobná, ale pri výpočte korelácie
pri danom oneskorení **odstraňuje** koreláciu už vysvetlenú
**medziľahlými** (napr. jednotkovým oneskorením) posunmi (hrubý popis myšlienky).

### Príklady

- **Gaussovský šumový vstup** (stredná hodnota ≈ 0, σ ≈ 1): každá vzorka je nezávislá
  od predchádzajúcej (ako hádzanie kockou), takže ACF ukazuje len hrot pri oneskorení 0;
  všetky ostatné stonky ležia v pásme — **žiadna korelácia**.
- **Výstup FIR druhého rádu (kĺzavý priemer)**, napr. $y_1 = \tfrac{1}{2}u_1 +
  \tfrac{1}{2}u_0$, $y_2 = \tfrac{1}{2}u_2 + \tfrac{1}{2}u_1$: ACF má **jednu
  významnú hodnotu pri oneskorení 1**, pretože $y_1$ a $y_2$ zdieľajú spoločný vstup
  $u_1$. To naznačuje, že $y_k$ je funkciou $u_{k-1}$ — dynamický model posunutý aspoň
  o jednu vzorku dozadu. PACF nie je tu veľmi informatívna so iba 100 vzorkami.
- **ARX prvého rádu**, napr. $y_1 = \tfrac{9}{10}y_0 + \tfrac{1}{10}u_0$, $y_2 =
  \tfrac{9}{10}y_1 + \dots = \tfrac{81}{100}y_0 + \dots$: ACF ukazuje koreláciu cez
  **mnoho** oneskorení (výstup je ovplyvnený počiatočnou podmienkou ešte asi 10 krokov
  neskôr), takže môže **prehnane navrhnúť** vysoký rád (5., 10.). **PACF** jasne
  naznačuje **prvý rád** odstránením prenášanej korelácie — takže pre AR/modely typu
  prenosovej funkcie je **PACF lepšia na výber rádu**.
- **Tvar vstupu záleží.** Rovnaký systém prvého rádu so vstupom $0,1,0,1,\dots$
  (namiesto PRBS) mätie analýzu (vstup skáče ďaleko medzi po sebe idúcimi krokmi);
  PRBS, kde po sebe idúce vstupy zostávajú bližšie, sa správa oveľa lepšie. ACF stále
  ukazuje dynamické správanie; ignoruj mierne rozptýlenú PACF, pokiaľ neexistuje
  skutočná sezónnosť.
- **Dynamika druhého rádu** so Gaussovým šumom alebo PRBS vstupom: ACF ukazuje veľkú
  seba-koreláciu, ale **PACF jasne naznačuje vziať dve minulé hodnoty** —
  vyber **druhý rád**.

Kombinuj korelačnú analýzu s **krížovou validáciou** (trénovacie / validačné /
testovacie dáta), aby si si bol istý, že vybraný rád modelu je správny.
