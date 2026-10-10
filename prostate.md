# Prostate cancer module (optional add-on to `patient-dossier`)

Reference cards, report templates and question lists for a patient dossier about **localized prostate cancer**.
Every card names its source (PMID). Sources last checked on PubMed in **October 2026**.
This is reading support, **not medical advice**: thresholds change, centres differ, decisions belong to the clinicians.
Guidelines (NCCN, EAU, AUA/ASTRO) are summarised in our own words and linked; their tables are not reproduced.

---

## 1. Reference cards

### 1.1 Gleason score and Grade Group (ISUP)
- Grade Groups 1-5 replace Gleason sums: GG1 = 3+3, **GG2 = 3+4**, GG3 = 4+3, GG4 = 8, GG5 = 9-10.
  Sources: ISUP 2014 consensus, PMID 26492179; validation, PMID 26166626.
- 2019 ISUP update (PMID 32459716): report the **percentage of pattern 4** in GG2-3, and report
  **cribriform** and **intraductal carcinoma (IDC-P)** explicitly.
- Why "how much 4" matters: in biopsy GG2 without cribriform/IDC, % pattern 4 independently predicted upgrading at
  surgery (PMID 36190529); % or mm of pattern 4 predicted metastasis better than Grade Group alone (PMID 40774801).
- **Read pattern 4 per lesion, not as one number.** A report may give different % for each core; the highest
  value is not "the" value of the case.
- Cribriform and IDC are under-sampled by biopsy: in one series, MRI-assisted biopsy had a sensitivity of only about
  20-30% for the cribriform/IDC later found at surgery (PMID 40614127). "Absent on biopsy" ≠ "absent".
- Inter-observer agreement on the 3/4 boundary is imperfect: a **second pathology review** at a high-volume centre
  is a common, reasonable step.

### 1.2 MRI: PI-RADS, PI-QUAL, PRECISE
- **PI-RADS v2.1** (PMID 30898406): 1-5 likelihood of clinically significant cancer per lesion; 3 = equivocal.
- **PI-QUAL** (PMID 32646850): 1-5 score of image quality. A report mentioning motion artefacts is a reason to ask
  whether quality was adequate.
- **PRECISE** (PMID 27349615): standard for comparing serial MRIs in active surveillance (likelihood of real change
  between scans). Worth asking for if surveillance is chosen.
- **MRI-invisible cancer exists.** MRI has a 10-20% false-negative rate for significant cancer; in one fusion-biopsy
  series 13% of men had GG2+ cancer in zones without any MRI lesion (PMID 33568751).
  This is why **systematic cores are taken in addition to targeted ones**; combined biopsy reduces grade
  misclassification compared with either method alone (PMID 32130814).

### 1.3 PSA density
- PSA density = PSA / prostate volume (ng/ml/cc). Common rule of thumb: 0.15.
- **It depends on gland size**: in a 2026 series of 2190 men, PSAd performed differently across volumes and
  PI-RADS categories; at a 10% risk threshold the optimal cut-offs were about 0.20 for PI-RADS 1-2 and 0.12 for PI-RADS 3 (PMID 41484253).
  In small glands a "high" density is reached easily; in large glands PSAd is less informative.
- Volume is often missing from MRI reports (PI-RADS recommends reporting it). Ask for the number and the method
  (ellipsoid formula vs segmentation), and use the PSA value from **before** the biopsy.

### 1.4 PSMA PET
- **PROMISE / miTNM** (PMID 29123012; v2, PMID 36935345): standard reporting framework, includes a PSMA-expression
  score (miPSMA) that compares the lesion with reference organs (blood pool, liver, parotids or spleen).
- **PRIMARY score** (PMID 35301240): intraprostatic pattern 1-5; focal peripheral-zone uptake = 4;
  SUVmax ≥ 12 = 5. Developed with **68Ga-PSMA-11**; thresholds do not transfer automatically to 18F tracers.
- **SUVmax is not comparable across tracers, scanners and reconstructions.** Compare with reference organs in the
  same scan, and with the centre's own experience. Small single-centre studies link intense focal uptake to upgrading
  at surgery (e.g. PMID 42489410, 34 patients) — association, not a grading tool.
- The PET report answers the question written on the request. If the question is "staging", intraprostatic detail
  (SUVmax, sector-by-sector description, PRIMARY) may simply not be reported: ask for it, and for the DICOM disc.

