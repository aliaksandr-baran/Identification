---
lecture: L01
title: "Úvod do identifikácie. Vizualizácia dát."
course: Identifikácia
source: "https://www.youtube.com/watch?v=PZz7OA9_4Gw"
---

# L01 — Úvod do identifikácie. Vizualizácia dát.

## O tejto prednáške

Prednášajúci predstavuje predmet **identifikácia** a rámuje túto prvú
prednášku ako relatívne stručný, „komiksový" prehľad — veľa obrázkov a **žiadne
matematické vzorce**. Cieľom je pozrieť sa na to, ako náš svet funguje
v súčasnosti, ako fungoval predtým, čo sa zmenilo a prečo by sme sa mali venovať
predmetu identifikácie systémov. Časť materiálu bola už ukázaná v predmete
„modelovanie v procesnom priemysle", tu však ideme o niečo hlbšie.

## Zrýchľujúci sa svet

Prvou správou je, že náš svet sa skutočne zrýchľuje — všetko sa deje
rýchlejšie a rýchlejšie. Prednášajúci to ilustruje postupnosťou
veľkých udalostí v ľudskej histórii a skracujúcimi sa intervalmi medzi nimi:

- **Poľnohospodárska revolúcia** — keď ľudstvo prestalo túlať sa po
  Zemi a usadilo sa niekde s poľom úrody (zelenina, ovocie a podobne).
- Potom uplynulo **8 000 rokov** do **priemyselnej revolúcie**, kde sme
  si uvedomili, že môžeme rozdeliť prácu v spoločnosti a niektoré práce
  automatizovať alebo aspoň mechanizovať — pomocou parného alebo iných strojov.
