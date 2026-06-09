---
lecture: L07
title: "Praktické aspekty lineárnej regresie"
course: Identifikácia
source: "https://www.youtube.com/watch?v=HqCN0mFgmTQ"
---

# L07 — Praktické aspekty lineárnej regresie

> Vzorce overené podľa príslušnej sady snímok (*Identification L07 — Practical
> aspects of lin reg*). Počas záznamu si prednášateľ nebol istý konštantou vo výsledku
> kovariančnej matice parametrov; snímka uvádza čistý tvar
> $V_P = \sigma_y^2 (X^TX)^{-1}$, ktorý je použitý nižšie.

Táto prednáška je prevažne praktická. Priebežným príkladom je **destilačná kolóna**
s mnohými meranými teplotami, tlakmi a niekedy aj zloženiami; typickým cieľom je
predpovedať **zloženie** destilátu alebo spodného prúdu, čo fyzikálna chémia
(rovnováhy para–kvapalina) uvádza ako korelované s teplotou a tlakom. Problémom je
**nadbytok** meraní.

## Výber členov modelu

Predikčný model je $\hat{y} = X p$. Stĺpce $X$ môžu byť teplota na prvom tanieri,
teplota na druhom tanieri, tlak na vrchu, tlak na dne atď. — vrátane **nelineárnych
transformácií**: súčinov, pomeru destilátu k nástrektu $D/F$ alebo $e^{T}$
(Arrheniov zákon). Jednoduchšou verziou je **polynóm** v jednej premennej:

$$
\hat{y} = p_0 + p_1 x + p_2 x^2 + p_3 x^3 + \dots
$$

(Pri dvoch premenných by pribudli krížové členy.) Otázkou je, ako **vybrať** rozumné
členy.

## Korelácia verzus závislosť

Nadväzujúc na pojem korelácie z minulej prednášky: je „korelovaný" to isté čo
„závislý"? Nie — ide o **jednostrannú implikáciu** (snímka):

$$
\text{korelácia} \;\Longleftarrow\; \text{závislosť (kauzalita)}
$$

Ak sú premenné **závislé**, z toho **plynie** korelácia (mali by sme ju vidieť
v korelačnom koeficiente). **Korelácia však neznamená závislosť** — spomeňme si
na príklad so študentmi v zahraničí, kde boli čísla korelované iba preto, že
pandémia COVID ich všetky naraz znížila.

### Korelácia medzi vstupmi je nežiaduca; so výstupom je žiaduca

- **$x_1, x_2$ korelované — nežiaduce.** Korelácia *medzi nezávislými premennými*
  (kolinearita) je problém.
- **$x_1, y$ korelované — žiaduce.** *Chceme*, aby vstup koreloval s výstupom, ktorý
  predpovedáme; inak by parameter mohol nadobudnúť v podstate náhodnú hodnotu
  nesúvisiacu s realitou.

### Prečo je kolinearita škodlivá

Predpokladajme model s dvomi vstupmi $\hat{y} = p_1 x_1 + p_2 x_2$, pričom nám nie
je známe, že $x_1 = k\,x_2$ (dva blízke tanier destilačnej kolóny sú silne
korelované, alebo bol experiment vedený tak, že teplota a tlak sa vždy zvyšovali
spolu). Dosadením:

$$
\hat{y} = p_1 k\, x_2 + p_2 x_2 = (p_1 k + p_2)\, x_2
$$

Existuje iba **jeden** efektívny parameter. Ak napr. $k = 1$ a skutočná hodnota závorky
je $3$, potom akékoľvek $p_1, p_2$ s $p_1 + p_2 = 3$ je platným výsledkom regresie —
$(1, 2)$, $(\tfrac{1}{2}, 2\tfrac{1}{2})$, $(-5, 8)$, … — nežiaduci **extra stupeň
voľnosti**, ktorý robí „fyzikálne" parametre bezvýznamnými.

