# Identifikácia — Praktická príprava na skúšku (MATLAB)

> Cieľ: vedieť si sadnúť k MATLABu a zo surových nameraných dát reprodukovať
> celý pracovný postup identifikácie vyučovaný na seminároch 1–11 a zadaniach 1–2.
> Každý blok kódu nižšie je **opakovateľne použiteľná šablóna** — memorujte si *vzor*,
> nie presné čísla.

---

## 0. Štandardný pracovný postup (zapamätajte si túto kostru)

Takmer každá úloha v tomto kurze sa riadi rovnakým postupom:

1. **Načítanie** dát (`readtable`, `load` alebo `sim`)
2. **Vizualizácia** surových signálov (časové rady + rozptylový/závislostný graf)
3. **Čistenie** dát (odstránenie odľahlých hodnôt / zlých prevádzkových oblastí)
4. **Štandardizácia** (nulový priemer, jednotkový rozptyl)
5. **Rozdelenie** na trénovacie (TV) a testovacie (TS) datasety
6. **Fitovanie modelu** metódou najmenších štvorcov (`X\y`)
7. **Predikcia** a vyhodnotenie pomocou **RMSE**
8. **Porovnanie** modelov / vizualizácia zhody (paritný graf, prekrytie)

Udržiavajte túto kostru v hlave — úloha na skúške je zvyčajne jej variáciou.

### Úvodná hlavička používaná všade
```matlab
clc; clear all; close all; rng(100);   % rng pre reprodukovateľné náhodné čísla
```

### Šablóna pre vykresľovanie (používaná v každom grafe)
```matlab
figure; hold on; grid on; box on; text = [];
plot(x, y, '.r', 'MarkerSize', 10);          text = [text; {'Merania'}];
legend(text, 'Interpreter', 'latex', 'Location', 'best');
xlabel('$x$', 'Interpreter', 'latex');
ylabel('$y$', 'Interpreter', 'latex');
set(gca, 'FontSize', 15, 'ticklabelinterpreter', 'latex');
set(gcf, 'Position', [100, 100, 1400, 600]);
```
*Trik `text = [text; {...}]` postupne buduje pole buniek legendy,
jedna položka na každé volanie `plot`.*

---

## 1. Načítanie a vizualizácia dát (Seminár 1, 3, 4)

```matlab
% Z CSV / tabuľky
data  = readtable('tank_data.csv');
time  = table2array(data(:,1));        % alebo  data.Year
h     = table2array(data(:,9));

% Z .mat
d = load('data_FCC_dep_XY_anonymous.mat');   % dáva štruktúru d.X, d.Y, ...

% Uloženie / načítanie pre preskočenie pomalého výpočtu (vzor s prepínačom "con")
con = 1;
if con == 1
    data = sim('s_gas_tank', time);     % spustenie Simulink, pomalé
    save('data_training', 'data');
else
    load('data_training');              % opätovné použitie, rýchle
end
```

**Vykresľovanie v logaritmickej škále** (pre exponenciálny rast, napr. Moorov zákon):
```matlab
set(gca, 'YScale', 'log');              % alebo 'xscale','log'
plot(t, log(y), '-*');                  % alternatíva: transformácia dát
```

---

## 2. Popisná štatistika (Seminár 1, 2)

```matlab
n   = length(x);
mu  = mean(x);              %  = 1/n * sum(x)
s   = std(x);               %  = sqrt( 1/(n-1) * sum((x-mu).^2) )  (výberová smerodajná odchýlka, N-1)
v   = var(x);               %  = s^2
med = median(x);
g   = geomean(x);
```
Vedzte, že `std`/`var` používajú štandardne menovateľ **N−1** (nestranný odhad).

### Počítanie dát v rozsahu ±3σ (Seminár 2)
```matlab
idx_in  = find(abs(x) <= 3);            % v rámci 3 sigma
idx_out = find(abs(x) > 3);
pct_in  = length(idx_in)/length(x)*100; % ~99.7% pre normálne rozdelené dáta
```

---

## 3. Rozdelenia pravdepodobnosti: hustota pravdepodobnosti / distribučná funkcia (Seminár 2)

