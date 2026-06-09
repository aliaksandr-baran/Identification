---
lecture: L02
title: "Úvod do štatistiky"
course: Identifikácia
source: "https://www.youtube.com/watch?v=laEQig6EanE"
---

# L02 — Úvod do štatistiky

> Vzorce a slovenská terminológia nižšie sú zapísané tak, ako boli uvedené na
> prednáške; kde ich titulky skomolili, boli rekonštruované z vlastných snímkov
> prednášajúceho (*Ident 24 02 2026*) a poznačené priamo v texte.

## Prečo štatistika — modelovanie zašumených dát

Minule sme videli, že náš svet je plný dát, ale **tieto dáta nie sú vždy
spoľahlivé** — v meraniach je vždy nejaký šum (viditeľný v mnohých laboratórnych
cvičeniach). Niekedy ide o **systematickú chybu** (napr. niekto neprekalibroval
prístroj); existuje aj štandardná chyba vznikajúca z množstva malých chýb, ktoré
sa kumulujú do šumu merania. Napriek týmto problémom by sme mali byť schopní dátam
porozumieť — nájsť **model**, nejakú funkciu alebo algoritmus, ktorý dátam dáva
zmysel.

O tom je **modelovanie na základe dát**, a **identifikácia systémov** je jeho
súčasťou (odtiaľ názov predmetu). Identifikácia systémov sa týka špeciálne
**dynamických systémov**; nezačneme s nimi hneď, ale budeme do nich prechádzať
postupne.

