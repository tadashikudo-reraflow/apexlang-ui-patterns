#!/usr/bin/env python3
"""Check routing targets, frontmatter, example paths, eval JSON and CSS variable names."""
import argparse
import json
import re
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("root", nargs="?")
parser.add_argument("--ut-vars", help="CSS variable list; without it the CSS variable check is skipped")
args = parser.parse_args()
ROOT = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
PLACEHOLDERS = {"--u-color-N"}
errors = []


def read(rel):
    try:
        return (ROOT / rel).read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{rel}: cannot read ({exc.strerror})")
    except UnicodeDecodeError:
        errors.append(f"{rel}: not UTF-8")
    return ""


def frontmatter_error(text):
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return "frontmatter is missing"
    if "---" not in lines[1:]:
        return "frontmatter is not closed"
    block = lines[1 : lines.index("---", 1)]
    for line in block:
        if line.strip() and not re.match(r"[\w-]+:(\s|$)|\s|#", line):
            return "frontmatter is not closed before the body"
    for index, line in enumerate(block):
        match = re.match(r"description:(.*)$", line)
        if match:
            value = match.group(1).strip()
            rest = block[index + 1 :]
            body = next((item for item in rest if item.strip()), "")
            continued = body.startswith((" ", "\t"))
            if value.strip("\"'") and value not in (">", "|", ">-", "|-", ">+", "|+") or continued:
                return None
            return "frontmatter description is empty"
    return "frontmatter description is missing"


known = None
if args.ut_vars:
    known = {
        line.strip().split()[0]
        for line in read(args.ut_vars).splitlines()
        if line.strip().startswith("--")
    }

skill = read("SKILL.md")
table = "\n".join(line for line in skill.splitlines() if line.startswith("|"))
routed = set(re.findall(r"references/[\w./-]+\.\w+", table))
for target in sorted(routed):
    if not (ROOT / target).is_file():
        errors.append(f"SKILL.md: missing target {target}")

docs = sorted((ROOT / "references").rglob("*.md"))
for doc in docs:
    rel = doc.relative_to(ROOT).as_posix()
    text = read(rel)
    if rel not in routed:
        errors.append(f"{rel}: not in the SKILL.md routing table")
    problem = frontmatter_error(text)
    if problem:
        errors.append(f"{rel}: {problem}")
    for target in sorted(set(re.findall(r"examples/[\w./-]+\.\w+", text))):
        if not (ROOT / target).is_file():
            errors.append(f"{rel}: missing example {target}")

css_docs = list(docs)
for folder in ("proposals", "examples"):
    for pattern in ("*.md", "*.html", "*.css"):
        css_docs += sorted((ROOT / folder).rglob(pattern))
for doc in css_docs if known is not None else []:
    for name in sorted(set(re.findall(r"--(?:ut|a|u)-[a-zA-Z0-9-]+", read(doc.relative_to(ROOT).as_posix())))):
        if name in PLACEHOLDERS:
            continue
        found = any(item.startswith(name) for item in known) if name.endswith("-") else name in known
        if not found:
            errors.append(f"{doc.relative_to(ROOT).as_posix()}: unknown CSS variable {name}")

for name in ("evals/evals.json", "evals/triggers.json"):
    try:
        if json.loads(read(name)) in (None, [], {}):
            errors.append(f"{name}: empty")
    except ValueError as exc:
        errors.append(f"{name}: {exc}")

for error in errors:
    print(error, file=sys.stderr)
if errors:
    sys.exit(1)
if known is None:
    print("skipped: CSS variable check (no --ut-vars)")
    print(f"ok: {len(docs)} references")
else:
    print(f"ok: {len(docs)} references, {len(known)} known variables")