```matlab
xe = linspace(-5, 5, 1000);

% Vytvorenie rozdelenia a výpočet hustoty pravdepodobnosti/distribučnej funkcie
pd    = makedist('normal', 'mu', 0, 'sigma', 1);
p_pdf = pdf(pd, xe);
p_cdf = cdf('norm', xe, 0, 1);

% Inverzná distribučná funkcia (kvantil): "aké x zodpovedá tejto pravdepodobnosti?"
x_q   = icdf('normal', 0.841, 0, 1);    % ~ +1 sigma

% Prekrytie teoretickej hustoty pravdepodobnosti na normalizovaný histogram
figure; hold on; grid on;
histogram(x, 'Normalization', 'pdf');
plot(xe, p_pdf, '.k');
```
- Väčší rozsah vzorky → histogram sa blíži k teoretickej hustote pravdepodobnosti (zákon veľkých čísel).

---

## 4. Fitovanie modelu metódou najmenších štvorcov

**Všetko** v tomto kurze sa rieši spätným lomítkom MATLABu:
```matlab
p = X \ y;          % rieši  min || X*p - y ||^2   (normálne rovnice)
yhat = X * p;       % predikcia modelu
```
`X` je **regresná matica** — každý stĺpec je jedna bázová funkcia /
príznak, každý riadok jedno meranie.

### Príklady statických modelov (Semináre 3, 5)
```matlab
% Nádrž:  q1 = k * sqrt(h)   (bez absolútneho člena)
k    = sqrt(h) \ q1;
q1c  = k * sqrt(h);

% Lineárny s absolútnym členom:  V = p1*T + p0
p1   = [T, ones(size(T))] \ V;
Vhat = [T, ones(size(T))] * p1;

% Vyskúšajte viacero štruktúr a porovnajte:
pLin = [T,     ones(size(T))] \ V;     % lineárny
pQua = [T.^2,  ones(size(T))] \ V;     % kvadratický
pInv = [1./T,  ones(size(T))] \ V;     % inverzný
```
**Tip:** pridanie `[príznak, ones(size(...))]` do `X` pridá absolútny člen (posun).
Vypustite stĺpec `ones` pre fitovanie prechádzajúce počiatkom.

---

## 5. Presnosť: RMSE a paritný graf

```matlab
RMSE = sqrt(mean((yhat - y).^2));       % ručný výpočet
RMSE = rmse(yhat, y);                   % vstavaná funkcia (novší MATLAB)
```

### Paritný graf / predikované vs. namerané hodnoty (typický grafický výstup na skúške)
```matlab
figure; hold on; grid on; box on;
plot(y, yhat, '.m', 'MarkerSize', 10);                 % body
lims = [min([y;yhat]), max([y;yhat])];
plot(lims, lims, '--k');                               % ideálna čiara 45°
xlabel('Namerané $y$', 'Interpreter', 'latex');
ylabel('Predikované $\hat{y}$', 'Interpreter', 'latex');
```
Body na uhlopriečke = dokonalá predikcia. Rozptyl od nej = chyba.

---

## 6. Štandardizácia (Semináre 5, 7, 9)

```matlab
xs = (x - mean(x)) / std(x);            % nulový priemer, jednotkový rozptyl
```
Overenie numericky — `mean(xs) ≈ 0`, `std(xs) ≈ 1`:
```matlab
disp(['mu = ', mat2str(round(mean(xs),4)), ', sigma = ', mat2str(round(std(xs),4))]);
```
**Pozor:** *konštantný* signál má `std = 0` → delenie nulou.
Ošetrite to (Zadanie 2, šumový kanál `n`):
```matlab
if std(n) == 0, ns = zeros(size(n)); else, ns = (n-mean(n))/std(n); end
```

---

## 7. Korelácia, kovariancia, analýza hlavných komponentov (Semináre 6, 7)

