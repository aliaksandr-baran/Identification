---
lecture: L08
title: "Filtrácia dynamických signálov"
course: Identifikácia
source: "https://www.youtube.com/watch?v=nAS4yAqv5ak"
---

# L08 — Filtrácia dynamických signálov

> Vzorce overené podľa prednášateľových snímok (*Notes_250416*): pásmo σ-limitu,
> kovariančná elipsa, prenosová funkcia dolnopriepustného filtra a
> kĺzavý priemer / FIR filter a jeho zosilnenie.

## Premostenie statiky a dynamiky

Doteraz sa kurz venoval v podstate **statickým** systémom — meraniu teploty,
tlaku a pod. v (takmer) ustálenom stave, budovaniu statických modelov, odhadu
konštanty. Identifikácia sa v skutočnosti týka **dynamických systémov**. Dnešným
premostením medzi statickou analýzou dát a dynamickými systémami je **filtrácia**.

**Dolnopriepustný filter** (angl. *low-pass filter*) „prepúšťa nízke" — prepúšťa
**nízke frekvencie**. Signál možno rozložiť na **vysokofrekvenčnú** zložku
(rýchlo, takmer periodicky sa meniaca časť — šum) a **nízkofrekvenčnú** zložku
(trend v dátach). V ideálnom prípade:

- **Dolnopriepustný filter** vráti trend a vynechá šum.
- **Hornopriepustný filter** vráti šum — povie nám (na prvej úrovni) **ako veľký
  je šum**, prípadne **kedy sa signál mení**.

## Filtrácia v statickom prípade — odľahlé hodnoty

Pri vykresľovaní zozbieraného časového radu (teplota, tlak) môžeme zaznamenať
podozrivú hodnotu — **odľahlú hodnotu** (outlier). Možnosti:

- **Odstrániť** dotknutý úsek (napr. posledných 100 meraní). Ak chceme iba model
  ustáleného stavu a ostatné signály v danom okne vyzerajú normálne, môžeme toto
  okno odstrániť naprieč signálmi, aby zostali **zarovnané**.
- **Odstrániť a nahradiť.** Odľahlú hodnotu nahradiť pomocou dát — napr. priemerom
  **poslednej dobrej hodnoty pred** a **prvej dobrej hodnoty po** odľahlej hodnote
  (interpolácia), prípadne priemerom minulých hodnôt. Všetko sú tu minulé dáta
  (spracúvané o rok neskôr), takže interpolácia je legitímna; náhrada by mala
  zostať v rozumnom rozsahu, aby sme nezahodili inak dobré dáta.

### Automatická detekcia odľahlých hodnôt

Pre 10 000 signálov je vykresľovanie nepraktické, preto detegujeme automaticky:

- **Rýchlosť zmeny signálu** — označiť náhlu zmenu gradientu/derivácie. **Pozor na
  šum**, ktorý zvyšuje deriváciu; dobre naladený hornopriepustný filter hlási šum,
  ale zároveň označí **náhlu** zmenu (derivácia vyššia ako zvyčajne).
- **Signál mimo limitov** — označiť hodnoty mimo prijateľných limitov, získaných z:
  - **Fyzikálnych limitov** (napr. teplota reaktora nemôže byť −200 K), alebo
  - **Štatistických limitov.** Odľahlá hodnota je niečo zriedkavé, čo nezodpovedá
    našim predpokladom o signáli. Vypočítame stredný hodnotu a smerodajnú odchýlku
    a použijeme pásmo (snímka):

$$
[\,\bar{y} - 3\sigma_y,\; \bar{y} + 3\sigma_y\,]
$$

  Dobrá prax: po odstránení odľahlej hodnoty **prepočítame** strednú hodnotu a
  smerodajnú odchýlku; ak sa príliš nezmenia, odstránený bod bol skutočne odľahlý
  a neovplyvnil štatistiku (odľahlá hodnota ponechaná v dátach posúva strednú
  hodnotu aj σ).

## Viacrozmerný prípad

Jednorozmerná analýza sa pozerá na jeden signál naraz a ostatné ignoruje.
Uvažujme teplotu a tlak v čase, ktoré **korelujú**. „Hrb", kde oba súčasne
stúpajú, **nie je** chybou senzora — je to normálna, ale nezvyčajná prevádzková
situácia. V **korelačnom grafe** (T oproti P) leží pozdĺž očakávaného trendu
korelácie.