Rekapitulácia typov modelov (z predmetu „modelovanie v procesnom priemysle"):
**modely z prvých princípov** vychádzajú z fyzikálnych zákonov. V tomto predmete
žijeme vo svete **modelov založených na dátach** — statických aj dynamických,
lineárnych aj nelineárnych — a trochu sa venujeme aj **odhadovaniu stavu** (technika,
ktorá spracúva dáta a odstraňuje časť šumu).

Dnešná otázka: **ako môžeme modelovať šum/neistotu v dátach** a pochopiť dáta ešte
pred tým, ako postavíme model? Jednou z ciest je porozumieť **pravdepodobnosti** a
robiť trochu **štatistiky**. (Prednášajúci poznamenáva, že tieto snímky boli
pôvodne pripravené pre Noc výskumníkov, aby ukázali deťom, ako pravdepodobnosť
funguje.)

Prednášajúci tiež spomína prednášku slovenského vedca
<!-- unclear: meno v titulkoch „mikal vco"; opisovaný ako spoluzakladateľ Google DeepMind -->
o **veľkých jazykových modeloch (LLM)**, pričom zdôrazňuje, že **LLM sú len
aplikovaná štatistika** — trénované pomocou stredných hodnôt, smerodajných odchýlok
a pravdepodobnosti. Poznámka na okraj: keby sme mohli takýto model trénovať
viackrát, mohli by sme dokonca dostať **interval spoľahlivosti** pre jeho odpovede;
dnes vám nikto nepovedal, že výstup ChatGPT má napr. 80 % vs. 20 % šancu byť správny.

## Pravdepodobnosť a experiment s kockou

**Pravdepodobnosť** (známa zo strednej školy) vyjadruje, že udalosť môže nastať
s určitou pravdepodobnosťou, v matematickom vyjadrení od **0 do 1**. Dobrým
testovacím zariadením je **kocka**.

Nadväzujúc na myšlienku histogramu z minulého týždňa, prednášajúci buduje histogram
výsledkov hodov kockou (1–6):

- Niekoľko **fyzických** hodov v triede nevyzerá rovnomerne (napr. niekoľko dvojiek,
  pár jednotiek). Dôvod je, že **počet experimentov nie je dostatočný** — to poukazuje
  na **zákon veľkých čísel**.
- V **MATLAB**-e, pri simulácii *spravodlivej* kocky:
  - **20** pokusov: stále veľmi nerovnomerne (šestka sa môže objaviť takmer v
    polovici prípadov).
  - **100** pokusov: iný obraz, žiadne číslo nedominuje.
  - **1 000 / 10 000 / 100 000 / 1 000 000 / 6 000 000** pokusov: stĺpce sa
    postupne vyrovnávajú. Pri **6 miliónoch** hodov sa každé číslo objaví asi
    **1 milión** krát — každý výsledok je rovnako pravdepodobný.

Potom histogram **normalizujeme** — nezaujíma nás absolútny počet, len
**podiely/pomery**. Pravdepodobnosť udalosti (napr. hodenie trojky) je **počet
úspešných výskytov vydelený počtom pokusov**. Prednášajúci poznamenáva, že keby
kocka bola **nefér**, niektoré čísla by sa vyskytovali častejšie, ale z malého
počtu experimentov to nemožno zistiť.

## Súčet viacerých kociek → zvonová krivka

Klasický odbočný príklad: hodiť **dvoma kockami naraz** a pozerať sa nie na
jednotlivé čísla, ale na ich **súčet**.

- Jedna kocka dáva 6 výsledkov; dve kocky dávajú **36 možných výsledkov** pre dvojicu.
- Súčty **nie sú** rovnomerne rozdelené: napr. súčet **3** nastane len dvakrát,
  ale súčet **7** dominuje, lebo ho možno dosiahnuť ako 6+1, 5+2, 4+3, … Takže
  model tejto hry už nie je rovnomerný — **7** je najpravdepodobnejší súčet.

Pokračujeme hrou s **troma kockami**: najmenší súčet je 1+1+1 = **3**, najväčší
6+6+6 = **18**; súčty 10 a 11 sa stávajú najpravdepodobnejšími. So **štyrmi, piatimi,
šiestimi, … až ~20 kockami** sa objaví zreteľný **tvar**. Pri ~20 kockách je
najpravdepodobnejší súčet okolo **70** (desaťnásobok vrcholu dvoch kociek, t. j. 7).

Tento tvar je **zvonová krivka** — **Gaussova krivka** so známou rovnicou. Nemci ju
dokonca dali na svoju menu: **Carl Friedrich Gauss** a zvonová krivka sa objavili na
bankovke **10 nemeckých mariek**.

## Hustota pravdepodobnosti (PDF)

Zvonová krivka je **hustota pravdepodobnosti**, skrátene **PDF** (nie „portable
document format"). PDF existuje pre akékoľvek rozdelenie — dokonca aj pre
**rovnomerné rozdelenie** (kocka), ktoré nie je funkciou „e na nejakú mocninu".

PDF hovorí, **aká je pravdepodobnosť výskytu udalosti**. Pre kocku (6 diskrétnych
výsledkov) je to ľahko interpretovateľné, ale pre spojitú veličinu ako
**teplota v miestnosti** sa myšlienka „pravdepodobnosť namerania presne
25,7284…°" stáva skreslená — bude na to riešenie (distribučná funkcia).

### Normálne/Gaussovo rozdelenie

„Normálne" a „Gaussovo" sú synonymá (Nemci zvyknú hovoriť *Gaussovo*; iní hovoria
*normálne*). Hovoríme, že náhodná premenná $X$ (veľké $X$; po slovensky *premenná*)
**sa riadi** normálnym rozdelením, zapísané — pozor, celý svet, dokonca aj Nemci,
píše veľké **N**, nie G:

$$
X \sim N(\mu, \sigma^2)
$$

s dvoma parametrami $\mu$ a $\sigma$ (na snímku: zapísané s $\bar{x}$;
$X \sim N(\bar{x}, \sigma^2)$ s parametrami $\bar{x}$ a $\sigma^2$).

Parametre a ich slovenské názvy (potvrdené zo snímku):

- $\mu$ (tiež písané $\bar{x}$) — **priemer** / **stredná hodnota** / **stredná
  očakávaná hodnota**. Prednášajúci preferuje anglický výraz „expected value", dokonca
  zapísaný ako operátor $\mu = E[X]$. Po slovensky: **stredná hodnota**. Ak sú dáta
  normálne rozdelené, stredná hodnota je číslo, ktoré očakávame od ďalšieho pokusu
  (ďalší hod kockou, teplota, výsledok skúšky). Pre hru s dvoma kockami je priemer
  **7**.
- $\sigma$ — **smerodajná odchýlka**.
- $\sigma^2$ — **rozptyl** (veľmi užitočný pojem).

PDF normálneho rozdelenia (funkcia z nemeckej bankovky; potvrdená zo snímku):

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}}\, e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

Táto PDF, $f(x)$, nám hovorí, **ako relatívne pravdepodobný** je výsledok $x$.

### Zostrojenie krivky z jednoduchších funkcií

Na pochopenie tejto zložite vyzerajúcej funkcie sa prednášajúci pozrie na
jednoduchší prípad $\mu = 0$ a $\sigma = 1$ — **štandardné normálne/Gaussovo
rozdelenie**. Potom:

$$
f(x) = \frac{1}{\sqrt{2\pi}}\, e^{-\frac{1}{2}x^2}
$$

Nakreslí ho v troch krokoch (snímok zobrazuje rovnakú trojpanelovú postupnosť):

