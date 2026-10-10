# patient-dossier

Notes for an AI assistant helping a patient keep their own medical dossier, drawn from several months of real work
between one patient and an assistant (Claude) on a prostate cancer diagnosis.

It is **a source of ideas, not a rulebook**: how the work was organised, what helped, what went wrong, how the
patient corrected the assistant along the way. Take what fits your situation and change the rest.

## Files
- `SKILL.md` — the notes themselves: who leads, keeping every fact tied to its source, reading reports, images,
  literature, mistakes that happened, tone.
- `dossier.py` — optional standard-library Python helpers that keep a facts table and an index consistent, and
  fail loudly instead of silently not writing.
- `prostate.md` — optional module for localized prostate cancer: reference cards (Grade Group and % pattern 4,
  cribriform/IDC, PI-RADS / PI-QUAL / PRECISE, PSA density, PSMA PET, risk groups and surveillance, germline vs
  tissue testing), report templates, questions others found useful, PubMed queries. Each card cites a PMID,
  checked in October 2026.

## Use
Load `SKILL.md` as a skill (or paste it as instructions). The helpers and the module are optional.

Written with an AI assistant (Claude). Not medical advice; decisions belong with you and your clinicians.
License: CC0 — use it however you like.