**Kĺzavý priemer** robí limity **dynamickými**: malé, keď je signál stabilný,
väčšie, keď sa signál mení. (V pohyblivom okne predpokladáme, že prechodové javy
z ďalekej minulosti sú preč a neovplyvňujú prítomnosť; stredná hodnota a σ sa
počítajú z posledných hodnôt okna.) Bod označený ako odľahlý voči pevným
historickým limitom môže byť v poriadku voči pohyblivému pásmu.

Pomocou **kovariančnej matice** (ako pri parametroch regresie) normalizovaná
odchýlka bodu sleduje chi-kvadrát rozdelenie, čím dostaneme **konfidenčnú
elipsu**. Testovací kritérium (snímka):

$$
(x - \bar{x})^T V^{-1} (x - \bar{x}) \le \chi^2_{N,\alpha},
  \qquad V = \frac{1}{N-1} X^T X
$$

Tu $x$ je vektor teploty a tlaku pre daný dátový bod. Ak nerovnosť platí, bod leží
**vo vnútri elipsy** — konzistentný s historickými dátami, aj keď sú teplota aj
tlak súčasne vysoké. Porovnajme s **pevnými limitmi obdĺžnika** na každú premennú
zvlášť: bod s **nízkou teplotou, ale bežným tlakom** môže byť vo vnútri obdĺžnika,
a pritom **mimo očakávaného korelačného trendu** — elipsa ho zachytí, obdĺžnik nie.
Toto presahuje úzke konštantné limity, využíva minulé korelácie a je ľahko
použiteľné a testovateľné.

## Skutočný dynamický prípad

„Rozprávka": nevinný **pôvodný signál** (skutočná teplota vo vnútri reaktora —
to, čo by nameraval *dokonalý* senzor) je otrávený záporákmi, **šumom merania
(senzora)**. Oba sa skombinujú do **nameranej odozvy** — a my priamo nepoznáme
ani jednu zo zložiek. Napriek tomu je signál v meraní často stále viditeľný voľným
okom.

Privedenie skutočného signálu cez filtre:

- **Hornopriepustný filter** rekonštruuje aproximáciu šumu (nikdy dokonalú — dve
  časti informácie boli skombinované) a stále nesie nejakú informáciu o **zmenách**
  pôvodného signálu.
