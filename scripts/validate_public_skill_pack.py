#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FORBIDDEN_PATHS = {
    "AGENTS.md",
    "CLAUDE.md",
    ".claude",
    ".codex",
}

FORBIDDEN_TEXT_PATTERNS = [
    re.compile(r"/Users/" + r"edwardhallam\b"),
    re.compile(r"\bobsidian/" + r"nexus\b", re.IGNORECASE),
    re.compile(r"\b" + r"nexus" + r" >\b", re.IGNORECASE),
    re.compile(r"\b1" + r"Password:\b"),
    re.compile(r"\bop" + r"://"),
    re.compile(r"\btail" + r"f[0-9a-z]*\b", re.IGNORECASE),
    re.compile(r"\bheart" + r"beat URL\b", re.IGNORECASE),
    re.compile(r"\b(?:co" + r"ve|launch|ubuntu-mini)\.tail", re.IGNORECASE),
]

TEXT_SUFFIXES = {
    ".json",
    ".md",
    ".py",
    ".sh",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def iter_files() -> list[Path]:
    ignored_dirs = {".git", ".ruff_cache", ".pytest_cache", "__pycache__"}
    files: list[Path] = []
    for current_root, dirs, names in os.walk(ROOT):
        dirs[:] = [name for name in dirs if name not in ignored_dirs]
        for name in names:
            files.append(Path(current_root) / name)
    return files


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_forbidden_paths(files: list[Path]) -> None:
    for path in files:
        rel = path.relative_to(ROOT)
        parts = rel.parts
        if rel.as_posix() in FORBIDDEN_PATHS:
            fail(f"forbidden public file present: {rel}")
        if any(part in {".claude", ".codex"} for part in parts):
            fail(f"forbidden public directory present: {rel}")
        if path.name in {"AGENTS.md", "CLAUDE.md"}:
            fail(f"forbidden public agent instruction file present: {rel}")


def check_text_hygiene(files: list[Path]) -> None:
    for path in files:
        if path.suffix not in TEXT_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        text = read_text(path)
        for pattern in FORBIDDEN_TEXT_PATTERNS:
            match = pattern.search(text)
            if match:
                fail(f"forbidden public text {match.group(0)!r} in {rel}")


def check_skill_metadata() -> None:
    skills_dir = ROOT / "skills"
    if not skills_dir.is_dir():
        fail("missing skills directory")

    skill_dirs = sorted(path for path in skills_dir.iterdir() if path.is_dir())
    if not skill_dirs:
        fail("no skills found")

    for skill_dir in skill_dirs:
        readme = skill_dir / "README.md"
        latest = skill_dir / "latest"
        skill_file = latest / "SKILL.md"
        if not readme.is_file():
            fail(f"{skill_dir.relative_to(ROOT)} is missing README.md")
        if not skill_file.is_file():
            fail(f"{skill_dir.relative_to(ROOT)} is missing latest/SKILL.md")

        text = read_text(skill_file)
        if not text.startswith("---\n"):
            fail(f"{skill_file.relative_to(ROOT)} is missing YAML frontmatter")
        frontmatter_end = text.find("\n---\n", 4)
        if frontmatter_end == -1:
            fail(f"{skill_file.relative_to(ROOT)} has unterminated frontmatter")
        frontmatter = text[4:frontmatter_end]
        if not re.search(r"^name:\s*\S+", frontmatter, re.MULTILINE):
            fail(f"{skill_file.relative_to(ROOT)} frontmatter missing name")
        if not re.search(r"^description:\s*.+", frontmatter, re.MULTILINE):
            fail(f"{skill_file.relative_to(ROOT)} frontmatter missing description")


def check_markdown_links(files: list[Path]) -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in files:
        if path.suffix != ".md":
            continue
        rel = path.relative_to(ROOT)
        text = read_text(path)
        for match in link_pattern.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target):
                continue
            candidate = (path.parent / target).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                fail(f"{rel} links outside repo: {target}")
            if not candidate.exists():
                fail(f"{rel} has missing local link: {target}")


def check_release_archives() -> None:
    for archive in sorted((ROOT / "skills").glob("*/releases/*.zip")):
        with zipfile.ZipFile(archive) as zf:
            for info in zf.infolist():
                if info.is_dir():
                    continue
                name = info.filename
                if Path(name).name in {"AGENTS.md", "CLAUDE.md"}:
                    fail(f"{archive.relative_to(ROOT)} contains forbidden file {name}")
                if ".claude/" in name or ".codex/" in name:
                    fail(f"{archive.relative_to(ROOT)} contains forbidden directory entry {name}")
                if Path(name).suffix not in TEXT_SUFFIXES:
                    continue
                text = zf.read(info).decode("utf-8")
                for pattern in FORBIDDEN_TEXT_PATTERNS:
                    match = pattern.search(text)
                    if match:
                        fail(
                            f"{archive.relative_to(ROOT)} contains forbidden text "
                            f"{match.group(0)!r} in {name}"
                        )


def main() -> None:
    files = iter_files()
    check_forbidden_paths(files)
    check_text_hygiene(files)
    check_skill_metadata()
    check_markdown_links(files)
    check_release_archives()
    print("public skill-pack validation passed")


if __name__ == "__main__":
    main()
