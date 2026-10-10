"""Patient dossier helpers: a facts log, an action list and an index that checks itself.

Standard library only. Point DOSSIER_ROOT at your own folder (or pass root=...).
Files used inside the folder:
  FACTS.csv    date,topic,fact,value,source,status,notes
  ACTIONS.csv  n,action,who,when,why,blocked_by
  INDEX.md     a markdown table of documents + the line "**Facts log** (N rows)"
               and the line "**Updated:** dd/mm/yyyy"
"""
import csv
import pathlib
import re
import shutil

DOSSIER_ROOT = "./dossier"
FACTS_HEADER = ["date", "topic", "fact", "value", "source", "status", "notes"]
ACTIONS_HEADER = ["n", "action", "who", "when", "why", "blocked_by"]
STATUSES = ("settled", "open", "disputed", "superseded")


def dossier_dir(root=None):
    return pathlib.Path(DOSSIER_ROOT if root is None else root)


def dossier_init(root=None):
    """Create an empty dossier skeleton (does not overwrite existing files)."""
    D = dossier_dir(root)
    (D / "sources").mkdir(parents=True, exist_ok=True)
    if not (D / "FACTS.csv").exists():
        _write_csv("FACTS.csv", FACTS_HEADER, [], root)
    if not (D / "ACTIONS.csv").exists():
        _write_csv("ACTIONS.csv", ACTIONS_HEADER, [], root)
    if not (D / "INDEX.md").exists():
        (D / "INDEX.md").write_text(
            "# INDEX\n\n**Updated:** 01/01/2000\n\n**Facts log** (0 rows): `FACTS.csv`\n\n"
            "| document | what it is | date |\n|---|---|---|\n| `FACTS.csv` | facts log, one source per row | - |\n")
    return str(D)


def _read_csv(name, root=None):
    rows = list(csv.reader(open(dossier_dir(root) / name, encoding="utf-8")))
    return rows[0], rows[1:]