1. Vykresliť $x^2$ — parabola s minimom (hodnota 0) v $x = 0$ (priemer).
2. Negovať: $-x^2$ — teraz **konkávna**, s **maximom** v $x = 0$.
3. Aplikovať **exponenciálu** $e^{(\cdot)}$. Keďže $-x^2$ nadobúda len **záporné
   hodnoty**, zostávame na časti exponenciály medzi **1** (v maxime, $e^0 = 1$)
   a **0** (hodnoty smerujú k nule, t. j. **infimum** na chvostoch, nikdy nedosiahnuté).
   Maximum zostáva v $x = 0$, lebo exponenciála je rastúca funkcia. Faktor
   $\tfrac{1}{2}$ len riadi rýchlosť poklesu. Výsledkom je **Gaussova krivka**.

## Prečo konštanta $\tfrac{1}{\sqrt{2\pi}}$ — integrál rovný 1

PDF **nie je priamo pravdepodobnosť**. Pre kocku sa môžeme pýtať napr. „aká je
pravdepodobnosť **párneho** čísla?" — sčítame jednotlivé pravdepodobnosti:
$\tfrac{1}{6} + \tfrac{1}{6} + \tfrac{1}{6} = \tfrac{1}{2}$ (operácia **ALEBO** pre
udalosti → súčet pravdepodobností; toto je rozlíšenie **spojenej** a jednoduchej
sumy, na ktoré prednášajúci upozorňuje). Sčítaním cez **všetky** výsledky kocky
dostaneme $6 \times \tfrac{1}{6} = 1$.

Pre spojitú PDF je analógiou „prejsť cez všetky možnosti a sčítať" **integrácia**.
Platná PDF teda musí integrovať na jedna. Testovanie samotnej štandardnej normálnej
exponenciály v MATLAB-e:

$$
\int_{-\infty}^{\infty} e^{-\frac{1}{2}x^2}\, dx = \sqrt{2\pi} \approx 2{,}5066
$$

Práve preto je tam normalizačná konštanta $\tfrac{1}{\sqrt{2\pi}}$ (všeobecnejšie
$\tfrac{1}{\sigma\sqrt{2\pi}}$) — aby **celková pravdepodobnosť bola 1**. Snímok
uvádza všeobecné vlastnosti:

$$
f(x) \ge 0, \qquad F(\infty) = \int_{-\infty}^{\infty} f(x)\, dx = 1
$$

Interpretácia: *nejaká* udalosť musí nastať — teplota v miestnosti je buď
$-\infty$, nejaké konečné číslo, alebo $+\infty$ — takže celková pravdepodobnosť
je 1.

## Distribučná funkcia (CDF)

Aby sme dostali **pravdepodobnosť** (nie len hustotu), používame **distribučnú
funkciu**, **CDF**. Po slovensky: **distribučná funkcia**.

Kontrast v zápise: PDF zapísaná ako $f(x)$ (malé $f$) dáva hustotu/relatívnu
pravdepodobnosť; CDF zapísaná ako $F$ (veľké) dáva **pravdepodobnosť samotnú**.
CDF je definovaná ako pravdepodobnosť, že $X$ je menšie alebo rovné nejakej hodnote
$z$ (konkrétna hodnota $x$):

$$
F(z) = \Pr(X \le z) = \int_{-\infty}^{z} f(x)\, dx
$$

Integrál musíme začínať na jednom konci, teda začíname od $-\infty$. Tým vypočítame
**plochu pod krivkou PDF** až po $z$ — rovnaký princíp ako súčet
$\tfrac{1}{6}+\tfrac{1}{6}+\tfrac{1}{6}$ na kocke pre $P(X \le 3) = \tfrac{1}{2}$,
ale teraz v **spojitom** svete (teplomer, nabíjanie batérie atď.).

Skicovanie CDF bod po bode (snímok zobrazuje integrálnu formu):

- Na jednom konci je **0** a na druhom **asymptoticky 1** (po zintegrovaní celej
  krivky, $P(X \le 10\,000°) \approx 1$). Nikdy nejde do záporných hodnôt, lebo
  PDF je vždy kladná (plochy sa nerušia).
- Je to **integrál** PDF, teda PDF je jej **derivácia**: malé sklony na chvostoch,
  **maximálny sklon (inflexný bod)** v strednej hodnote.
- Pre zvolené $z_1$ (napr. 10°) prečítame $F(z_1)$, povedzme **0,2 (20%)** —
  pravdepodobnosť, že teplota je $z_1$ alebo menej. Pre $z_2 = \mu$ (stredná hodnota)
  dostaneme asi **0,5**; vyššie $z_3$ dáva viac.

### Od distribučnej funkcie k pravdepodobnostiam intervalov