```matlab
% Pearsonov korelačný koeficient medzi dvoma premennými
c = corrcoef(x1, x2);  c = c(1,2);      % mimediagonálny prvok, v [-1, 1]

% Matice kovariancie a korelácie
K  = cov(X);                            % kovariancia
R  = corrcoef(X);                       % korelácia (štandardizovaná kovariancia)

% Vizuálna korelačná matica pre mnoho premenných
corrplot(X, 'varNames', tags);

% Vlastná dekompozícia kovariancie (hlavné smery)
[eigvec, eigval] = eig(K);

% Vykreslenie kovariancie "elipsy" (1σ/2σ/3σ) — Seminár 7
nc = 1000;  Xc = [cos(linspace(0,2*pi,nc))', sin(linspace(0,2*pi,nc))'];
ellipse = mean(X) + Xc * sqrtm(K);      % sqrtm = odmocnina matice
```

### Analýza hlavných komponentov (Seminár 7, Úloha 6–7)
```matlab
[COEFF, SCORE, LATENT, TSQ, EXPLAINED, MU] = pca(X);
% COEFF    = hlavné smery (zaťaženia)
% SCORE    = dáta v súradniciach hlavných komponentov
% EXPLAINED= % rozptylu vysvetlený každým komponentom
% Rekonštrukcia:  X_centered ≈ SCORE * COEFF'
```
**Pravidlo kolena/lakťa** pre výber počtu hlavných komponentov: nakreslite čiaru od prvého k poslednému
bodu krivky `EXPLAINED`; bod s maximálnou vzdialenosťou od tejto čiary je
lakeť:
```matlab
it = (1:numel(EXPLAINED))';
p  = [it(1) 1; it(end) 1] \ [EXPLAINED(1); EXPLAINED(end)];
d  = abs([it ones(size(it))]*p - EXPLAINED);
idx = find(d == max(d));                 % index lakťa
```

---

## 8. Multivariátna regresia + trénovacie/testovacie dáta (Semináre 6, 7)

```matlab
% Výber príznakov: odstránenie lineárne závislých / kolineárnych stĺpcov
idx_remove        = sort([8;15;13;18]);
Xsel              = X;  Xsel(:,idx_remove) = [];

% Rozdelenie trénovacie / testovacie
nTR   = 100;
Xtr   = X(1:nTR,:);   Xts = X(nTR+1:end,:);
ytr   = y(1:nTR);     yts = y(nTR+1:end);

p          = Xtr \ ytr;                  % trénovanie len na TR
RMSE_tr    = sqrt(mean((Xtr*p - ytr).^2));
RMSE_ts    = sqrt(mean((Xts*p - yts).^2));  % skutočná testovacia chyba
```
**Signál preučenia:** `RMSE_tr` malé, ale `RMSE_ts` veľké → príliš veľa príznakov.

### 95% interval spoľahlivosti pre regresiu (Seminár 5)
```matlab
[b, bint] = regress(y, X);               % bint = 95% IS pre každý koeficient
```

---

## 9. Filtrácia / vyhladzovanie signálov (Semináre 8, Zadanie 2)

```matlab
yl = lowpass(y, 0.001);                  % zachová pomalý trend (malé Wn)
yh = highpass(y, 0.1);                   % zachová rýchly šum

% FIR vyhladzovacie priemerovanie s oknom n:
n  = 50;  b = ones(n,1)/n;
ys = filter(b, 1, y);                    % kauzálny (vnáša oneskorenie)

% Vyhladzovanie s nulovou fázou (bez časového oneskorenia) — používané pre testovací výstup v Zadaní 2
win  = 201;  b_ma = ones(1,win)/win;
ytest = filtfilt(b_ma, 1, y);            % dopredu-dozadu => bez oneskorenia
```
- **Dolnopriepustný filter** odstraňuje šum, ale spôsobuje oneskorenie / vyhladzuje hrany.
- **filtfilt** = nulová fáza: rovnaké vyhladzovanie, **bez oneskorenia** (používané pre vyhladzenú
  testovaciu referenciu).

---

## 10. Identifikácia dynamických systémov — FIR & ARX (Semináre 9–11, Zadanie 2)

Oba modely sú stále len metóda najmenších štvorcov; mení sa len regresná matica.

