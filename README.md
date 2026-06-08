# System Identification — Lecture Notes & Exam Prep

Strict-fidelity Markdown notes for the **System Identification** course
(*Identifikácia*, UIAM FCHPT STU), reconstructed from the **Ident_2025** YouTube
lecture playlist, plus study material for the exam.

> The notes are built **only** from what each lecturer actually says in the video
> (caption transcripts), with formulas cross-checked against the lecturer's own
> slide PDFs. No outside facts or invented examples were added. Where a caption
> garbled a formula or name, an inline `<!-- unclear: ... -->` comment marks it
> instead of guessing.

## Lectures

One Markdown file per video, in [`lectures/`](lectures/). All lectures are in
**English**.

| # | Notes | Video |
|---|-------|-------|
| L01 | [Introduction to Identification. Data Visualization.](lectures/L01_Introduction_to_Identification.md) | [PZz7OA9_4Gw](https://www.youtube.com/watch?v=PZz7OA9_4Gw) |
| L02 | [Introduction to Statistics](lectures/L02_Introduction_to_Statistics.md) | [laEQig6EanE](https://www.youtube.com/watch?v=laEQig6EanE) |
| L03 | [Estimation of a Constant #1](lectures/L03_Estimation_of_a_Constant_1.md) | [G6Auo4Mw_V0](https://www.youtube.com/watch?v=G6Auo4Mw_V0) |
| L04 | [Estimation of a Constant #2](lectures/L04_Estimation_of_a_Constant_2.md) | [PXgpgTrh07Y](https://www.youtube.com/watch?v=PXgpgTrh07Y) |
| L05 | [Linear Regression #1](lectures/L05_Linear_Regression_1.md) | [J6QAT6-BkDY](https://www.youtube.com/watch?v=J6QAT6-BkDY) |
| L06 | [Linear Regression #2](lectures/L06_Linear_Regression_2.md) | [DLTnS_SWr_k](https://www.youtube.com/watch?v=DLTnS_SWr_k) |
| L07 | [Practical Aspects of Linear Regression](lectures/L07_Practical_Aspects_of_Linear_Regression.md) | [HqCN0mFgmTQ](https://www.youtube.com/watch?v=HqCN0mFgmTQ) |
| L08 | [Filtration of Dynamic Signals](lectures/L08_Filtration_of_Dynamic_Signals.md) | [nAS4yAqv5ak](https://www.youtube.com/watch?v=nAS4yAqv5ak) |
| L09 | [Identification of Dynamic Systems](lectures/L09_Identification_of_Dynamic_Systems.md) | [WEGsY_W654g](https://www.youtube.com/watch?v=WEGsY_W654g) |
| L10 | [Practical Aspects of Identification](lectures/L10_Practical_Aspects_of_Identification.md) | [uuRbAaWFfmQ](https://www.youtube.com/watch?v=uuRbAaWFfmQ) |
| L11 | [Recursive Estimation](lectures/L11_Recursive_Estimation.md) | [cTlkFkwKV4U](https://www.youtube.com/watch?v=cTlkFkwKV4U) |

Course arc: **statistics → estimating a constant → linear regression → its
practical aspects → filtering → dynamic-system models (FIR/ARX/ARMAX) → practical
identification → recursive estimation**.

## Exam preparation

Three study files for the exam (oral theory + practical MATLAB):

- [`Exam_Prep_1_Practical_MATLAB.md`](Exam_Prep_1_Practical_MATLAB.md) — reusable
  MATLAB templates for the full identification workflow (load → clean →
  standardize → split → least squares → RMSE → compare), FIR/ARX/ARMAX, RLS.
- [`Exam_Prep_2_Oral_Theory.md`](Exam_Prep_2_Oral_Theory.md) — explain-in-words Q&A
  behind every concept, plus per-topic "talk tracks".
- [`Exam_Prep_3_Topic_Sheets.md`](Exam_Prep_3_Topic_Sheets.md) — one printable sheet
  per exam topic: what to put on the board, formulas, likely follow-ups.

## Repository layout

```
lectures/        L01–L11 Markdown notes (the main deliverable)
transcripts/     raw .vtt caption downloads (en-orig + en) used to build the notes
Prednásky/       the lecturers' slide PDFs, used to verify/repair garbled formulas
Exam_Prep_*.md   exam study guides
clean_vtt.py     strips VTT timestamps/tags and de-duplicates rolling captions
```

## How the notes were built

1. **Download captions** with `yt-dlp` (auto-generated subtitles; the videos are
   public, so no login is needed):

   ```bash
   yt-dlp --skip-download --write-auto-subs --sub-langs "en-orig,en.*" \
     --sub-format vtt -o "transcripts/%(playlist_index)02d_%(id)s.%(ext)s" \
     "https://www.youtube.com/playlist?list=PLXyoIl3CJDekre01DKPmvoHd768rc1BBH"
   ```

2. **Clean** each transcript: `python clean_vtt.py` strips cue timestamps and the
   inline word tags, then collapses the rolling-caption duplication into continuous
   text (output goes to `transcripts/clean/`, which is git-ignored).

3. **Write the notes** from the cleaned text, following each lecture's actual flow.
   Formulas are typeset in LaTeX only where the lecturer states them, and verified
   against the matching slide deck in `Prednásky/` where one exists (L01, L02, L05,
   L06, L07, L08, L09, L11). L03, L04 and L10 had no matching slides and are
   transcript-only.

## Notes on the source material

- Every video had usable captions; none were missing.
- All transcripts are **English** (the `en-orig` track) — there are no Slovak
  captions, though Slovak technical terms the lecturer says are kept in place.
- `<!-- unclear -->` markers are rare (mostly garbled proper nouns in L01); their
  low density means the transcripts are good quality.

## Math rendering

Display equations use `$$ … $$` on their own lines and avoid GitHub's
disallowed macros (e.g. `\mathrm` instead of `\operatorname`), so they render on
both **GitHub** and **Obsidian**. The notes use Obsidian-compatible YAML
frontmatter.

## Attribution

Source: the **Ident_2025** lecture playlist (System Identification, UIAM FCHPT
STU Bratislava). These are unofficial student notes derived from the public
lecture recordings; all course content belongs to its authors.
