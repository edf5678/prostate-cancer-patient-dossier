---
name: patient-dossier
description: "Keep a personal medical dossier in a local folder: a facts log where every line has its source, an action list, and an index that checks itself. Load in every session that reads or writes the dossier."
---

# Patient dossier — working method

The dossier is a folder (set `DOSSIER_ROOT` in `dossier.py`, or pass `root=`). Entry point: `INDEX.md`.
Facts log: `FACTS.csv` (`date,topic,fact,value,source,status,notes`). Actions: `ACTIONS.csv`.
Originals (reports, lab PDFs, images) live in `sources/` and are copied there, never moved or edited.

## Rules
- **Every fact has a source**: a document in `sources/`, a DOI/PMID, or the words `reported by patient`.
  Do not promote something the patient said to a documented fact.
- **Verify at the source before writing**: read the PDF, the abstract, the email. Do not quote numbers from memory.
- **Never delete, correct alongside**: a wrong fact becomes `superseded` with a dated note (`supersede_fact`),
  and the correction is a new row.
- **Status** is one of `settled` / `open` / `disputed` / `superseded`.
- **Say who wrote what**: every document written by the AI says so on its first line, with the date.
- **AI interpretations are labelled as such** (topic `AI hypothesis`, status `open`), with method and limits.
- **No clinical decisions**: documents end by stating they are organisation/reading notes, not medical advice.
  Questions for the doctors go in `ACTIONS.csv`.
- **Handover notes contain facts only**, no recommendations.
- **The index is checked, not trusted**: every write goes through the helpers, which fail loudly; run `audit()`
  at the end of every session (`cited_but_missing` must be empty, `md_not_indexed` should be empty,
  `facts_rows == count_in_index`).
- Never delete files in the dossier folder.

## Helpers (`dossier.py`)
- `dossier_init()` — create the skeleton.
- `add_facts(rows)` — append 7-field rows; refuses rows without source or with an unknown status; updates the count.
- `supersede_fact(match, note)` — mark one fact as superseded with a correction note.
- `add_action(...)`, `update_action(n, ...)`.
- `add_index_row(path, description, date, before=None)` — errors if the anchor row is missing or the file is already indexed.
- `index_replace(old, new)` — errors unless `old` occurs exactly once.
- `set_updated(date)`, `deposit_source(src, subdir, new_name)`, `audit()`.

## Disease modules
Optional files with reference cards, report templates and question lists, e.g. `prostate.md`.
Load the module only when relevant; every card cites its source and the date it was last checked.

## Typical session
1. Read the new document at its source; write the reading note (`.md`) in the dossier root.
2. `add_facts([...])`; `add_action(...)` for questions to bring to the doctors.
3. `add_index_row(...)`; `set_updated(...)`.
4. `audit()` — fix anything it reports before closing.