- **Dolnopriepustný filter** rekonštruuje aproximáciu trendu — lepšiu než bez
  filtrácie, ale zaostáva tam, kde sa pôvodný signál mení **rýchlo** (filter hovorí
  „ak sa meniš tak rýchlo, neprepustím ťa"), a rýchle rysy sú stratené.

## Filtre ako prenosové funkcie

Prechod od stredných hodnôt/priemerov k **prenosovým funkciám diskrétneho času**.

### Dolnopriepustný filter ako systém prvého rádu

Uvažujme surový vstup, ktorý skočí z 0 na 1. Filter by **nemal** okamžite
skočiť (jeden vzorkový bod môže byť len impulz, ktorý nechceme nasledovať) —
mal by reagovať plynule, ako **prechodová charakteristika**. Je to systém prvého
rádu so **zosilnením 1** (snímka):

$$
G(s) = \frac{1}{T s + 1}
$$

Zosilnenie je 1, pretože dlhodobo, ak je signál konštantný, filter musí vrátiť
ten istý signál (0 → 0, trvalá 1 → 1). Je tu **jeden parameter** — **časová
konštanta** $T$: jej zmena robí filter ľubovoľne pomalým alebo rýchlym a určuje,
koľko vysokých frekvencií sa odreže. Každý dynamický systém funguje ako filter
(hladina v dvojici nádrží nereaguje okamžite na zmenu prítoku). Pre **vyšší rád**
je lepšie pracovať vo **frekvenčnej oblasti** — takto tlmenie zvuku tlmí
konkrétne frekvencie.

### Spojenie so štatistikou: príklad COVID

Modrá krivka je počet **denných PCR prípadov** s periódou vzorkovania **jeden
deň**. Je veľmi **zúbkovaná**: nie preto, že by prípady skutočne kolísali od 7 000
do 2 000, ale kvôli **akumulácii** — testovanie/hlásenie bolo nízke cez víkendy
(nedeľa najnižšie) a kopilo sa v **pondelok** (rovnomerne rozmiestnené veľké
špičky). Pre rozhodnutia (zatvorenie podnikov, systém „semaforu") sa používala
**červená krivka** — **7-dňový kĺzavý priemer** — nie surové modré čísla.

(Na okraj: priemer vs. medián závisí od predpokladaného rozdelenia šumu —
priemer je optimálny pre **Gaussov** šum, medián pre **Laplaceov**; medián sa
uprednostňuje aj pri nesymetrických dátach, ako sú mzdy, kde mnohí zarábajú
minimálnu mzdu.)

## Filter kĺzavého priemeru

Pre $m$-dňový kĺzavý priemer výstup $y_k$ v čase $k$ spriemeruje $m$ hodnôt.
Vrátane aktuálnej hodnoty (snímka):

$$
y_k = \frac{1}{m}\sum_{i=0}^{m-1} u_{k-i}
$$

Vylúčenie aktuálnej hodnoty dáva **predikciu** (len s minulými hodnotami, pred
tým, ako je dnešné číslo známe):

$$
y_k = \frac{1}{m}\sum_{i=1}^{m} u_{k-i}
$$

(Pozor na počítanie indexov: sčítanie $m+1$ hodnôt a delenie $m$ by nebol priemer;
preto sú limity vyššie také, aké sú.)

Zovšeobecníme rovnaké váhy $\tfrac{1}{m}$ na ľubovoľné váhy $b_i$:

$$
y_k = \sum_{i=1}^{m} \frac{1}{m}\, u_{k-i}
  \qquad\longrightarrow\qquad
  y_k = \sum_{i=1}^{m} b_i\, u_{k-i}
$$

- **Filter kĺzavého priemeru:** všetky váhy rovnaké, $b_1 = b_2 = \dots = b_m$,
  pričom $\sum_{i=1}^{m} b_i = 1$. (Pre $m = 3$: $b_1 + b_2 + b_3 = 1$ pri
  rovnakých váhach vyžaduje $b_i = \tfrac{1}{3}$ — teda $\tfrac{1}{m}$.)
- **Vážený filter kĺzavého priemeru:** zachovajte $\sum_{i=1}^{m} b_i = 1$, ale
  dovoľte nerovnaké váhy s $b_i \ge 0$ pre všetky $i$. Príklad ($m = 3$):
  $b_1 = \tfrac{1}{4}$, $b_2 = \tfrac{1}{2}$, $b_3 = \tfrac{1}{4}$ — stredný
  (alebo najpresnejší) deň má väčšiu váhu.

## Konečná impulzná odozva (FIR)

Model

$$
y_k = \sum_{i=1}^{m} b_i\, u_{k-i}
$$

sa nazýva filter s **konečnou impulznou odozvou (FIR)**.

### Jeho prenosová funkcia

Pomocou operátora spätného posunu $z^{-i}$ (teda $u_{k-i} \leftrightarrow z^{-i}$;
$u_k$ zodpovedá $z^0 = 1$, bez posunu):

$$
Y(z^{-1})\,z^{0} = \left(\sum_{i=1}^{m} b_i\, z^{-i}\right) U(z^{-1})
$$

Vydelením ľavej aj pravej strany výrazom $z^0$ dostaneme prenosovú funkciu
(čitateľ sú vážené posuny, menovateľ je 1):

$$
G(z^{-1}) = \frac{Y(z^{-1})}{U(z^{-1})} = \frac{\sum_{i=1}^{m} b_i\, z^{-i}}{z^{0}}
  = \sum_{i=1}^{m} b_i\, z^{-i}
$$

### Zosilnenie

Zosilnenie nájdeme dosadením $z = 1$ (diskrétny ekvivalent $s = 0$ v spojitom
čase, cez $z = e^{T s}$):

$$
\text{zosilnenie} = \sum_{i=1}^{m} b_i
$$

Keďže filtre kĺzavého priemeru a váženého kĺzavého priemeru vyžadujú
$\sum b_i = 1$, ich **zosilnenie je 1** — presne zosilnenie dobrého
dolnopriepustného filtra.

**Upozornenie na ďalší krát:** porušíme pravidlo $\sum b_i = 1$, takže filter
môže predstavovať **ľubovoľné zosilnenie**, ako aj **ľubovoľnú časovú konštantu**
a **ľubovoľný rád** systému.