### FIR model  `y_k = Σ b_i · u_{k-i}`  (výstup = vážené minulé vstupy)
```matlab
m = 50;  N = length(u);                 % m = rád modelu (# minulých vstupov)
Phi = zeros(N-m, m);  Y = zeros(N-m,1);
for k = (m+1):N
    Phi(k-m,:) = u(k-1:-1:k-m)';        % [u(k-1), u(k-2), ..., u(k-m)]
    Y(k-m)     = y(k);
end
b    = Phi \ Y;                         % FIR koeficienty (impulzná odozva)
yhat = Phi * b;
RMSE = sqrt(mean((yhat - Y).^2));
```

### ARX model  `y_k = -Σ a_i·y_{k-i} + Σ b_i·u_{k-i}`  (používa aj minulé *výstupy*)
```matlab
n = 3; m = 3; p = max(n,m);  N = length(y);
Phi = zeros(N-p, n+m);  Y = zeros(N-p,1);
for k = (p+1):N
    ylag = -y(k-1:-1:k-n)';             % POZOR: záporné znamienko pri oneskoreniach výstupu
    ulag =  u(k-1:-1:k-m)';
    Phi(k-p,:) = [ylag, ulag];
    Y(k-p)     = y(k);
end
theta = Phi \ Y;                        % [a1..an, b1..bm]
a = theta(1:n);  b = theta(n+1:end);
yhat = Phi * theta;
```