Geometricky (3D): dáta ležia pozdĺž priamky v rovine $x_1$–$x_2$ a **ľubovoľná
rovina otočená okolo tejto priamky** fituje rovnako dobre — fit nie je jednoznačný.
Keď sú body dobre rozprestreté, je ťažké rovinu od dát odkloniť. Liek: zostrojíme
kovariančnú maticu, skontrolujeme korelácie a **odstránime korelované nezávislé
premenné**, pričom $x_1, x_2$ zachovávame čo najnezávislejšie.

## Polynomický fit, preučenie a extrapolácia

Pri polynomickom fite jednej premennej na rozptýlené dáta:

- **Lineárny** fit nemusí byť zlý — reziduá môžu vyzerať ako normálny šum merania.
- **Kvadratický** fit môže sledovať väčšinu bodov.
- **Oktický** fit (8. stupňa) prechádza takmer každým bodom — ale **fituje šum**,
  čo nechceme. Chceme fitovať *informáciu* obsiahnutú v dátach, nie šum.

**Neextrapolujte.** Mimo trénovacieho rozsahu polynóm vysokého stupňa divoko uniká.
Dokonca **lineárny** model možno extrapolovať len málo (napr. zdvojnásobenie
intervalu je už príliš ďaleko). Zbierajte dáta v **celom rozsahu**, kde musí model
platiť — inak zmena prevádzky zariadenia (iná ropa, surovina od iného dodávateľa)
spôsobí, že model zlyhá a „šéf vám povie, že to nefunguje."

Prečo vôbec skúšať polynómy? Kvôli **Taylorovmu rozvoju** — každú nelineárnu funkciu
možno aproximovať polynómom, takže polynómy sú dobrými aproximátormi. S fyzikálnou
intuíciou (destilácia) možno odhadnúť tvar (exponenciálny, logaritmický); pri
veciach ako cena Bitcoinu je skutočná podstata oveľa ťažšie poznateľná.

## Krížová validácia

Na výber zložitosti modelu používame **krížovú validáciu**: dáta rozdelíme (pomer
zo snímky **50 : 30 : 20**) na

- **Trénovacie (TR)** — použité na výpočet hodnôt parametrov;
- **Validačné (V)** — použité na rozhodnutie o ráde/zložitosti modelu;
- **Testovacie (TS)** — typicky ~20 %, uzamknuté „v trezore" pred všetkým ostatným
  a použité iba na **záverečné** hodnotenie výkonnosti (akoby model prešiel do
  prevádzky).

Vynesieme výkonnostný ukazovateľ (napr. RMSE) v závislosti od zložitosti modelu
$n_p$ (počtu parametrov):

- **Trénovacia** chyba **monotónne klesá** s pridávaním členov — optimalizácia nás
  stále teší, aj pri fitovaní šumu (oktický fit), takže samotné trénovacie dáta
  najlepší model nikdy neodhalí.
- **Testovacia / validačná** chyba **najprv klesá, potom rastie**, čím odhalí
  optimálnu zložitosť $n_p^{*}$. Keďže skutočné testovacie dáta sú skryté,
  **validačné** dáta ich pri rozhodovaní o ráde simulujú.

## Kritériá hodnotenia

Nespoliehajte sa na jedno číslo; pre každý kandidátny model skontrolujte niekoľko.

### Koreň strednej kvadratickej chyby (RMSE)

$$
\text{RMSE} = \sqrt{\frac{1}{N}\sum_{k=1}^{N}\big(y_k - \hat{y}_k\big)^2}
$$

(niekedy RMSPE, koreň strednej kvadratickej **predikčnej** chyby). Žije v jednotkách
dát — „náš model sa mýli o 0,01 bar."

### Koeficient determinácie $R^2$

Porovnáva model s jednoduchým fitom **konštantou** (priemerom dát):

$$
R^2 = 1 - \frac{\sum_{k=1}^{N}(y_k - \hat{y}_k)^2}{\sum_{k=1}^{N}(y_k - \bar{y})^2}
$$

