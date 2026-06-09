# System Identification — Notes & Exam Prep · Identifikácia — Poznámky a príprava na skúšku

Bilingual study material for the **System Identification** course (*Identifikácia*,
UIAM FCHPT STU Bratislava), reconstructed from the **Ident_2025** YouTube lecture
playlist. The same content is available in two languages.

Dvojjazyčný študijný materiál k predmetu **Identifikácia** (UIAM FCHPT STU
Bratislava), zostavený z playlistu prednášok **Ident_2025**. Rovnaký obsah je
dostupný v dvoch jazykoch.

## Languages · Jazykové verzie

| | Folder | Contents · Obsah |
|---|---|---|
| 🇬🇧 **English** | [`en/`](en/) | [README](en/README.md) · [lecture notes L01–L11](en/lectures/) · exam prep |
| 🇸🇰 **Slovenčina** | [`sk/`](sk/) | [README](sk/README.md) · [poznámky L01–L11](sk/lectures/) · príprava na skúšku |

Each language folder contains its own README, the 11 lecture notes (L01–L11), and
the three exam-prep guides (practical MATLAB, oral theory, topic sheets). · Každý
jazykový priečinok obsahuje vlastný README, 11 poznámok z prednášok a tri prípravné
materiály na skúšku.

## Shared source material (repository root) · Spoločné zdroje (koreň repozitára)

- [`transcripts/`](transcripts/) — raw `.vtt` caption downloads used to build the notes · surové titulky, z ktorých sú poznámky zostavené.
- [`Prednásky/`](Prednásky/) — the lecturers' slide PDFs · snímky prednášajúcich (na overenie vzorcov).
- [`clean_vtt.py`](clean_vtt.py) — strips VTT timestamps/tags and de-duplicates captions · čistenie titulkov.

These are language-independent and shared by both versions. · Tieto sú nezávislé od
jazyka a zdieľané oboma verziami.

## Math rendering · Vykresľovanie matematiky

All notes typeset math with `$ … $` (inline) and `$$ … $$` (display) so they render
on both **GitHub** and **Obsidian**. Two rules keep the display blocks GitHub-safe:
never leave a bare `=` (or `-`) alone on a line inside a `$$` block (GitHub reads it
as a setext heading and the equation breaks), and prefer a `$$` display block over a
long inline `$…$` formula that shares its line with another inline span.

## Attribution · Pôvod

Source: the **Ident_2025** lecture playlist (System Identification, UIAM FCHPT STU
Bratislava). These are unofficial student notes derived from the public lecture
recordings; all course content belongs to its authors. · Neoficiálne študentské
poznámky odvodené z verejných záznamov prednášok; všetok obsah predmetu patrí jeho
autorom.