### ARMAX model  `y_k = -Σ a_i y_{k-i} + Σ b_i u_{k-i} + Σ c_i e_{k-i}`
ARX plus člen kĺzavého priemeru na **minulých chybách** — modeluje poruchy a
online sa samokoriguje. Časť `c` ho robí **nelineárnym** v parametroch, takže
prosté `\` tu nefunguje; použite System Identification Toolbox:
```matlab
dataID = iddata(y, u, Ts);               % zabalenie výstupu/vstupu
na = 2; nb = 2; nc = 2; nk = 1;          % rády AR / X / MA + oneskorenie vstupu
sysARMAX = armax(dataID, [na nb nc nk]); % iteračný (nelineárny) odhad
ypred = predict(sysARMAX, dataID, 1);    % predikcia o jeden krok dopredu
```
Použite ARMAX vtedy, keď sú rezíduá ARX viditeľne **korelované** (znak, že nemodelovaná
porucha uniká do `a, b`).

### Zostrojenie prenosových funkcií z koeficientov (Semináre 9–10)
```matlab
% FIR:  a = 1,  b = [0, b1..bm]
G_fir = tf([0 b'], 1, Ts, 'Variable', 'z^-1');

% ARX:  a = [1, a1..an],  b = [0, b1..bm]
G_arx = tf([0 b'], [1 a'], Ts, 'Variable', 'z^-1');

% Simulácia odozvy modelu na vstupný signál:
y_sim = lsim(G_arx, u);                 % alebo  idpoly(a,b,'Ts',Ts) + sim()
```

### Výber rádu modelu pomocou ACF / PACF (Seminár 11, Zadanie 2, Úloha 6)
```matlab
autocorr(y, 'NumLags', 50);             % ACF  -> celková pamäť / rád b (MA)
parcorr(y, 'NumLags', 50);              % PACF -> rád AR n: posledné oneskorenie mimo
                                        %         intervalu spoľahlivosti
```
Tu vyučované pravidlo palca: vyberte `n` tam, kde **PACF** klesne do intervalu
spoľahlivosti; udržiavajte `m ≤ n`, aby ste sa vyhli preučeniu.
- **Pomaly klesajúca ACF** (zostáva mimo pásma po stovky/tisíce
  oneskorení) = **dominantná časová konštanta** / silná dlhodobá pamäť → budete potrebovať
  dostatočne veľký rád AR `n`.

### Pamäťové okno FIR: prečo rád musí byť veľký (poznatky zo Zadania 2)
FIR model rádu `m` si „pamätá" len posledných `m` vzoriek vstupu, t. j.
**pamäťové okno `τ = m·Ts` sekúnd**. Pre dobré fitovanie musí `τ` pokrývať
**čas ustálenia** systému (ako dlho trvá, kým skoková odozva dosiahne ustálený stav).
```matlab
tau = m * Ts;            % napr. m=50, Ts=0.02 s  ->  tau = 1 s pamäte
```
Ak sa systém ustáli napríklad za niekoľko sekúnd, `m=50` (1 s) je **podučenie**. Ale
zvyšovanie `m` až na 1000 ukazuje, že RMSE sa takmer nezlepšuje — dôkaz, že pridávanie FIR
koeficientov je neefektívnou náhradou spätnej väzby, ktorú poskytuje ARX.
```matlab
for mi = [10 25 50:50:1000]              % prehľad RMSE podľa rádu
    [~,Gi] = deal(fir_train(u,y,mi));    % opakovanie fitu, predikcie, uloženie RMSE(mi)
end                                       % krivka sa splošťuje -> klesajúce výnosy
```

### Predikcia o jeden krok dopredu vs. voľná simulácia (záleží na spôsobe vyhodnotenia)
Dve rôzne „predikcie" ARX dávajú veľmi odlišné RMSE:
```matlab
% (a) O jeden krok dopredu (OSA): regresor používa SKUTOČNÉ namerané minulé výstupy
y_osa = Phi * theta;                     % Phi zostrojená zo skutočných y(k-1..k-n)
% (b) Voľná simulácia: model si späťvádza VLASTNÉ minulé výstupy
y_sim = lsim(G_arx, u);                  % zadáva sa len u
```
- **OSA** je ľahšia úloha → nižšie RMSE (takmer nulové RMSE ARX testovania v
  Zadaní 2 je OSA na *vyhladených* testovacích dátach). **Voľná simulácia** je
  poctivý, náročnejší test. Pri porovnaní modelov ich vyhodnocujte **rovnakým spôsobom** —
  porovnávanie ARX-cez-OSA s FIR-cez-`lsim` nie je plnohodnotné porovnanie jabĺk s jablkami.

---

## 11. Návrh VSTUPNÉHO signálu (Semináre 8–11)

Dobrá identifikácia potrebuje **perzistentne budiaci** vstup (bohatý na frekvencie):

```matlab
% Schodovité zmeny (schodisko)
u(1:200) = 1200; u(201:400) = 1000; ...   % po častiach konštantný

% Náhodné uniformné úrovne
u(idx) = 0 + (10-0).*rand;

% PRBS — pseudonáhodná binárna sekvencia (najlepšia pre dynamiku)
sig = prbs(5, 100);                       % rád 5, 100 vzoriek
u   = sig * 10;
```
- Čistý skok budí málo frekvencií; **PRBS** budí široké pásmo → lepšie
  dynamické modely. (Nápoveda v Zadaní 2, Úloha 1: „systémy reagujú rôzne na
  pomalé a rýchle zmeny — vyberte vstup, ktorý zachytí všetky dynamiky.")

---

## 12. Mapa úloh Zadania 2 (pravdepodobná šablóna pre praktickú skúšku)

| Úloha | Čo robiť | Kľúčový MATLAB |
|-------|----------|----------------|
| 1 | Načítať dáta Flexy², vykresliť u, n, y | `interp1(..,'previous')`, `plot` |
| 2 | Odstrániť zlé sekcie (napr. y>40%, nulový ventilátor) | `find`, orezanie indexov |
| 3 | Štandardizovať; zvoliť `u`, nie konštantné `n` | `(x-mean)/std` |
| 4 | Trénovacie = zašumené, Testovacie = y vyhladené nulovou fázou | `filtfilt(ones(1,201)/201,1,y)` |
| 5 | FIR rád 50, RMSE na TR/TS | cyklus buduje `Phi`, `Phi\Y` |
| 6 | ARX, rád z ACF/PACF, RMSE | `autocorr`,`parcorr`, `Phi\Y` |
| 7 | Porovnanie FIR vs ARX (prekrytie + stĺpcový graf RMSE) | `bar([...])` |

> **Prečo FIR potrebuje vysoký rád (~50):** nemá spätnú väzbu (žiadne členy `a`), takže
> musí aproximovať celý chvost impulznej odozvy mnohými koeficientmi `b`.
> **ARX** zachytí rovnakú dynamiku s oveľa menej parametrami, pretože
> rekurzívne členy `a·y_{k-i}` modelujú pokles implicitne → zvyčajne nižšie RMSE.

---

## 13. Bežné úskalia / rýchly kontrolný zoznam

- [ ] Použité `rng(100)` pre reprodukovateľné náhodné výsledky?
- [ ] `std`/`var` sú **N−1** bazírované — nedeliť znova.
- [ ] Štandardizácia **konštantného** kanála → ochrana pred `÷0`.
- [ ] Regresor `Phi` musí používať len **minulé** vzorky (`u(k-1:-1:k-m)`), nikdy `u(k)`.
- [ ] Oneskorenia výstupu ARX nesú **záporné znamienko** v `Phi`.
- [ ] Vyhodnocovať RMSE na **testovacích** dátach pre poctivú presnosť.
- [ ] Preskočiť prvých ~100 prechodových vzoriek pred výpočtom RMSE (`idx_ac=100`).
- [ ] Uhlopriečka paritného grafu musí mať **rovnaké** limity osi x aj y.
- [ ] Pre vyhladzovanie „bez časového oneskorenia" použiť `filtfilt`, nie `filter`.

---

## 14. Mapa prednášok (Ident_2025 — UIAM FCHPT, 11 prednášok, 15.5 h)

Playlist **Ident_2025** je seriál **teoretic­kých prednášok** (semináre sú
praktické cvičenia v MATLABu). Použite ho na prepojenie každej prednášky s príslušným kódom seminára
a príslušnou sekciou týchto poznámok.

| # | Prednáška (názov videa) | Príslušný seminár | Poznámky § |
|---|------------------------|-------------------|------------|
| L01 | Úvod do identifikácie. Vizualizácia dát. | `seminar1.m` | §1, §2 |
| L02 | Úvod do štatistiky | `seminar2.m` | §2, §3 |
| L03 | Odhad konštanty #1 | `seminar3.m`,`seminar4.m` | §2, §4, §5 |
| L04 | Odhad konštanty #2 | `seminar4.m` | §4, §11 |
| L05 | Lineárna regresia #1 | `seminar5.m` | §4, §5 |
| L06 | Lineárna regresia #2 | `seminar6.m` | §6, §8 |
| L07 | Praktické aspekty lineárnej regresie | `seminar7.m` | §7, §8 |
| L08 | Filtrácia dynamických signálov | `seminar8.m` | §9 |
| L09 | Identifikácia dynamických systémov | `seminar9.m` | §10 |
| L10 | Praktické aspekty identifikácie | `seminar10.m`,`seminar11_Flexy2.m` | §10, §11, §12 |
| L11 | **Rekurzívny odhad** | *(žiadny seminár — len teória)* | **§13a** |

- **„Odhad konštanty"** (L03/L04) = odhadovanie jedného parametra z
  opakovaných zašumených meraní (konštanta nádrže `k11` v Seminári 4: aritmetický
  priemer vs. geometrický priemer vs. medián, ich rozptyl cez krabicové grafy).
- **L11 Rekurzívny odhad** je jedinou témou prednášky **bez seminára** — jej
  praktický postup je v novej sekcii §13a nižšie.

---

## 13a. Rekurzívna metóda najmenších štvorcov — RLS (Prednáška L11)

**Myšlienka:** namiesto opätovného výpočtu `X\y` pre *celý* dataset zakaždým, keď príde nová
vzorka, **aktualizujeme** predchádzajúci odhad len s novým meraním.
Používa sa na online / real-time identifikáciu a pre systémy s časovo premennými parametrami.

### RLS aktualizácia (pre každú novú vzorku k)
```matlab
% --- Rekurzívna metóda najmenších štvorcov s faktorom zabúdania ---
lambda = 1;                 % faktor zabúdania: 1 = štandardná RLS (všetky dáta rovnaké)
                            %                    <1 (napr. 0.95..0.99) sleduje zmeny
np     = size(Phi, 2);      % počet parametrov
theta  = zeros(np, 1);      % počiatočný odhad parametrov
P      = 1e6 * eye(np);     % počiatočná kovariancia: veľká = "verím dátam, nie aprióru"
Theta  = zeros(np, N);      % na ukladanie trajektórie parametrov

for k = 1:N
    phi   = Phi(k, :)';                       % aktuálny regresor (stĺpcový vektor)
    e     = y(k) - phi' * theta;              % inovácia / chyba predikcie
    K     = P*phi / (lambda + phi'*P*phi);    % zisk Kalmanovho typu (vektor)
    theta = theta + K * e;                    % KOREKCIA: aktualizácia odhadu
    P     = (P - K*phi'*P) / lambda;          % aktualizácia kovariancie
    Theta(:, k) = theta;                      % zaznamenanie vývoja
end
```

### Čo znamená každý prvok
| Symbol | Význam |
|--------|--------|
| `theta` | aktuálny odhad parametrov (aktualizovaný v každom kroku) |
| `e` | **inovácia** = nová informácia, ktorú vzorka prináša (namerané − predikované) |
| `P` | kovariancia odhadu (klesá s rastúcou istotou) |
| `K` | zisk — ako silno nová chyba koriguje odhad |
| `lambda` | **faktor zabúdania** ∈ (0,1]; `1` = pamätá všetko, `<1` = diskontuje staré dáta |

### Kľúčové fakty na zapamätanie
- Pri `lambda = 1`, po spracovaní **všetkých** N vzoriek dáva RLS **rovnaký
  výsledok ako dávková metóda najmenších štvorcov** `X\y`, vypočítaný postupne. (Striktne presné
  v limite veľkého počiatočného `P`; s konečným `P₀=1e6·I` vyššie je to
  zanedbateľne regularizovaná verzia.)
- **`lambda < 1`** spôsobuje, že odhadovač „zabúda" staré dáta exponenciálne → môže
  **sledovať parametre, ktoré sa menia** (systémy s časovo premennými parametrami). Menšie λ = rýchlejšie
  sledovanie, ale zašumenejšie odhady (kompromis).
- Veľké počiatočné `P` (napr. `1e6·I`) = nízka dôvera v odhad → rýchla počiatočná
  konvergencia. Malé `P` = silná dôvera v počiatočné `theta`.
- RLS je špeciálny prípad **Kalmanovho filtra** (zisk `K` je Kalmanov zisk).
- Vykresliť riadky `Theta` oproti `k` pre zobrazenie konvergencie odhadov k ich skutočným hodnotám.

### Aktualizácia posunu — jednoriadkový rekurzívny postup (L11)
Keď sa posunul len konštantný **absolútny člen** (sklon je stále dobrý), adaptujte len `b`:
```matlab
delta = 0.95;                              % zisk dôvery v [0,1]; ->1 = pomalý/opatrný
for k = 2:N
    yhat = a*x(k-1) + b;                   % predikcia s aktuálnym posunom
    b    = delta*b + (1-delta)*(b + (y(k-1) - yhat));   % filtrovaná aktualizácia posunu
end
```
Rovnaký tvar „odhad ← odhad + zisk × chyba predikcie" ako P regulátor;
`delta→1` ignoruje šumové jednotlivé body, `delta=0` sleduje posledné meranie.

---

## 15. Ťahák funkcií

| Potreba | Funkcia |
|---------|---------|
| Metóda najmenších štvorcov | `X\y` |
| RMSE | `sqrt(mean((yh-y).^2))` / `rmse` |
| Priemer/smerodajná odchýlka/rozptyl/medián | `mean std var median geomean` |
| Hustota pravdepodobnosti/distribučná funkcia/kvantil | `pdf cdf icdf makedist` |
| Histogram | `histogram(...,'Normalization','pdf')` |
| Korelácia | `corrcoef` , `corrplot` |
| Kovariancia | `cov` , `sqrtm` , `eig` , `chol` |
| Analýza hlavných komponentov | `pca` |
| Interval spoľahlivosti regresie | `regress` |
| Filtre | `lowpass highpass filter filtfilt` |
| Rád dynamického modelu | `autocorr parcorr` |
| Prenosová funkcia | `tf idpoly lsim sim` |
| Návrh vstupu | `prbs rand` |
| Spustenie Simulink | `sim('model', time)` |