Konštantný fit v menovateli je priemer $\bar{y}$. Keď je reziduálny súčet modelu
(čitateľ) malý voči súčtu konštantného fitu (menovateľ), $R^2 \to 1$. Konštrukčne
$R^2 \in [0, 1]$ (1 = dokonalý, 0 = nič lepšie ako konštanta). **Záporný** $R^2$
signalizuje **chybu** pri fitovaní modelu.

### Paritný graf

Vynesieme **predikciu oproti meraniu** (paritný / korelačný graf). Užitočný aj vtedy,
keď viac ako dve alebo tri nezávislé premenné robia iné grafy nepraktickými.

- Body na **diagonále** $\hat{y} = y$ (s výnimkou šumu) — **dobré**, veľmi žiaduce.
- Konzistentný **posun pri správnom trende** (predpoveď väčšia → meranie väčšie,
  ale posunuté) — **chýbajúci regresor / vstup**: nejaká závislosť (napr. od tlaku)
  bola opomenutá.
- Tvar **dobrý a potom sa odchyľujúci** — pravdepodobne **nelineárne správanie**
  nezahrnuté v modeli.

## Intervaly spoľahlivosti parametrov

Pri dostatku dát štatistika funguje dobre a intervaly spoľahlivosti môžu
signalizovať **preučený** parameter: ak interval **obsahuje nulu**, model sa môže
zaobísť bez tohto parametra pri rovnakej úrovni pravdepodobnosti.

Zostrojíme **kovariančnú maticu parametrov** analogicky ku kovariancii dát:

$$
V_P = E[P P^T], \qquad
V_P = \begin{pmatrix} \sigma_{p_1}^2 & \sigma_{p_1 p_2} & \cdots \\
                      \sigma_{p_1 p_2} & \sigma_{p_2}^2 & \\
                      \vdots & & \ddots \end{pmatrix}
$$

($P$ je $n_p \times 1$, teda $P P^T$ je matica $n_p \times n_p$.) Dosadíme
$P = (X^T X)^{-1} X^T y$ a jeho transponovaný $P^T = y^T X (X^T X)^{-1}$
(s využitím symetrie $X^T X$):

$$
V_P = E\!\left[(X^T X)^{-1} X^T y\, y^T X (X^T X)^{-1}\right]
$$

Predpokladáme **nezávislý, konštantný šum merania**, teda $E[y y^T] = V_y =
\sigma_y^2 I$. Vytiahnutím $\sigma_y^2$ sa vnútorné $X^T X$ skráti s jedným
$(X^T X)^{-1}$ (pár $A^{-1} A$):

$$
V_P = \sigma_y^2\, (X^T X)^{-1}
$$

**Interpretácia:** neistota parametrov rastie so šumom $\sigma_y^2$ a — kvôli
inverzii — **klesá s pribúdajúcimi meraniami**, keď $X^T X$ rastie (podobne ako pri
odhade konštanty). Závisí tiež od **návrhu experimentu** (výberu nezávislých dát):
ak body ležia na priamke, $X^T X$ nie je invertovateľná (vyššie opísaný problém
kolinearity).

### Rozdelenie parametrov a elipsa spoľahlivosti

Ak $P$ chápeme ako náhodný vektor, $P \sim N(\hat{P}, V_P)$, hustota
pravdepodobnosti viacrozmerného Gaussovho rozdelenia (maticová generalizácia skalárneho
$\frac{1}{\sqrt{2\pi}\,\sigma}e^{-(x-\bar{x})^2/2\sigma^2}$) je:

$$
\text{pdf}(p) = \frac{1}{(\sqrt{2\pi})^{n_p}\,\lvert V_P^{1/2}\rvert}\,
  e^{-\frac{1}{2}(p - \hat{P})^T V_P^{-1}(p - \hat{P})}
$$

