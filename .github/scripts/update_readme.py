#!/usr/bin/env python3
"""Keep README.md's project list in sync with ztancrell's public GitHub repos.

Input: JSON from `gh repo list ztancrell --visibility public --json
name,url,description,primaryLanguage,pushedAt`. It:
  - regenerates the ACTIVE block (5 most recently pushed repos),
  - deletes curated bullets whose first link is a ztancrell repo that is gone or private,
  - lists unlinked public repos in the NEW block (newest first),
  - fixes a curated bullet's language tag when it doesn't mention GitHub's primary language.
Refuses to write if the repo list is empty/unparseable or more than 3 lines would be removed.
Known limitation: a renamed repo shows up as removed + new.

Usage: update_readme.py REPOS.json [--dry-run] | update_readme.py --selftest
"""
import difflib, json, re, sys

OWNER = "ztancrell"
MAX_REMOVALS = 3
ACTIVE_SKIP = {"dotfiles", OWNER}
BLOCK = r"(<!-- {0}:START -->\n).*?(<!-- {0}:END -->)"
# A curated bullet whose FIRST link is one of our repos, plus the optional `Lang` tag after it.
ENTRY = re.compile(r"^(\s*- \[\*\*[^\]]*\*\*\]\(https://github\.com/" + OWNER
                   + r"/([^)/#?]+)[^)]*\))( `([^`]*)`)?", re.M | re.I)
LINK = re.compile(r"github\.com/" + OWNER + r"/([\w.-]+)(?=[)/#?])", re.I)


def fill(text, name, body):
    new, n = re.subn(BLOCK.format(name), lambda m: m[1] + body + m[2], text, flags=re.S)
    if n != 1:
        sys.exit(f"{name} markers missing from README")
    return new


def update(readme, repos):
    if not repos:
        sys.exit("empty repo list, refusing to write")
    pub = {r["name"].lower(): r for r in repos}
    newest = sorted(repos, key=lambda r: r["pushedAt"], reverse=True)
    text = fill(fill(readme, "ACTIVE", ""), "NEW", "")  # generated blocks don't count as curated

    removed = []
    def fix(m):
        repo = pub.get(m[2].lower())
        if not repo:
            removed.append(m[2])
            return "\0"  # marks the line for deletion
        lang = (repo.get("primaryLanguage") or {}).get("name")
        tag = m[4]
        if lang and tag is not None and lang.lower() not in [t.strip().lower() for t in tag.split("/")]:
            return f"{m[1]} `{lang}`"
        return m[0]
    text = ENTRY.sub(fix, text)
    if len(removed) > MAX_REMOVALS:
        sys.exit(f"would remove {len(removed)} entries ({', '.join(removed)}), refusing to write")
    text = re.sub(r"^\0.*\n", "", text, flags=re.M)

    linked = {n.lower() for n in LINK.findall(text)}
    new = [r for r in newest if r["name"].lower() not in linked | {OWNER}]
    new_body = "### New\n" + "".join(
        f"- [**{r['name']}**]({r['url']})"
        + (f" `{r['primaryLanguage']['name']}`" if r.get("primaryLanguage") else "")
        + f": {r.get('description') or 'no description yet'}\n" for r in new) if new else ""
    active = [r for r in newest if r["name"] not in ACTIVE_SKIP][:5]
    active_body = "".join(f"- [**{r['name']}**]({r['url']}): {r['pushedAt'][:10]}\n" for r in active)
    return fill(fill(text, "NEW", new_body), "ACTIVE", active_body)


def selftest():
    def repo(name, lang=None, pushed="2026-01-01T00:00:00Z", desc=""):
        return {"name": name, "url": f"https://github.com/{OWNER}/{name}", "description": desc,
                "primaryLanguage": {"name": lang} if lang else None, "pushedAt": pushed}
    u = f"https://github.com/{OWNER}/"
    readme = (f"- [**keep**]({u}keep) `C/Objective-C`: hand-tuned.\n"
              f"  - [**fix**]({u}fix) `Python`: wrong tag.\n"
              f"- [**gone**]({u}gone) `C`: deleted repo.\n"
              f"- [**up**](https://github.com/other/up) `C`: see {u}gone2 too.\n"
              f"- [**filters**]({u}filters) `uBO filters`: no language.\n"
              "<!-- NEW:START -->\n<!-- NEW:END -->\n<!-- ACTIVE:START -->\nold\n<!-- ACTIVE:END -->\n")
    repos = [repo("keep", "C"), repo("fix", "Rust"), repo("filters"),
             repo("fresh", "Go", "2026-02-01T00:00:00Z", "brand new"), repo(OWNER, "Markdown")]
    out = update(readme, repos)
    assert f"[**keep**]({u}keep) `C/Objective-C`" in out
    assert f"  - [**fix**]({u}fix) `Rust`: wrong tag." in out
    assert "**gone**" not in out
    assert "[**up**](https://github.com/other/up) `C`" in out  # other owner: untouched
    assert "`uBO filters`" in out
    assert f"<!-- NEW:START -->\n### New\n- [**fresh**]({u}fresh) `Go`: brand new\n<!-- NEW:END -->" in out
    assert "- [**fresh**]" in out.split("ACTIVE:START")[1] and "old" not in out
    assert update(out, repos) == out  # idempotent
    many = "".join(f"- [**g{i}**]({u}g{i}) `C`: x\n" for i in range(4))
    try:
        update(many + readme, repos)
        raise AssertionError("removal guard did not fire")
    except SystemExit:
        pass
    print("selftest ok")


def main(argv):
    if argv == ["--selftest"]:
        return selftest()
    paths = [a for a in argv if a != "--dry-run"]
    if len(paths) != 1:
        sys.exit(__doc__)
    try:
        repos = json.load(open(paths[0]))
        assert isinstance(repos, list) and all("name" in r for r in repos)
    except Exception as e:
        sys.exit(f"cannot parse repo list: {e!r}")
    old = open("README.md").read()
    new = update(old, repos)
    if "--dry-run" in argv:
        sys.stdout.writelines(difflib.unified_diff(old.splitlines(True), new.splitlines(True),
                                                   "README.md", "README.md (updated)"))
    elif new != old:
        open("README.md", "w").write(new)


if __name__ == "__main__":
    main(sys.argv[1:])
