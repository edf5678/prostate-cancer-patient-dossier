---
name: patient-dossier
description: "Notes for an AI assistant helping a patient keep their own medical dossier: how one patient and an assistant worked together over several months, what helped, what went wrong. A source of ideas, not a rulebook. Optional helpers in dossier.py, optional prostate cancer module in prostate.md."
---

# Patient dossier — notes from one way of working

These notes come from several months of work between one patient and an AI assistant, on a real diagnosis.
They are **not rules**. Every patient, illness and doctor is different; take what fits, change what doesn't, and
let the patient decide how they want to work. The patient's own conventions always come first.

---

## 1. Who leads

The patient leads. The assistant reads, searches, organises, measures, drafts — and the patient decides what to
keep, what to send, what to ask, and what to do. Some things the patient in these notes told the assistant along
the way, which changed how it worked:

- *"Make it clear you wrote it, so others know."* — every document said on its first line that an AI wrote it, and when.
- *"No blocks, only facts — the other session will do the analysis."* — handover notes between sessions carried facts, not advice.
- *"If the text is simple I read it in markdown, don't waste energy on Word or PDF."* — format followed the use.
- *"I'm not going to pick the slides myself."* — technical choices belong to the professionals; the patient informs.
- *"It's not true that cure comes first for me. I'm not in a hurry."* — the assistant had projected someone else's priorities.
- *"That sounds like a schoolteacher."* — drafts written for the patient to post should tell what *they* did, not what others should do.

The pattern: listen for these corrections, write them down, and keep applying them.

## 2. Facts, and where they come from

What helped most was a plain table of facts (`FACTS.csv`) where **every line has its source**: a report in the
folder, a PMID/DOI, or *"reported by the patient"*. A few habits that grew around it:

- **Read the source before writing.** Open the PDF, the abstract, the email. Several times the "remembered" number
  was wrong — a PSA value from the wrong date, a percentage rounded in a visit note, a figure from a lay article
  instead of the paper.
- **Keep "said" separate from "written".** What a doctor said in a visit is valuable; record it as a quote,
  marked as reported, next to the written report. They often say more than the report does.
- **Correct alongside, don't delete.** A wrong line becomes "superseded" with a dated note, and the correction is a
  new line. Months later you can still see what was believed and why it changed.
- **Check what other tools say.** Texts from other chatbots or forums were useful leads and often partly wrong
  (an outdated scanner model, an invented contact address). Each claim was verified before entering the table.

## 3. Reading reports

- **A report answers the question written on the request.** A PET requested as "staging" reports metastases, not
  the sector-by-sector detail inside the gland. An MRI may not report gland volume. That is not negligence; it is
  a reason to write the specific question on the next request.
- **Read the whole report, slowly.** Re-reading line by line found things nobody had noticed: which PSA value had
  been used, that lesions were measured but the gland was not.
- **Ask for the images.** Reports are summaries for other doctors; the disc holds much more.
- **Don't let the worst number become "the case".** One core with 20% of a pattern and three at 10% is not "20%".

## 4. Images

With the patient's explicit permission, the assistant went beyond inventorying DICOM files:

- **Measurements and geometry first**: reference-organ values, distances, which slices cover what, registering
  one exam onto another on bone.
- **Interpretations labelled as hypotheses**, each with a confidence level, the method and the limits
  (e.g. "alignment uncertainty 5-10 mm, the same scale as the question being asked"). Never a diagnosis.
- **Help the patient measure, and check the result.** A first value from a home viewer turned out to be the
  bladder, not the lesion; the shape of the region (volume, minimum value) gave it away.
- **Say when the honest answer is "can't tell from here"**, and say who can (a fused read at the centre, the
  biopsy system screenshots).

## 5. Literature

- Query PubMed directly; keep the search strings; **read the abstracts in full**, not just titles.
- **No published cohort will match the patient exactly.** Say which features match and which don't.
- **Show both directions.** The same search often returned a reassuring and a worrying finding; both went in.
- Thresholds depend on context (tracer, scanner, gland size, population). Say so before comparing a number.
- Report what you didn't find, and which numbers you didn't verify at the source.

## 6. Mistakes that happened (and what helped)

- **An index row silently not written**: a search-and-replace looked for text that wasn't there, and "succeeded".
  Helpers that fail loudly, plus an audit at the end of each session, fixed it.
- **A date in the index header frozen for weeks**, for the same reason.
- **"The package has arrived"** written before anyone knew. State only what is recorded.
- **A first answer that was wrong in approach** (suggesting the patient choose which slides to send). Saying so
  plainly, and correcting, kept trust.
- **Publishing**: copying from a rendered preview stripped the markdown; a first upload exposed a personal email in
  the commit. Checking the published result byte by byte caught both.

## 7. Tone

- Plain language, one idea per sentence, the number with its unit and its source.
- Good news and bad news in the same voice. Don't reassure beyond the evidence, don't alarm beyond it either.
- The patient's questions, not the assistant's agenda. Offer, don't push.
- Every document ends by saying what it is: a reading or organisation note, not medical advice.

---

## Optional helpers (`dossier.py`)

Standard-library Python, for those who want the table and index kept consistent automatically:
`dossier_init`, `add_facts` (refuses a fact with no source), `supersede_fact`, `add_action`, `update_action`,
`add_index_row` (errors if the anchor row is missing), `index_replace` (errors unless the text occurs once),
`set_updated`, `deposit_source` (copies, never moves), `audit` (two-way index check).

## Optional disease module

`prostate.md`: reference cards with PMIDs, report templates, questions others found useful, lessons and PubMed
queries for localized prostate cancer. Checked in October 2026; it will age, so each card carries its source.

*Written with an AI assistant (Claude), from one patient's experience. Not medical advice.*
