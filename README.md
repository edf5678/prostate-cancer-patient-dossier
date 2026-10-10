# patient-dossier

A small Claude skill for keeping a personal medical dossier with an AI assistant without losing track of
where each piece of information came from.

It is not a medical tool and has nothing disease-specific in it. It is a working method:

- a **facts log** (CSV) where every row carries its source (document, DOI/PMID, or "reported by patient");
- **corrections are added next to the old row**, never deleted, so you can see what changed and when;
- an **action list** for the questions to bring to the doctors;
- an **index** of documents that is **audited** both ways (cited files exist, files on disk are cited), and
  helper functions that **fail loudly** instead of silently not writing.

The last point exists because, in practice, an assistant editing an index with search-and-replace can "succeed"
without changing anything; the helpers refuse to do that.

## Files
- `SKILL.md` — the rules the assistant follows.
- `dossier.py` — standard-library Python helpers (no dependencies). Set `DOSSIER_ROOT` to your folder.
- `prostate.md` — optional module for localized prostate cancer: reference cards (Grade Group and % pattern 4,
  cribriform/IDC, PI-RADS / PI-QUAL / PRECISE, PSA density, PSMA PET with PRIMARY and PROMISE, risk groups and
  surveillance, germline vs somatic testing), report templates, a question list and PubMed queries. Each card cites
  a PMID, checked in October 2026.

## Use
Load the skill in your Claude environment (or paste `SKILL.md` as instructions), make `dossier.py`
importable, run `dossier_init()` once.

Written with an AI assistant (Claude). Not medical advice; decisions belong with your clinicians.
License: CC0 — use it however you like.