def _write_csv(name, hdr, body, root=None):
    with open(dossier_dir(root) / name, "w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerows([hdr] + body)


def _update_count(n, root=None):
    p = dossier_dir(root) / "INDEX.md"
    t = p.read_text()
    m = re.search(r"\*\*Facts log\*\* \((\d+) rows\)", t)
    if not m:
        raise RuntimeError("count line '**Facts log** (N rows)' not found in INDEX.md")
    p.write_text(t.replace(m.group(0), f"**Facts log** ({n} rows)", 1))
    return n


def add_facts(rows, root=None):
    """Append rows (lists of 7 fields) to FACTS.csv; returns the new total."""
    hdr, body = _read_csv("FACTS.csv", root)
    for r in rows:
        if len(r) != len(hdr):
            raise ValueError(f"row has {len(r)} fields, expected {len(hdr)}: {r[:3]}")
        if r[5] not in STATUSES:
            raise ValueError(f"status {r[5]!r} not in {STATUSES}")
        if not str(r[4]).strip():
            raise ValueError("every fact needs a source (use 'reported by patient' if undocumented)")
        body.append([str(x) for x in r])
    _write_csv("FACTS.csv", hdr, body, root)
    return _update_count(len(body), root)


def supersede_fact(match, note, root=None):
    """Mark the single fact containing `match` as superseded, appending a dated note. Never deletes."""
    hdr, body = _read_csv("FACTS.csv", root)
    hit = [r for r in body if match in r[2]]
    if len(hit) != 1:
        raise RuntimeError(f"{match!r} matches {len(hit)} facts (need exactly 1)")
    hit[0][5] = "superseded"
    hit[0][6] = (hit[0][6] + " | CORRECTED: " + note).strip(" |")
    _write_csv("FACTS.csv", hdr, body, root)
    return hit[0]


def add_action(action, who, when, why, blocked_by="", root=None):
    hdr, body = _read_csv("ACTIONS.csv", root)
    nid = max([int(r[0]) for r in body if r[0].isdigit()] + [0]) + 1
    body.append([str(nid), action, who, when, why, blocked_by])
    _write_csv("ACTIONS.csv", hdr, body, root)
    return nid


def update_action(n, append=None, when=None, why=None, blocked_by=None, root=None):
    hdr, body = _read_csv("ACTIONS.csv", root)
    hit = [r for r in body if r[0] == str(n)]
    if len(hit) != 1:
        raise KeyError(f"action {n}: found {len(hit)} rows")
    r = hit[0]
    if append:
        r[1] = r[1] + " " + append
    if when is not None:
        r[3] = when
    if why is not None:
        r[4] = why
    if blocked_by is not None:
        r[5] = blocked_by
    _write_csv("ACTIONS.csv", hdr, body, root)
    return r


def add_index_row(path_cited, description, date, before=None, root=None):
    """Insert a table row in INDEX.md just before the row containing `before` (or at the end of the
    table if before is None). Fails loudly if the anchor is missing or the file is already indexed."""
    p = dossier_dir(root) / "INDEX.md"
    t = p.read_text()
    key = "`" + path_cited + "`"
    if key in t:
        raise RuntimeError(f"{key} already in INDEX.md: use index_replace")
    lines = t.split("\n")
    if before:
        idx = [i for i, l in enumerate(lines) if l.startswith("|") and before in l]
        if len(idx) != 1:
            raise RuntimeError(f"anchor {before!r} found in {len(idx)} table rows (need exactly 1)")
        pos = idx[0]
    else:
        rows = [i for i, l in enumerate(lines) if l.startswith("|")]
        if not rows:
            raise RuntimeError("no table found in INDEX.md")
        pos = rows[-1] + 1
    lines.insert(pos, f"| {key} | {description} | {date} |")
    p.write_text("\n".join(lines))
    if key not in p.read_text():
        raise RuntimeError("row not present after writing")
    return pos + 1


def index_replace(old, new, root=None):
    p = dossier_dir(root) / "INDEX.md"
    t = p.read_text()
    c = t.count(old)
    if c != 1:
        raise RuntimeError(f"text to replace found {c} times (need exactly 1)")
    p.write_text(t.replace(old, new))
    return True


def set_updated(date, root=None):
    p = dossier_dir(root) / "INDEX.md"
    t = p.read_text()
    m = re.search(r"\*\*Updated:\*\* (\S+)", t)
    if not m:
        raise RuntimeError("line '**Updated:**' not found")
    p.write_text(t.replace(m.group(0), "**Updated:** " + date, 1))
    return m.group(1), date


def deposit_source(src, subdir, new_name, root=None):
    """Copy (never move) an original document into sources/<subdir>/."""
    d = dossier_dir(root) / "sources" / subdir
    d.mkdir(parents=True, exist_ok=True)
    dst = d / new_name
    shutil.copy(str(src), str(dst))
    return str(dst.relative_to(dossier_dir(root)))


def audit(root=None):
    """Two-way check: every file cited in INDEX.md exists; every .md in the root is cited; count matches."""
    D = dossier_dir(root)
    t = (D / "INDEX.md").read_text()
    cited = set(re.findall(r"`([^`]+\.(?:md|pdf|html|csv|txt|jpg|jpeg|png|docx|xlsx|json))`", t))
    missing = sorted(c for c in cited if not (D / c).exists() and not list(D.rglob(pathlib.Path(c).name)))
    names = {pathlib.Path(c).name for c in cited}
    not_indexed = sorted(f.name for f in D.glob("*.md") if f.name not in names and f.name != "INDEX.md")
    _, body = _read_csv("FACTS.csv", root)
    m = re.search(r"\*\*Facts log\*\* \((\d+) rows\)", t)
    return {"cited_but_missing": missing, "md_not_indexed": not_indexed,
            "facts_rows": len(body), "count_in_index": int(m.group(1)) if m else None}
