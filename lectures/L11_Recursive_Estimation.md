---
lecture: L11
title: "Rekurzívny odhad"
course: Identifikácia
source: "https://www.youtube.com/watch?v=cTlkFkwKV4U"
---

# L11 — Rekurzívny odhad

> Vzorce overené podľa prednášateľových snímok (*L Identifikácia, L11 —
> 30. 04. 2024*). Poznámka: na kamere prednášateľ na chvíľu napísal odhad sklonu
> ako $\sum y_k / \sum x_k$; snímka (a rekurzia, ktorú potom odvodzuje) používa
> správnu formu najmenších štvorcov $a_N = \frac{\sum y_k x_k}{\sum x_k^2}$,
> použitú nižšie.

## Problém

Máme zariadenie/proces/systém, pre ktorý sme z experimentu zostavili model, ktorý
predikuje historické dáta. Nasadený v priemysle, model by mal predikoval budúce výstupy
pre ľubovoľné vstupy, takže **chyba predikcie** by mala byť približne nulová:

$$
e \approx 0
$$

(rozdiel medzi nameraným výstupom systému $y_k^{\text{meas}}$ a predikciou modelu
$\hat{y}_k$). **Rekurzívny odhad** rieši prípad, keď sa to **nestane** a model sa musí
**adaptovať online**.

## Aktualizácia posunu

Predpokladajme, že historické (nominálne) dáta boli dobre nafitované, ale v oblasti
nezávislých premenných, ktorá nebola preskúmaná pri trénovaní, skutočné zariadenie sa
vyvíja s takmer **konštantnou systematickou chybou** (napr. nelinearita alebo zmenený
dodávateľ reaktantov). **Sklon** vyzerá stále správne (závislá premenná reaguje
rovnakým spôsobom), a nemôžeme meniť nezávislé premenné — preto upravujeme len
**posuv/offset** $b$, aby absorboval konštantný posun. Toto je najjednoduchší
rekurzívny odhad, **aktualizácia posunu**, hojne využívaná v priemysle (spoločnosti
preferujú nemeniť overené sklony/závislosti).

Posuv sa stáva funkciou času. Porovnaním predchádzajúcej predikcie
$\hat{y}_{k-1} = a x_{k-1} + b_{k-1}$ s aktuálnym meraním $y_{k-1}$, aktualizujeme
posuv o chybu predikcie:

$$
b_k = b_{k-1} + \big(y_{k-1} - \hat{y}_{k-1}\big)
$$

Toto posúva priamku na nový prevádzkový bod.

### Filtrovaná aktualizácia posunu

Reagovanie na jedno meranie je **krátkozraké** (jeden zašumený bod hojdá posunom).
Pridáme **filtráciu** s parametrom $\delta \in [0, 1]$ pôsobiacim ako **faktor
dôvery**:

$$
b_k = \delta\, b_{k-1} + (1 - \delta)\,(\text{člen chyby predikcie})
$$

<!-- the exact combination was stated loosely; delta weights the old bias against the new error-based correction -->

- $\delta$ blízko **1**: **nedôverujeme** nedávnym meraniam príliš; posuv sa mení málo,
  ale trvalý trend sa postupne akumuluje a pomaly posúva priamku na nový prevádzkový
  bod.
- $\delta = 0$: odhad je riadený **výlučne** novým meraním.

Toto $\delta$ je ako zosilnenie **P regulátora**, kde riadiaca akcia sa mení o
zosilnenie × riadiaca chyba (snímka):

$$
u_k = K\, e_k = K\,(w_k - y_k)
$$

Tu sa namiesto toho **odhad** mení o zosilnenie × **chyba predikcie**.

## Aktualizácia sklonu: rekurzívna metóda najmenších štvorcov (skalárna)

Teraz prípad, kde sa musia meniť samotné **závislosti**. Vezmime najjednoduchšie
nastavenie lineárnej regresie ($b = 0$, skalárne $a$), $y_k = a x_k$. Odhad
najmenších štvorcov z $N$ meraní a z $N-1$ meraní (snímka):

$$
a_N = \frac{\sum_{k=1}^{N} y_k x_k}{\sum_{k=1}^{N} x_k^2},
  \qquad
  a_{N-1} = \frac{\sum_{k=1}^{N-1} y_k x_k}{\sum_{k=1}^{N-1} x_k^2}
$$

Brať všetkých $N$ (napr. tisíc alebo milión) historických hodnôt zakaždým je
nepraktické (veľké inverzie matíc vo viacrozmernom prípade) a existuje
**vzor**: nová hodnota by mala byť stará hodnota plus (filtrovaná) korekcia.

### Odvodenie rekurzie

Oddelíme posledný člen v čitateli a menovateli,
$\sum_{k=1}^{N} = \sum_{k=1}^{N-1} + (\text{člen } N)$, a dosadíme
$\sum_{k=1}^{N-1} y_k x_k = a_{N-1}\sum_{k=1}^{N-1} x_k^2$:

$$
a_N = \frac{a_{N-1}\sum_{k=1}^{N-1} x_k^2 + y_N x_N}{\sum_{k=1}^{N} x_k^2}
$$

Aby sme dostali $a_{N-1}$ krát **úplný** súčet, **pridáme a odčítame** $a_{N-1} x_N^2$
(„predstieraj, kým to nedokážeš"):

$$
a_N = \frac{a_{N-1}\sum_{k=1}^{N} x_k^2 + y_N x_N - a_{N-1} x_N^2}
             {\sum_{k=1}^{N} x_k^2}
$$

Oddelením $a_{N-1}$ dostaneme **rekurzívnu aktualizáciu**:

$$
a_N = a_{N-1} + \frac{x_N}{\sum_{k=1}^{N} x_k^2}\,\big(y_N - a_{N-1} x_N\big)
$$

Štruktúra odráža aktualizáciu posunu a regulátor:

- $y_N$ je práve vykonané **meranie**.
- $a_{N-1} x_N$ je **predikcia starého (neaktualizovaného) modelu** — predikcia
  v čase $N$ na základe informácií dostupných do času $N-1$, zapísaná
  $\hat{y}_{N\mid N-1}$. Takže $(y_N - a_{N-1}x_N)$ je **chyba predikcie**.
- $\dfrac{x_N}{\sum_{k=1}^{N} x_k^2}$ je **zosilnenie** — nakoľko dôverujeme novému
  meraniu.

### Zosilnenie sa automaticky zmenšuje (a zabúdanie)

Na rozdiel od aktualizácie posunu, zosilnenie **nie je** naša voľná voľba. Začínajúc
s jedným meraním ($x = 1$) je zosilnenie 1; po 100 meraniach (všetky $x = 1$) je
$\tfrac{1}{100}$ — oveľa menšie. Toto je žiaduce: $a_{N-1}$ už nesie informáciu
$N-1$ bodov, ktorú nechceme prepísať jedným možno zašumeným meraním.

Ak však 10 rokov dát diktuje koreláciu a len ~5 nedávnych meraní je s ňou v rozpore,
môžeme **obmedziť** minulé dáta — použiť iba posledný mesiac alebo polrok. Toto je
**skrátené časové okno pre novšie aktualizácie** (zabúdanie), naladené podľa toho,
ako veľmi sa proces môže meniť.

## Rekurzívna metóda najmenších štvorcov: všeobecný (vektorový) prípad

Vo všeobecnosti je predikčný model $y = X p$, kde regresný (riadkový) vektor
$\phi_N$ pre vzorku $N$ dáva $y_N = \phi_N^T p$. Rovnaká úvaha dáva vektorovú
rekurziu (snímka):

$$
p_N = p_{N-1} + P_N^{-1}\,\phi_N\,\big(y_N - \phi_N^T p_{N-1}\big)
$$

pričom **kovariančná** matica sa akumuluje ako

$$
P_N = P_{N-1} + \phi_N\,\phi_N^T \quad\longrightarrow\ \text{kovariancia}
$$

(ekvivalentne zosilnenie je $(X^T X)^{-1} x_N$ v predchádzajúcej notácii).
Ingrediencie sú opäť rovnaké:

- **chyba predikcie** $\big(y_N - \phi_N^T p_{N-1}\big)$;
- **apriorné znalosti** $p_{N-1}$ (predchádzajúci odhad parametrov);
- **zosilnenie** $P_N^{-1}\phi_N$ — zostavené z kovariančnej matice (akumulovaného
  $X^T X$ historických hodnôt $x$) a jej inverzie, takže s rastúcim počtom minulých
  hodnôt zosilnenie **klesá**.

(V priebehu času sa odhad $p$ konverguje k skutočnému $p^{*}$, so zmenšujúcim sa
intervalom spoľahlivosti okolo neho.)

## Spojenie s Kalmanovým filtrom

S viac času je toto jeden krok od **odhadovača stavu**. Pre model stavového priestoru

$$
x_k = A x_{k-1} + B u_{k-1}
$$

korigovaný odhad tvaru

$$
\hat{x}_k = A \hat{x}_{k-1} + B u_{k-1} + K\big(y_k - C \hat{x}_k\big)
$$

s múdro zvoleným zosilnením $K$ (**Kalmanov zisk**) sa stáva **Kalmanovým filtrom** —
ktorý odhaduje **stavy** dynamického systému namiesto parametrov. Myšlienka je
identická: z predchádzajúcej predikcie (v čase $k-1$) predpovedáme $x_k$;
zmeráme niečo o stave; a korigujeme pomocou **matice zosilnenia** krát nesúlad merania.

*(Tým sa kurz končí.)*