### 1.5 Risk groups and active surveillance
- Risk groups (NCCN, EAU, AUA/ASTRO) combine PSA, Grade Group, stage and extent; "favourable intermediate" is
  where surveillance vs treatment is most debated. AUA/ASTRO 2022: PMID 35536144 (Part I), with Parts II-III.
- Surveillance criteria for GG2 **vary between centres** (number/extent of positive cores, % pattern 4, absence of
  cribriform/IDC, PSA density, MRI and sometimes PET or genomic tests). Ask which criteria *this* centre uses.
- Germline testing: the Philadelphia consensus (PMID 32516092) recommends it with metastatic disease or a family
  history suggestive of hereditary cancer; **BRCA2 is relevant to surveillance discussions**.
  Note: a **somatic** test on tumour tissue is not the same as a **germline** (inherited) test on blood or saliva.

### 1.6 Treatment evidence, if it comes to that
- SBRT in 5 fractions: PACE-B (PMID 39413377) — low/intermediate risk, **ADT not permitted**, non-inferior to longer
  schedules. NRG-GU005 (JAMA 2026, PMID 42593775) compared SBRT with moderate hypofractionation in intermediate
  risk; read the full text for the oncological outcomes before citing numbers.
- Focal therapy (HIFU, IRE, cryo): good functional results, retreatment common, no randomised comparison with
  surgery or radiotherapy, limited long-term data. Eligibility usually requires a visible index lesion and no
  significant cancer outside the treated zone — MRI-invisible cores matter here.

---

## 2. Templates

### 2.1 Biopsy report, core by core
| core | site | systematic / targeted (which target) | length mm | % cancer | Gleason | % pattern 4 | cribriform | IDC-P | PNI |
|---|---|---|---|---|---|---|---|---|---|

Add: number of cores and containers (a "sample" may contain several fragments — counting conventions differ),
biopsy route (transperineal / transrectal), fusion system used.

### 2.2 What an MRI report should contain
Field strength · sequences · **gland volume (and method)** · each lesion: PI-RADS, zone, sector, size, ADC ·
extraprostatic extension · seminal vesicles · nodes · quality (PI-QUAL if available).

### 2.3 What a PSMA PET report should contain
Tracer (exact molecule) · injected activity · uptake time · scanner · intraprostatic: pattern, sector, **SUVmax**,
PRIMARY · nodes · bone · other findings with SUV · reference organ values · miTNM.

---

## 3. Questions some patients found useful (use any, none, or your own)
1. What is the gland volume, and which PSA did you use for density?
2. What is the % pattern 4 in each positive core? Any cribriform or intraductal pattern?
3. Were systematic cores taken as well as targeted ones? Did any positive core come from a zone the MRI didn't show?
4. Can the slides be reviewed by a second pathologist?
5. Which surveillance criteria does your centre use for GG2, and do I meet them?
6. Is germline testing indicated given my family history?
7. For the PET: what is the SUVmax, which tracer, and is there uptake in the sector of each positive core?
8. Can I have the images (MRI, PET) and, for fusion biopsy, the targeting screenshots?
9. If surveillance: what is the schedule (PSA, MRI with PRECISE, confirmatory biopsy), and what triggers treatment?

---

## 4. Lessons learned (general)
- An exam answers the question written on the request. Write the specific question on it.
- Always ask for the images on disc; reports are summaries for other doctors.
- Keep pattern 4 per lesion; don't let the worst core become "the case".
- MRI-invisible ≠ cancer-free; PET-negative in one sector ≠ cancer-free there.
- Record what clinicians say in the visit as "reported", next to the written report; both matter.
- Don't compare SUVmax numbers across centres or tracers.

## 5. PubMed queries that proved useful
- `("active surveillance") AND ("grade group 2" OR "favorable intermediate") AND ("pattern 4")`
- `(PSMA PET) AND ("active surveillance") AND (upgrading OR reclassification OR progression)`
- `(MRI-invisible) AND prostate cancer AND (systematic biopsy OR outcomes)`
- `("PSA density") AND (prostate volume) AND threshold AND (PI-RADS 3)`
- `(cribriform OR intraductal) AND biopsy AND (active surveillance OR radical prostatectomy) AND sensitivity`
- `(focal therapy OR hemiablation) AND prostate AND (outcomes OR retreatment)`

*Written with an AI assistant (Claude). Not medical advice.*