Zvyčajne chceme pravdepodobnosť, že $X$ padne do **intervalu**, čo je rozdiel dvoch
hodnôt CDF, resp. určitý integrál (snímok):

$$
P(a \le x \le b) = \int_{a}^{b} f(x)\, dx
$$

V praxi na to **zbierame dáta**, odhadneme dva parametre (priemer a
rozptyl/smerodajnú odchýlku) krivky a potom kladieme takéto otázky. Diskutovaný
príklad: meranie **výšky** každého v miestnosti. Rovnako ako pri kocke nezísame
rovnomerné rozdelenie — **fitujeme normálne rozdelenie** na dáta, dostaneme priemer
a smerodajnú odchýlku a potom sa pýtame napríklad „kto má výšku medzi 174 a
178 cm?". Pravdepodobnosť **presne** jedného bodu (napr. presne 25°) je **nula**,
lebo integrál cez jeden bod je nula — preto sa vždy pýtame na malý interval
(napr. $25 \pm 0{,}1$).

Poznámka k jednotkám: v $\frac{(x-\mu)^2}{2\sigma^2}$ musia $x$ a $\sigma$ „žiť
v rovnakom svete" — ak je $x$ teplota v Kelvinoch, čitateľ je v Kelvinoch² a
menovateľ (cez $\sigma$) tiež v Kelvinoch², takže exponent je **bezrozmerný**.
To nám umožňuje **štandardizovať**: odčítame strednú hodnotu a meriame vzdialenosť
v násobkoch $\sigma$.

## Pravidlo 68–95–99,7 (sigmaové intervaly)

Meranie vzdialenosti od strednej hodnoty v **smerodajných odchýlkach** dáva
slávne pravdepodobnosti intervalov (vypočítané v MATLAB-e integrovaním štandardnej
normálnej PDF medzi hranicami; potvrdené na snímku):

$$
P(\mu - \sigma \le x \le \mu + \sigma) = 68{,}27\%
$$

$$
P(\mu - 2\sigma \le x \le \mu + 2\sigma) = 95{,}45\%
$$

$$
P(\mu - 3\sigma \le x \le \mu + 3\sigma) = 99{,}73\%
$$

Teda $\pm 1\sigma \approx 68\%$, $\pm 2\sigma \approx 95\%$, $\pm 3\sigma \approx
99{,}7\%$. Prednášajúci poznamenáva, že toto je **všeobecné** — akonáhle poznáme
strednú hodnotu a (čo je najdôležitejšie) smerodajnú odchýlku, platí pre
akékoľvek normálne rozdelenie. Pre návrh regulácie nemusíme dbať na 5 % prípadov
mimo $\pm 2\sigma$. Tiež spomína, že v **CERN**-e sa „objav" (napr. Higgsov bozón,
alebo tvrdenie o neutrínoch rýchlejších ako svetlo) vyhlasuje pri asi
**6 smerodajných odchýlkach**.

## Odhadovanie parametrov z dát

Nakoniec, ako vypočítať parametre z $n$ vzoriek $x_1, x_2, \dots, x_n$.
Strieška označuje **výberový** odhad (na základe pozorovaní, nie presnej hodnoty):

**Výberový priemer** — aritmetický priemer (sčítame hodnoty, vydelíme počtom
pokusov), rovnaká myšlienka ako pravdepodobnosť $\tfrac{1}{6}$ pri kocke:

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
$$

**Rozptyl/smerodajná odchýlka** — slovne opísaný ako **priemer toho, o koľko sa
vzorky líšia od priemeru**, a keďže tento rozdiel môže byť kladný alebo záporný,
používa sa **druhá mocnina** (prednášajúci nepíše explicitný menovateľ; snímok
ho ponecháva ako „$\sigma^2 = \dots$"):

<!-- unclear: prednášajúci uvádza „priemer druhých mocnín odchýlok od priemeru", ale nešpecifikuje menovateľ (n vs n-1) -->

$$
\sigma^2 \approx \frac{1}{n}\sum_{i=1}^{n} (x_i - \bar{x})^2
$$

Smerodajná odchýlka je potom priemerná vzdialenosť dát (výšky, teploty, …) od ich
strednej hodnoty.

Záver analógie s LLM: odpoveď ChatGPT je ako **jedna vzorka** odobratá z nejakého
základného súboru (odpovede nájdené online, niektoré overené expertmi) — ale
rozptyl ľahko nezískate, lebo každá „vzorka" je jedno trénovanie ~40 miliárd
parametrov za milióny dolárov, takže nikto nefinancuje viaceré trénovania, ktoré
by boli potrebné.