- Od priemyselnej revolúcie k **vynálezu žiarovky**.
- Medzi vynálezom žiarovky a **pristátím na Mesiaci** uplynulo len **120 rokov**.
- Od pristátia na Mesiaci k **World Wide Web** len **20 rokov**
  (prednášajúci najprv povie „90 rokov", potom opraví na asi 20).
- A **9 rokov** k **sekvenovaniu ľudského genómu**.

Tieto udalosti sú do istej miery ľubovoľné, no sú to veľké udalosti v ľudskej histórii.
Zaujímavé je, že medzery medzi nimi sa stále skracujú — vývoj sa zrýchľuje.
Toto zrýchlenie v 20. a 21. storočí bolo pozorované aj v niečom, čo sa
nazýva **Moorov zákon**.

## Moorov zákon

Pán Moore bol inžinier (prednášajúci sa domnieva, že v Bell Laboratories v USA).
Urobil **pozorovanie na základe dát**: vzal nejaké dáta, použil časovú os a
vyznačil niekoľko bodov predstavujúcich **počet tranzistorov** na rôznych
počítačových procesoroch (dnes by sme povedali „na čipoch") — teda koľko
výpočtového výkonu procesor obsahuje. Tieto dáta zobrazil a zistil, že
**zhruba každých 10 rokov sa počet tranzistorov zdvojnásobuje**.

Keď sa niečo zdvojnásobuje, ide o **exponenciálny rast**.

### Príbeh o šachu a ryži (príklad exponenciálneho rastu)

Štandardný prvý príklad exponenciálneho rastu: príbeh o šachovi/kráľovi v
Iráne alebo Perzii, ktorý hral šach s jedným zo svojich sluhov. Prehrával hru
a opýtal sa sluhu, čo chce ako odmenu. Sluha povedal: daj **jedno** zrnko ryže
na prvé políčko šachovnice, **dve** zrnká na ďalšie políčko, a stále
**zdvojnásobuj**. Na treťom políčku sú štyri zrnká, na štvrtom osem, a stále
sa to zdvojnásobuje. Keď sa dostanete na koniec (asi $2^{64}$ zrniek ryže),
máte asi rovnaký počet zrniek, ako je počet atómov vo vesmíre, alebo aj viac.
Je to teda dosť desivé.

### Logaritmická os

Na Moorovom grafe nie je os y **v lineárnej mierke** — je
**logaritmická**. Jeden krok v tomto smere neznamená pridávanie rovnakého množstva
zakaždým (1, 2, 3, 4, 5, 6); znamená pridávanie **mocnín desiatky**. Tu jeden krok
zodpovedá zväčšeniu mierky o $10^5$, teda o 100 000 (napríklad
od 1 do 100 000). Preto **ak na takomto grafe dostanete priamku, naznačuje to exponenciálny rast** —
čo je presne to, čo Moore pozoroval.

S ďalším vývojom bol Moorov zákon vlastne **porušovaný**: videli sme
ešte rýchlejší vývoj a ešte vyšší počet tranzistorov na čipe. Graf, ktorý
prednášajúci ukazuje, je z roku 2011; predpovedá, že v určitom bode dosiahneme
**singularitu** — že v roku 2023 výpočtový výkon čipu prekoná ľudský mozog.
Možno sa niekde okolo toho nachádzame.

## Rast dát

Rovnaký trend, s mierne odlišnými číslami, sa deje aj s **množstvom
dát**. Lacnejšie, dostupnejšie a spoľahlivejšie senzory vedú k väčšej senzornej
kapacite: môžeme snímať viac dát, ukladať viac dát, za oveľa nižšiu
cenu. Problémom teraz je, že **potrebujeme pochopiť, čo dáta znamenajú** —
svet je nesmierene bohatý na dáta.

Prednášajúci zdôrazňuje, že **dáta samotné nám nehovoria, čo sa stalo** —
len sedia v nejakej databáze. Je dobré dáta vykresliť a mať aspoň
základnú štatistiku pre prehľad, ale **zmysluplná interpretácia dát je oveľa
náročnejší problém.** Zvyšok prednášky prechádza príkladmi dátových súborov.

## Príklady dát zo sveta

### Ceny plemien psov počas COVID

Správa v médiách (okolo roku 2022) informovala, že ceny plemien psov sa rýchlo zmenili
počas pandémie COVID vo Veľkej Británii. Diskutovaný dôvod: **dopyt stúpol** —
počas pandémie smeli na niektorých miestach von iba ľudia so psami,
a ľudia uväznení doma chceli spoločnosť/priateľov.

### Hladiny oxidu dusičitého nad Čínou

Satelitné snímky ukazujú **hladiny oxidu dusičitého (NO₂)** nad Čínou v
**januári 2020** a opäť vo **februári 2020**. Vo februári sú hladiny oveľa
nižšie. Dôvod: **zastavenie prevádzky tovární** kvôli pandémii COVID-19.
Prednášajúci poznamenáva, že COVID-19 je akoby skvelý zdroj dát — bol
v podstate **skokovou zmenou mnohých vstupov vo svete** (analogicky skokova zmena
vstupu aplikovaná na zariadenie).

### Ceny fosílnych palív

Okolo **marca 2020** nastáva veľká skoková zmena v **cenách fosílnych palív** —
ropa, nafta/zemný plyn, dokonca uhlie. Pointa: keby ste si v januári 2020
dokázali predpovedať, čo sa stane s cenami ropy, mohli by ste prispôsobiť
stratégiu svojej firmy (nakúpiť viac ropy, vyprázdniť zásobníky, kým je cena nízka atď.)
a zarobiť peniaze. Peniaze sú veľkým hnacím motorom týchto problémov.

### Romantické vzťahy tučniakov v akváriu v Kjóte

Komiksový **vývojový diagram komplikovaných romantických vzťahov medzi
tučniakmi** v akváriu v Kjóte. Sledovalo sa, ako sa tučniaci navzájom majú radi
(vrátane prípadného „podvádzania" partnerov) a potom to bolo zobrazené. Jedno možné
využitie: personál akvária mohol predchádzať bitkám medzi tučniakmi riadením
„milostných trojuholníkov".

### Facebook blokuje francúzske mesto

Okolo apríla 2021 Facebook zablokoval webovú stránku francúzskeho mesta
<!-- unclear: meno mesta, popis hovorí "Bish"; znie ako mesto "Bitche" -->.
Štatisticky kombinácia písmen v názve najviac pripomína neslušné slovo. Facebook zrejme
má politiku, že neslušné slová nesmú byť názvami webových stránok / Facebook stránok / používateľov,
a prevádzkuje algoritmus porovnávajúci neslušné slová s názvami. So štatistickými dôkazmi
(s viac ako **95 % spoľahlivosťou**) algoritmus tvrdil, že webová stránka porušuje pravidlá.

### Ekologické trasy v Google Maps

Google Maps mal ponúkať najekologickejšiu / environmentálne najšetrnejšiu
trasu pre vaše auto. Nie je jasné, či sa to plne realizovalo; zdá sa, že stále
ponúka hlavne najrýchlejšiu (a najkratšiu) trasu. Diskutované obmedzenie:
výber trasy v skutočnosti nezohľadňuje, či idete hore alebo dole, a
navrhovanie trasy cez dopravnú zápchu nie je ekologické, pretože nakoniec
nechávate bežať motor, kým stojíte v kolóne.

### Únik dát / ochrana súkromia dát

Novinový titulok (žartovne: ak počúvate Nickelback
<!-- unclear: popis znie "Nickel Beck" -->, buďte si vedomí tejto hrozby) poukazuje na
**ochranu súkromia dát**: ako šifrujeme a kódujeme dáta, aby neboli vystavené
tretím stranám. Prednášajúci poznamenáva (bez menovania krajín, aby zostal politicky
korektný), že možno nechcete zdieľať svoje dáta s nikým, a predsa to robíme pomerne často.

### Cena Bitcoinu (prednášajúceho obľúbený trend)

Zobrazuje sa séria novinových titulkov, spočiatku úmyselne v nesprávnom poradí,
potom chronologicky: cena Bitcoinu nad 30 000 \$; dlhodobo by mohla dosiahnuť 140 000 \$;
nad 40 000 \$; za tri dni cena klesá; hodnota pod 30 000 \$; potom o 20 % nahor
za sedem dní. Rozpätie týchto titulkov je len **jeden mesiac** — takže je ťažké
sledovať situáciu len z titulkov. Preto myšlienka: **vykresliť dáta na ich vizualizáciu**.

Prechádzanie grafom ceny Bitcoinu v čase:

- Trend začína okolo roku **2013**. Bol tu počiatočný hype, potom cena klesla (okolo
  augusta 2015 by bol smutný niekto, kto kúpil blízko 1 000 \$).
- Ale keby ste len počkali dva roky, aj kúpa za túto cenu by vás za štyri roky
  dostala asi **o 300 % do plusu** — investície si vyžadujú čas.
- Predĺžením grafu (červená čiara označuje, kde predchádzajúci graf skončil) vstupujeme
  do volatilného obdobia; cena ďalej rástla v rokoch 2017–2018.
- Keby ste zachytili trend neskoro a kúpili za asi 12 500 \$, za pol roka až rok
  by ste boli späť na asi 2 500 \$. Mali by ste predať? Pravdepodobne nie,
  pretože by sa to opäť zmenilo.
- V roku 2021 (rok, z ktorého pochádzajú zobrazené titulky) dostala cena ďalší veľký impulz —
  pravdepodobne kvôli miernejším reguláciám a lepšiemu prijatiu obchodníkmi, väčšiemu
  verejnému prístupu na trh, ľuďom necestujúcim a majúcim „voľné peniaze"
  (stimulačné šeky) na investovanie.
- Prednášajúci ukazuje aj cenu na **logaritmickej mierke** (podobne ako Moorov zákon).
  Na logaritmickej mierke by ste boli v pokušení preložiť dáta **priamkou**
  a začať predpovedať, či cena Bitcoinu v roku 2025 bude tam, kde je teraz.
  Vizualizácia dát v inom kontexte môže odhaliť aspoň nejaké informácie.
- Neskôr: prudký pokles do roku 2023, potom zotavenie a nedávny skok okolo
  **amerických volieb** a hype okolo nich. Ďalší veľký skok sa pripisuje rozhodnutiu
  Elona Muska investovať 1 miliardu dolárov do Bitcoinu
  <!-- unclear: obrázok uvádza "one billion / 1 billion dollars" -->.

Prednášajúci uvádza, že toto **nie je** na presvedčenie kohokoľvek investovať do Bitcoinu —
osobne to nerobí, pretože sa mu nepáči, že vyčerpáva zdroje a (podľa jeho názoru) nemá
žiadnu hodnotu. Pointa je, že **rôzne aspekty v dátach spôsobujú zmeny nejakého
trendu v nejakom bode**, a je dosť ťažké zistiť, čo skutočne spôsobilo to, čo
vidíme v hodnotách dát.

### Aktívne prípady COVID na Slovensku

Ďalší trend je zadaný ako hádanka s jednotkami čísel dní (napr. deň 1 až
~33, hodnoty okolo 600–650; potom 1 až ~100 dní s predchádzajúcim trendom
obráteným; potom vrcholy počas takmer roka). Je to **počet aktívnych prípadov COVID
na Slovensku**. Medzi marcom 2020 a 21. januárom (2021) bola mierna prvá vlna, ale
**druhá vlna po lete** (okolo septembra 2020) zasiahla dosť silno.

### Denné PCR prípady a filtrácia

Súvisiace dáta: **počet denných PCR prípadov** (PCR je metóda testovania
na COVID antigén) versus dni od prvého prípadu. Prednášajúci vytvoril tento
graf v **MATLAB** z dát Národného centra zdravotníckych informácií.

Surová krivka (žltá) vykazuje **ostré skokové vrcholy**. Dôvod: počet
nových prípadov bol oveľa vyšší v **pondelok**, pretože mnohé testovacie miesta
cez víkend nepracovali, alebo ľudia strávili víkend doma s chrípkou a dali sa
otestovať v pondelok.

Ukážka témy predmetu: **ako odhaliť tento druh trendu**. Modrá krivka
robí akési **priemerovanie** — podobné **7-dennému mediánu** počtu
aktívnych prípadov používanému počas pandémie (ktorý vstupoval do statusu
„semaforu"). Nie je to nič iné ako aplikovaná **filtrácia** (ako vidno, alebo bude vidno,
v predmete „Technické prostriedky automatizácie"). Výsledky tejto filtrácie
používal aj predseda vlády.

### Nemecko — prípady vs úmrtia (korelácia)

Dáta COVID-19 z **Nemecka** (nie zo Slovenska). Prvá vlna bola mierna, druhá
oveľa ťažšia a pokračovala. **Horný graf** ukazuje počet prípadov; **dolný graf**
ukazuje počet úmrtí (ľudia, ktorí zomreli).

Postrehy z diskusie:

- Oba signály zdieľajú rovnaký základný **tvar**, najmä na začiatku —
  dve premenné (signály) sú **korelované**: keď jeden signál rastie, rastie aj
  druhý (nie nevyhnutne v rovnakom čase). Považované za dve premenné, možno to
  vidieť ako **dynamický systém / proces**, kde niečo, čo sa stalo, vyvolalo odozvu.
  **Korelácia a kauzalita nie sú to isté**, ale dáta aspoň ukazujú kvalitatívnu odozvu.
- V neskoršom vrchole (akási tretia vlna v roku 2021) nárast **nie je taký výrazný
  v počte úmrtí**. Možné vysvetlenia: **očkovanie** (začalo okolo februára 2021); **mutácia vírusu**,
  ktorá nebola taká smrteľná; a akási **nadobudnutá odolnosť** v populácii (ľudia mohli
  byť infikovaní viackrát).

### Skreslenie prežitia — lietadlá z druhej svetovej vojny

Klasický obrázok: v druhej svetovej vojne bol inžiniersky problém, ako
dostať viac lietadiel späť bezpečne z boja. Graf ukazuje, zo zbierky
vracajúcich sa lietadiel, **kde boli lietadlá zasiahnuté a predsa sa vrátili**.

Paradox: mali by sme spevniť časti, ktoré **sú** zasiahnuté, alebo časti,
ktoré zasiahnuté **nie sú**? Dáta hovoria, že by sme mali spevniť časti, ktoré
**nie sú** zasiahnuté — to je **skreslenie prežitia**. Lietadlá zasiahnuté na
označených miestach sa vrátili domov, takže tieto oblasti znesia poškodenie;
lietadlá, ktoré sa **nevrátili**, boli zasiahnuté inde (napr. motor, pilot alebo
úzka kritická časť). Naivná, sentimentálna reakcia by posilnila viditeľne zasiahnuté miesta,
ale to by nepomohlo. Toto je jeden z veľmi skorých **problémov rozhodovania na základe dát**:
ako pochopiť dáta a podľa toho konať na zlepšenie nejakého výkonu.

### Dáta lekárskeho skríningu

Okrem kardiogramu mnohé **skríningové techniky** v medicíne produkujú tento
druh dát (napr. skenovanie na nádor, röntgen na zlomeniny kostí alebo dentálne
problémy). Množstvo dát rastie, ale počet zručných lekárov, ktorí to dokážu čítať,
nerastie tak rýchlo — preto musíme niečo urobiť. (Prednášajúci spomína študenta, ktorý
hľadá letný stáž v Siemens Healthineers <!-- unclear: popis znie "seens healthy years" -->,
pracujúceho na tomto type problému.) Kroky zahŕňajú najprv **digitalizáciu** dát,
ktoré môžu existovať len na papieri perom/atramentom, a potom hľadanie trendov na
uvažovanie o tom, čo sa stalo, o stave pacienta, diagnóze a liečbe.

### Výroba elektriny vs intenzita CO₂ podľa krajiny

Graf **výroby elektriny vs intenzita CO₂ podľa krajiny**. Každý bod je
vzorkovaný každú **jednu hodinu**: množstvo elektriny vyrobenej elektrárňami
krajiny a intenzita CO₂ (koľko CO₂ sa emituje do atmosféry touto výrobou).
Zobrazené krajiny zahŕňajú Francúzsko, Nemecko, Poľsko, Taliansko, Španielsko,
Belgicko, Portugalsko (Slovensko nie je zobrazené).

Závery z diskusie:

- **Poľsko** je najmenej efektívne (najvyššie CO₂) — má veľa uhlia a mnoho
  uhoľných elektrární. Jeho výroba elektriny je tiež oveľa **užšia** (menej
  flexibilná).
- **Francúzsko** využíva veľa **jadrovej** energie. Je to zaujímavé, pretože **bez
  ohľadu na to, koľko energie je potrebné, emituje zhruba rovnaké množstvo CO₂** —
  čo ukazuje efektívnosť / ekologickú šetrnosť jadrových elektrární.
  Francúzsko je tiež relatívne flexibilné vo výrobe, pričom zostáva na
  environmentálne šetrnom konci.
- **Nemecko** ukazuje zaujímavý trend pozdĺž osi s **záporným sklonom /
  zápornou deriváciou**: pri výrobe relatívne **malého** množstva energie sú emisie CO₂
  **vysoké**, ale pri výrobe **veľkého** množstva energie sú emisie CO₂ **nižšie**.
  To je na prvý pohľad akosi paradoxné. Vysvetlenie: je to efekt **uhoľných elektrární**
  bežiacich aj keď obnoviteľné zdroje nepracujú. Vysoká výroba prichádza cez deň —
  vrcholy dobrého vetra pre veterné turbíny a jasné dni pre solárne články.

## Typy vizualizácie dát

Príklady vedú k rôznym typom vizualizácie dát. Počnúc od zozbieraných dát,
už len použitie rôznych grafov môže odhaliť poznatky. Prednášajúci zdôrazňuje
štyri bežné typy.

### Časový rad

Akýkoľvek signál / trend / informáciu, ktorú máte, zobrazíte oproti zodpovedajúcemu
**časovému kroku** na vodorovnej osi. To bolo robené v predmete „Teória automatického riadenia"
a v celej tejto prednáške.

- Niekedy **nie sú časové razítka** (napr. graf s elektrinou), takže nevieme presne,
  kedy každý bod nastal — vieme len **interval vzorkovania** (napr. body sú od seba hodinu).
- Keď **vieme** časové razítko, môžeme o ňom uvažovať. Prednášajúci dáva
  príklad 15-minútových dát zo závodu, kde sa dátové body zdanlivo **zdvojnásobili**
  (dve hodnoty pre jednu hodinu). Príčinou sa ukázal byť **prechod na letný/zimný čas**:
  pri prepnutí časy bežali 2:00, 2:15, 2:30, 2:45, 3:00, potom opäť 2:00 — praktická
  výzva, s ktorou sa môžete stretnúť.
- Pri časových radoch môže byť tiež ťažké pozorovať **korelácie**, keď je len niekoľko premenných.

### Bodové / korelačné grafy

Tu vezmeme dve premenné a vykreslíme jednu oproti druhej, **strácame zmysel
pre čas** (už nevieme, kedy bol každý bod zozbieraný, len že pár nastal spolu).

- **Pozitívna korelácia:** ak premenná na vodorovnej osi rastie, rastie aj
  druhá premenná (pohybom doprava sa pohybujeme aj nahor). Môžete si predstaviť
  aproximáciu oblaku bodov priamkou s kladným sklonom. Jedna os sa javí ako funkcia druhej.
- **Záporná korelácia:** prípad Nemecka je príkladom — väčšia výroba elektriny
  ide ruka v ruke s nižšími emisiami CO₂.
- **Centrovanie:** graf môže byť nakreslený tak, že počiatok je presunutý na
  miesto najčastejšej hodnoty (**priemer**). Po centrovaní sú pozitívne a
  negatívne odchýlky od priemeru priamo viditeľné a je ľahšie vidieť,
  napr., že zvýšenie vodorovnej hodnoty o 2 zvyšuje zvislú hodnotu o
  10. To je oveľa ťažšie čítať z absolútnych čísel (čo znamená „600 g CO₂
  ekvivalent" — je to veľa alebo málo?). Vizualizácia teda nie je len o
  *tom, ako kreslím graf*, ale aj *o tom, ako transformujem premenné* (logaritmickú
  transformáciu sme už videli pri cene Bitcoinu).

### Histogramy

Histogram zobrazuje, ako **hustá** je dáta v určitých oblastiach — ako
často sa vyskytujú určité hodnoty. Funguje ako vytváranie **priečinkov** („košov"): pre
priečinok uprostred spočítajte, koľko bodov padá napríklad medzi −0,1 a +0,1;
počet je ako hádzanie kamienka/guľôčky do stĺpca. Priamo to ukazuje, že niektoré
hodnoty sú úplne nepravdepodobné alebo nikdy nepozorované, zatiaľ čo iné sú
pravdepodobnejšie. Tvar môže začať vyzerať ako slávna **Gaussova krivka**.

V kombinovanom pohľade bodový graf+histogram červené oblasti označujú veľmi
pravdepodobné miesto výskytu bodov, zatiaľ čo modrá môže reprezentovať
**odľahlé hodnoty** alebo oveľa menej pravdepodobné hodnoty (napr. body ďaleko od
priemeru, so zápornými odchýlkami). Bodový graf môže ukazovať **takmer žiadnu koreláciu**:
aplikáciou testu „ak mierne zvýšime vodorovnú premennú, čo sa stane so zvislou?"
nedostaneme jasnú odpoveď (existujú rastúce aj nerastúce smery). Histogramy pozdĺž každej
osi potom ukazujú hustotu hodnôt v každej premennej osobitne.

### Paritné grafy

Paritné grafy sú menej bežné, ale užitočné. Problémom predchádzajúcich grafov
je, že musíte zvoliť relatívne **malý počet premenných** na zobrazenie
(dve, alebo maximálne tri dimenzie), takže nemôžete ľahko vizualizovať mnoho
premenných. Jednou z možností, ktorú paritný graf ponúka, je vykresliť **pozorovaný trend
oproti tomu, ako ho predpovedá váš model / pochopenie**.

Konkrétny príklad: **jas pixelov** na dvoch fotografiách toho istého
objektu nasnímaných asi **4 hodiny** od seba, s hodnotami jasu medzi 0 a 0,5
(biela vs čierna). Obe premenné majú rovnakú jednotku, ale jedna je **skutočné
pozorovanie** a druhá je **predpoveď** tejto premennej (alebo inej
premennej, ktorú sa snažíme korelovať). Farebné podfarbenie podobné histogramu ukazuje,
kde leží mnoho pixelov: modré body sú menej pravdepodobné hodnoty, červená je miesto,
kde je veľa pixelov. Pozdĺž priamky $y = x$ môžeme vidieť podobnosť dvoch fotografií:
ak má pixel jas 0,1 na jednej fotografii a rovnaká situácia je zachytená, tento bod leží
blízko priamky $y = x$. Graf ukazuje, že obe fotografie sú veľmi podobné, líšia sa
len nejakým šumom alebo malými zmenami. (Študenti budú robiť experimenty s paratnými
grafmi počas cvičení.)

## Záver

Prednášajúci preskočí záverečný snímok pre daný deň, pozve otázky a komentáre
a opýta sa študentov na ich názor na prednášku a na to, že prebieha v angličtine.
Poznamenáva, že **YouTube video je po prednáške spracované** so **subtitrami**
a že študenti môžu dokonca **stiahnuť prepis** prednášky, aby im pomohol.