Tu $2\pi$ nesie exponent (normalizácia vo viacerých premenných) a skalárne $\sigma$
sa stáva **maticovou odmocninou** kombinovanou s **determinantom**, čím dostaneme
jedno číslo. Exponent je **kvadratická forma** s $V_P^{-1}$ namiesto delenia
rozptylom.

„Svietenie baterkou" pozdĺž osi $p_1$ premieta (marginalizuje) viacdimenzionálny
zvon späť na jednorozmerné Gaussovo rozdelenie pre $p_1$ (a obdobne pre $p_2$).
**Vrstevnice** hustoty pravdepodobnosti sú **elipsy**; graf vrstevníc ukazuje
napríklad, že **rozptyl $p_1$ je oveľa väčší ako rozptyl $p_2$** — dáta/model
určili $p_2$ presnejšie.

Rovnako ako v skalárnom prípade kvadratická forma sleduje **chí-kvadrát** rozdelenie
s $n_p$ stupňami voľnosti, čím dostaneme **oblasť spoľahlivosti** (snímka):

$$
(p - \hat{P})^T V_P^{-1}(p - \hat{P}) \sim \chi^2_{n_p}
$$

$$
(p - \hat{P})^T V_P^{-1}(p - \hat{P}) \le \big(\chi^2_{n_p,\alpha}\big)^{-1}
$$

Toto je maticová analógia kružnice $p_1^2 + p_2^2 = r^2$ zovšeobecnená na elipsu
$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$: dĺžky poloosí pochádzajú z intervalov
spoľahlivosti (polomerov) a mimdiagonálne prvky elipsu **naklonia / otočia**.
(Vykreslenie tejto elipsy je cvičenie; podrobnosti nabudúce.)

**Varovný signál — interval obsahuje nulu.** Ak je 95% interval spoľahlivosti
napr. $p \in [-1, 2]$, potom všetky hodnoty medzi $-1$ a $2$ sú s 95% pravdepodobné,
**vrátane nuly**. Model sa môže zaobísť bez tohto parametra — premenná môže byť
nepozorovateľná (lineárna závislosť), nedostatočne odhalená dátami alebo jednoducho
nemá žiadny kauzálny vplyv na výstup.

## Analýza hlavných komponentov (PCA)

Metóda veľmi často používaná v analýze dát, ukázaná na príklade. Vezmeme 100
čiernobielych fotografií tvárí (Steven Tyler, George Bush, Robbie Williams, …),
každý pixel s hodnotou v $[0, 1]$ (0 = čierna, 1 = biela). Pri ~10 000 pixeloch na
snímku je dátová matica

$$
X \in \mathbb{R}^{100 \times 10000}
$$

— iba **100 pozorovaní**, ale **10 000 premenných**. Predikčný model po pixeloch

$$
\hat{y} = p_1 x_1 + p_2 x_2 + \dots + p_{10000}\, x_{10000}
$$

by potreboval 10 000 parametrov, ale z 100 dátových bodov sa nedá naučiť 10 000
parametrov (rovnako ako na fit priamky treba aspoň dva body, na 10 000 parametrov
treba aspoň 10 000 bodov).

**PCA** vykoná štatistiku na dátach a zostrojí malý počet **nezávislých, najpravdepodobnejších
kombinácií** pixelov — tu **36 komponentov „eigentváre"**
$\tilde x_1, \dots, \tilde x_{36}$ (napr. prvý zachytáva spoločnú farbu pozadia).
Redukovaný model potom potrebuje iba **36 parametrov**:

$$
\hat{y} = p_1 \tilde{x}_1 + \dots + p_{36}\,\tilde{x}_{36}
$$

Rekonštrukcia snímok z týchto komponentov dáva rozpoznateľné aproximácie — dostatočné
napríklad na rozlíšenie dvoch ľudí — **bez** fitovania 10 000 parametrov (väčšina z
nich by mala interval spoľahlivosti obsahujúci nulu). Základná matematika je pomerne
jednoduchá a je ponechaná na nabudúce.
