# Identifikácia systémov — Poznámky z prednášok a príprava na skúšku

Poznámky s prísnou vernosťou zdrojovému materiálu pre kurz **Identifikácia systémov**
(*Identifikácia*, UIAM FCHPT STU), zrekonštruované z YouTube playlistu prednášok
**Ident_2025**, doplnené o študijný materiál na skúšku.

> Poznámky sú zostavené **výlučne** z toho, čo každý prednášajúci v danom videu skutočne hovorí
> (prepisy titulkov), pričom vzorce sú overené podľa vlastných PDF prezentácií prednášajúceho.
> Neboli pridané žiadne externé fakty ani vymyslené príklady. Kde titulok skomolil
> vzorec alebo meno, je to na danom mieste označené komentárom `<!-- unclear: ... -->`
> namiesto hádania.

## Prednášky

Jeden súbor Markdown na každé video, v priečinku [`lectures/`](lectures/). Všetky prednášky sú
v **angličtine** (zdrojové prepisy titulkov sú v angličtine; poznámky sú napísané po **slovensky**).

| # | Poznámky | Video |
|---|----------|-------|
| L01 | [Úvod do identifikácie. Vizualizácia dát.](lectures/L01_Introduction_to_Identification.md) | [PZz7OA9_4Gw](https://www.youtube.com/watch?v=PZz7OA9_4Gw) |
| L02 | [Úvod do štatistiky](lectures/L02_Introduction_to_Statistics.md) | [laEQig6EanE](https://www.youtube.com/watch?v=laEQig6EanE) |
| L03 | [Odhad konštanty #1](lectures/L03_Estimation_of_a_Constant_1.md) | [G6Auo4Mw_V0](https://www.youtube.com/watch?v=G6Auo4Mw_V0) |
| L04 | [Odhad konštanty #2](lectures/L04_Estimation_of_a_Constant_2.md) | [PXgpgTrh07Y](https://www.youtube.com/watch?v=PXgpgTrh07Y) |
| L05 | [Lineárna regresia #1](lectures/L05_Linear_Regression_1.md) | [J6QAT6-BkDY](https://www.youtube.com/watch?v=J6QAT6-BkDY) |
| L06 | [Lineárna regresia #2](lectures/L06_Linear_Regression_2.md) | [DLTnS_SWr_k](https://www.youtube.com/watch?v=DLTnS_SWr_k) |
| L07 | [Praktické aspekty lineárnej regresie](lectures/L07_Practical_Aspects_of_Linear_Regression.md) | [HqCN0mFgmTQ](https://www.youtube.com/watch?v=HqCN0mFgmTQ) |
| L08 | [Filtrácia dynamických signálov](lectures/L08_Filtration_of_Dynamic_Signals.md) | [nAS4yAqv5ak](https://www.youtube.com/watch?v=nAS4yAqv5ak) |
| L09 | [Identifikácia dynamických systémov](lectures/L09_Identification_of_Dynamic_Systems.md) | [WEGsY_W654g](https://www.youtube.com/watch?v=WEGsY_W654g) |
| L10 | [Praktické aspekty identifikácie](lectures/L10_Practical_Aspects_of_Identification.md) | [uuRbAaWFfmQ](https://www.youtube.com/watch?v=uuRbAaWFfmQ) |
| L11 | [Rekurzívny odhad](lectures/L11_Recursive_Estimation.md) | [cTlkFkwKV4U](https://www.youtube.com/watch?v=cTlkFkwKV4U) |

Oblúk kurzu: **štatistika → odhad konštanty → lineárna regresia → jej
praktické aspekty → filtrácia → modely dynamických systémov (FIR/ARX/ARMAX) → praktická
identifikácia → rekurzívny odhad**.

## Príprava na skúšku

Tri študijné súbory na skúšku (ústna teória + praktický MATLAB). Všetky vzorce sú
sadzané v LaTeXu, takže sa správne zobrazia na GitHube aj v Obsidiane:

- [`Exam_Prep_1_Practical_MATLAB.md`](Exam_Prep_1_Practical_MATLAB.md) — opakovateľne použiteľné
  MATLAB šablóny pre celý pracovný postup identifikácie (načítanie → čistenie →
  štandardizácia → rozdelenie → metóda najmenších štvorcov → RMSE → porovnanie), FIR/ARX/ARMAX, RLS.
- [`Exam_Prep_2_Oral_Theory.md`](Exam_Prep_2_Oral_Theory.md) — otázky a odpovede vysvetľujúce
  každý koncept vlastnými slovami, vrátane „osnov výkladu" pre každú tému.
- [`Exam_Prep_3_Topic_Sheets.md`](Exam_Prep_3_Topic_Sheets.md) — jeden vytlačiteľný list
  pre každú tému skúšky: čo napísať na tabuľu, vzorce, pravdepodobné doplňujúce otázky.

## Štruktúra repozitára

```
lectures/        L01–L11 poznámky v Markdown (hlavný výstup)
transcripts/     surové .vtt titulky (en-orig + en) použité na zostavenie poznámok
Prednásky/       PDF prezentácií prednášajúcich, použité na overenie/opravu skomolených vzorcov
Exam_Prep_*.md   študijné príručky na skúšku
clean_vtt.py     odstraňuje VTT časové značky/tagy a odstraňuje duplicity z posúvajúcich sa titulkov
```

## Ako boli poznámky zostavené

1. **Stiahnutie titulkov** pomocou `yt-dlp` (automaticky generované titulky; videá sú
   verejné, takže nie je potrebné prihlásenie):

   ```bash
   yt-dlp --skip-download --write-auto-subs --sub-langs "en-orig,en.*" \
     --sub-format vtt -o "transcripts/%(playlist_index)02d_%(id)s.%(ext)s" \
     "https://www.youtube.com/playlist?list=PLXyoIl3CJDekre01DKPmvoHd768rc1BBH"
   ```

2. **Čistenie** každého prepisu: `python clean_vtt.py` odstraňuje časové značky titulov a
   vnorené slovo-úrovňové tagy, potom zlučuje opakujúce sa posúvajúce sa titulky do súvislého
   textu (výstup ide do `transcripts/clean/`, ktorý je ignorovaný gitom).

3. **Písanie poznámok** z vyčisteného textu podľa skutočného postupu každej prednášky.
   Vzorce sú sadzané v LaTeXu len tam, kde ich prednášajúci uvádza, a overené
   oproti príslušnej prezentácii v `Prednásky/`, kde taká existuje (L01, L02, L05,
   L06, L07, L08, L09, L11). L03, L04 a L10 nemali zodpovedajúce prezentácie a sú
   len na základe prepisu.

## Poznámky k zdrojovému materiálu

- Každé video malo použiteľné titulky; žiadne nechýbali.
- Všetky prepisy sú v **angličtine** (stopa `en-orig`) — slovenské titulky neexistujú,
  hoci slovenské odborné termíny, ktoré prednášajúci vysloví, sú ponechané na mieste.
- Značky `<!-- unclear -->` sú zriedkavé (väčšinou skomolené vlastné mená v L01); ich
  nízka hustota znamená, že prepisy sú dobrej kvality.

## Zobrazovanie matematiky

Všetky súbory Markdown — poznámky z prednášok **aj** tri príručky na prípravu na skúšku —
sadzajú matematiku pomocou `$ … $` (inline) a `$$ … $$` (zobrazenie), takže sa správne zobrazí na oboch
platformách — **GitHub** aj **Obsidian**. Dve pravidlá zaručujú kompatibilitu blokov so zobrazenín na GitHube:

- **Vyhýbať sa nedovoleným makrám GitHubu** (napr. `\mathrm` namiesto `\operatorname`).
- **Nikdy nenechať osamotené `=` (alebo `-`) na riadku vo vnútri bloku `$$`.** GitHub
  parsuje blokovú štruktúru *pred* matematikou, takže osamotené `=` sa interpretuje ako setext `<h1>`
  podčiarknutie a celá rovnica sa zobrazí ako obrovský nadpis (s doslovne zobrazeným LaTeXom). Udržujte `=`
  na rovnakom riadku ako jeho ľavá strana, alebo použite
  `&=` vo vnútri `\begin{aligned} … \end{aligned}`.

Poznámky z prednášok tiež používajú YAML frontmatter kompatibilný s Obsidianom.

## Zdroj

Zdroj: playlist prednášok **Ident_2025** (Identifikácia systémov, UIAM FCHPT
STU Bratislava). Sú to neoficiálne študentské poznámky odvodené z verejných
záznamov prednášok; všetok obsah kurzu patrí jeho autorom.
