#!/usr/bin/env python3
"""Local-only structural checks for the fixed 64-week course."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
PHASE_WEEKS = {
    "P0": range(1, 3),
    "P1": range(3, 10),
    "P2": range(10, 20),
    "P3": range(20, 32),
    "P4": range(32, 42),
    "P5": range(42, 50),
    "P6": range(50, 57),
    "P7": range(57, 65),
}
LESSON_FILES = {"README.md", "notes.md", "resources.md", "quiz.md", "record.md"}
REQUIRED_HEADINGS = (
    "## 本课目的",
    "## 固定 Scope",
    "## 掌握目标",
    "## 高级工程师面试覆盖",
    "## 与既有经验的连接",
    "## 知识型学习产出",
)
REQUIRED_DOMAINS = ("数据库内核", "存储引擎", "计算引擎", "分布式系统", "可观测性")
FORBIDDEN_PATH_PARTS = (
    ".github/workflows",
    ".circleci",
    ".buildkite",
    "docs/spec",
)
FORBIDDEN_FILENAMES = {
    ".gitlab-ci.yml",
    "jenkinsfile",
    "azure-pipelines.yml",
    "azure-pipelines.yaml",
    "cloudbuild.yaml",
    "cloudbuild.yml",
    "bitrise.yml",
    "woodpecker.yml",
    "woodpecker.yaml",
}
PROCESS_FILENAME_RE = re.compile(
    r"(^|[-_.])(prd|adr|rfc|spec|implementation[-_ ]?plan|tasks?|context[-_ ]?dump|handoff)([-_.]|$)",
    re.IGNORECASE,
)
LAB_PATH_RE = re.compile(r"(^|[-_.])(lab|labs|laboratory)([-_.]|$)", re.IGNORECASE)
FORBIDDEN_TEXT = (
    "docs/spec/",
    "GPU Kernel Laboratory",
    "Agent 工程实验",
    "learning-log.md",
    "scripts/sync_course.py",
    "scripts/validate_course.py",
)
LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
RESOURCE_LINE_RE = re.compile(
    r"^- \[(?P<title>[^]]+)\]\((?P<url>[^)]+)\) — "
    r"\*\*选入理由\*\*：(?P<reason>[^；]+)；"
    r"\*\*支撑 Scope\*\*：(?P<scope>[^；]+)；"
    r"\*\*阅读深度\*\*：(?P<depth>.+)$"
)
GENERIC_REASON_RE = re.compile(
    r"^(?:[A-Za-z0-9+.-]+\s*)?(?:官方|正式会议|经典|原始|NeurIPS|ICML|OSDI|MLSys|CACM)"
    r"(?:文档|规范|规则|教程|论文|仓库|源码|设计文档|内部文档|API|参考实现)?$",
    re.IGNORECASE,
)
GENERIC_REASON_PHRASES = (
    "对象模型、接口和失败边界",
    "以机制、推导、实验和限制条件",
    "完整机制、对照实验和限制条件",
    "提供规范性语义和可比口径",
    "规范性语义基线",
    "落到版本化的数据结构",
    "用连续解释或示例串起",
    "能同时训练原理推理、证据审查与适用边界判断",
    "能同时训练原理推导、实验审查与适用边界判断",
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def extract_scope_items(readme: str) -> list[str]:
    if "## 固定 Scope\n" not in readme or "\n## 掌握目标" not in readme:
        return []
    scope_section = readme.split("## 固定 Scope\n", 1)[1].split("\n## 掌握目标", 1)[0]
    return [line[2:].strip() for line in scope_section.splitlines() if line.startswith("- ")]


def github_repo(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.hostname != "github.com":
        return None
    parts = [part for part in parsed.path.removesuffix(".git").split("/") if part]
    if len(parts) < 2:
        return None
    return f"https://github.com/{parts[0]}/{parts[1]}".lower()


def check_lessons(errors: list[str]) -> None:
    seen: list[int] = []
    connection_sections: dict[str, str] = {}
    interview_sections: dict[str, str] = {}
    quiz_bodies: dict[str, str] = {}
    for phase, weeks in PHASE_WEEKS.items():
        phase_dir = ROOT / "course" / phase
        if not phase_dir.is_dir():
            fail(errors, f"missing phase directory: {phase_dir.relative_to(ROOT)}")
            continue

        actual_dirs = {path.name for path in phase_dir.glob("W??") if path.is_dir()}
        expected_dirs = {f"W{week:02d}" for week in weeks}
        if actual_dirs != expected_dirs:
            fail(errors, f"{phase} weeks differ: expected {sorted(expected_dirs)}, got {sorted(actual_dirs)}")

        for week in weeks:
            seen.append(week)
            lesson = phase_dir / f"W{week:02d}"
            actual_files = {path.name for path in lesson.iterdir() if path.is_file()} if lesson.is_dir() else set()
            if actual_files != LESSON_FILES:
                fail(errors, f"{lesson.relative_to(ROOT)} files differ: {sorted(actual_files)}")
                continue

            readme = (lesson / "README.md").read_text(encoding="utf-8")
            for heading in REQUIRED_HEADINGS:
                if heading not in readme:
                    fail(errors, f"{lesson.relative_to(ROOT)}/README.md missing {heading}")
            for domain in REQUIRED_DOMAINS:
                if f"**{domain}**" not in readme:
                    fail(errors, f"{lesson.relative_to(ROOT)}/README.md missing domain connection: {domain}")
            scope_items = extract_scope_items(readme)
            if not scope_items:
                fail(errors, f"{lesson.relative_to(ROOT)}/README.md has no concrete Scope list")

            def section(name: str, next_name: str) -> str:
                return readme.split(f"## {name}\n", 1)[1].split(f"\n## {next_name}", 1)[0].strip()

            key = lesson.relative_to(ROOT).as_posix()
            interview_sections[key] = section("高级工程师面试覆盖", "与既有经验的连接")
            connection_sections[key] = section("与既有经验的连接", "知识型学习产出")

            quiz = (lesson / "quiz.md").read_text(encoding="utf-8")
            quiz_body = quiz.split("## 答题与订正", 1)[0]
            quiz_body = re.sub(r"^# .+$", "", quiz_body, flags=re.MULTILINE).strip()
            quiz_bodies[key] = quiz_body
            questions = re.findall(r"^\d+\. ", quiz_body, re.MULTILINE)
            if len(questions) < 4:
                fail(errors, f"{lesson.relative_to(ROOT)}/quiz.md needs at least four lesson-specific questions")

            resources = (lesson / "resources.md").read_text(encoding="utf-8")
            resource_links = LINK_RE.findall(resources)
            if not resource_links:
                fail(errors, f"{lesson.relative_to(ROOT)}/resources.md has no fixed source")
            for marker in ("**选入理由**", "**支撑 Scope**", "**阅读深度**"):
                if resources.count(marker) != len(resource_links):
                    fail(errors, f"{lesson.relative_to(ROOT)}/resources.md lacks per-source marker: {marker}")
            if "资料状态核验：2026-10-22" not in resources:
                fail(errors, f"{lesson.relative_to(ROOT)}/resources.md lacks verification date")

            entries = [
                match.groupdict()
                for line in resources.splitlines()
                if (match := RESOURCE_LINE_RE.match(line))
            ]
            if len(entries) != len(resource_links):
                fail(errors, f"{lesson.relative_to(ROOT)}/resources.md has malformed source entries")
            for entry in entries:
                reason = entry["reason"].strip()
                if (
                    len(reason) < 24
                    or GENERIC_REASON_RE.fullmatch(reason)
                    or any(phrase in reason for phrase in GENERIC_REASON_PHRASES)
                ):
                    fail(
                        errors,
                        f"{lesson.relative_to(ROOT)}/resources.md has non-specific reason: {entry['title']}",
                    )
                if len(entry["scope"].strip()) < 2:
                    fail(
                        errors,
                        f"{lesson.relative_to(ROOT)}/resources.md has empty Scope mapping: {entry['title']}",
                    )
                if len(entry["depth"].strip()) < 18:
                    fail(
                        errors,
                        f"{lesson.relative_to(ROOT)}/resources.md has shallow reading guidance: {entry['title']}",
                    )

    if seen != list(range(1, 65)):
        fail(errors, "weeks are not exactly W01-W64 in order")

    for label, sections in (
        ("interview coverage", interview_sections),
        ("domain connections", connection_sections),
        ("quiz body", quiz_bodies),
    ):
        reverse: dict[str, list[str]] = {}
        for path, content in sections.items():
            reverse.setdefault(content, []).append(path)
        duplicates = [paths for paths in reverse.values() if len(paths) > 1]
        for paths in duplicates:
            fail(errors, f"duplicated {label}: {', '.join(paths)}")


def check_links(errors: list[str]) -> None:
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or re.match(r"^[a-z][a-z0-9+.-]*://", target, re.IGNORECASE):
                continue
            local = (markdown.parent / target).resolve()
            if not local.exists():
                fail(errors, f"broken link in {markdown.relative_to(ROOT)}: {raw_target}")


def check_references(errors: list[str]) -> None:
    refs = (ROOT / "references/projects.yaml").read_text(encoding="utf-8")
    revisions = re.findall(r"^\s+ref: ([0-9a-f]{40})$", refs, re.MULTILINE)
    if not revisions or len(set(revisions)) != len(revisions):
        fail(errors, f"Git revisions must be present and unique, got {len(revisions)}")

    registered: dict[str, str] = {}
    for block in re.split(r"\n  - name: ", refs)[1:]:
        url_match = re.search(r"^.*?\n    url: (https://github\.com/\S+)$", block, re.MULTILINE)
        ref_match = re.search(r"^    ref: ([0-9a-f]{40})$", block, re.MULTILINE)
        if not url_match or not ref_match:
            fail(errors, "projects.yaml has a malformed project entry")
            continue
        repo = github_repo(url_match.group(1))
        if not repo:
            fail(errors, f"projects.yaml has a non-GitHub project URL: {url_match.group(1)}")
            continue
        if repo in registered:
            fail(errors, f"projects.yaml repeats project: {repo}")
        registered[repo] = ref_match.group(1)

    used: dict[str, list[tuple[str, str]]] = {}
    for resource_file in (ROOT / "course").glob("P[0-7]/W??/resources.md"):
        for url in LINK_RE.findall(resource_file.read_text(encoding="utf-8")):
            if repo := github_repo(url):
                used.setdefault(repo, []).append((resource_file.relative_to(ROOT).as_posix(), url))
    for missing in sorted(set(used) - set(registered)):
        fail(errors, f"GitHub course source lacks pinned revision: {missing}")
    for repo, locations in sorted(used.items()):
        ref = registered.get(repo)
        if not ref:
            continue
        for path, url in locations:
            if not re.search(rf"/(?:blob|tree)/{re.escape(ref)}(?:/|$)", url):
                fail(errors, f"floating GitHub source in {path}: {url}")


def check_forbidden_artifacts(errors: list[str]) -> None:
    paths = [path for path in ROOT.rglob("*") if ".git" not in path.parts]
    for path in paths:
        rel = path.relative_to(ROOT).as_posix()
        if any(part in rel for part in FORBIDDEN_PATH_PARTS):
            fail(errors, f"forbidden path exists: {rel}")
        if path.is_file() and path.name.lower() in FORBIDDEN_FILENAMES:
            fail(errors, f"CI/CD configuration exists: {rel}")
        if path.is_file() and PROCESS_FILENAME_RE.search(path.name):
            fail(errors, f"process-design filename exists: {rel}")
        if LAB_PATH_RE.search(rel):
            fail(errors, f"manual-lab artifact exists: {rel}")

    scripts = {
        path.relative_to(ROOT / "scripts").as_posix()
        for path in (ROOT / "scripts").rglob("*")
        if path.is_file()
    }
    if scripts != {"check_course.py"}:
        fail(errors, f"scripts directory must contain only check_course.py, got {sorted(scripts)}")

    for path in paths:
        if not path.is_file() or path.suffix not in {".md", ".py", ".yaml", ".yml"}:
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        text = path.read_text(encoding="utf-8")
        for phrase in FORBIDDEN_TEXT:
            if phrase in text:
                fail(errors, f"forbidden legacy text in {path.relative_to(ROOT)}: {phrase}")


def check_remote_links(errors: list[str]) -> tuple[int, list[str]]:
    urls = {
        url
        for resource_file in (ROOT / "course").glob("P[0-7]/W??/resources.md")
        for url in LINK_RE.findall(resource_file.read_text(encoding="utf-8"))
        if url.startswith(("http://", "https://"))
    }
    refs = (ROOT / "references/projects.yaml").read_text(encoding="utf-8")
    for block in re.split(r"\n  - name: ", refs)[1:]:
        url_match = re.search(r"^.*?\n    url: (https://github\.com/\S+)$", block, re.MULTILINE)
        ref_match = re.search(r"^    ref: ([0-9a-f]{40})$", block, re.MULTILINE)
        if url_match and ref_match:
            base = url_match.group(1).removesuffix(".git")
            urls.add(f"{base}/commit/{ref_match.group(1)}")
    urls = sorted(urls)

    def probe(url: str) -> tuple[str, int | None, str | None]:
        request = Request(
            url,
            headers={
                "User-Agent": "tier1-study-link-check/1.0",
                "Range": "bytes=0-0",
                "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.1",
            },
        )
        try:
            with urlopen(request, timeout=15) as response:
                response.read(1)
                return url, response.status, None
        except HTTPError as exc:
            return url, exc.code, None
        except (URLError, TimeoutError, OSError) as exc:
            return url, None, str(exc)

    warnings: list[str] = []
    with ThreadPoolExecutor(max_workers=16) as executor:
        futures = [executor.submit(probe, url) for url in urls]
        for future in as_completed(futures):
            url, status, problem = future.result()
            if status in {404, 410}:
                fail(errors, f"remote source is unavailable ({status}): {url}")
            elif status is None:
                warnings.append(f"remote source could not be verified: {url} ({problem})")
            elif status >= 400 and status not in {401, 403, 405, 429}:
                warnings.append(f"remote source returned {status}: {url}")
    return len(urls), warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-remote",
        action="store_true",
        help="probe fixed course URLs; definitive 404/410 responses fail, access-control/network errors are warnings",
    )
    args = parser.parse_args()
    errors: list[str] = []
    if extract_scope_items("## 固定 Scope\n\nNo bullets\n\n## 掌握目标\n\n- unrelated"):
        fail(errors, "internal negative check failed: Scope parser crossed a section boundary")
    check_lessons(errors)
    check_links(errors)
    check_references(errors)
    check_forbidden_artifacts(errors)
    remote_count = 0
    warnings: list[str] = []
    if args.check_remote:
        remote_count, warnings = check_remote_links(errors)

    if errors:
        print("course check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    revisions = re.findall(
        r"^\s+ref: ([0-9a-f]{40})$",
        (ROOT / "references/projects.yaml").read_text(encoding="utf-8"),
        re.MULTILINE,
    )
    print(
        f"course check passed: 8 phases, 64 fixed-scope lessons, "
        f"specific source mappings and {len(revisions)} pinned Git revisions"
    )
    if args.check_remote:
        print(f"remote link check: {remote_count} unique URLs probed, no definitive 404/410")
        for warning in warnings:
            print(f"warning: {warning}")
    else:
        print("remote links were not probed; use --check-remote for live 404/410 verification")
    return 0


if __name__ == "__main__":
    sys.exit(main())
