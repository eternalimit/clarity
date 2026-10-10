#!/usr/bin/env python3
"""Reproducible, key-free Git signing I/O regression test for REIK Epoch 380008.

Uses only Python standard library, Git, and Bash; replaces gpg with an instrumented
mock. Deliberately fails every attempted signed commit. Never contacts GitHub,
uses an actual private key, or produces a real signature.

Run: python3 test_fd3_mock_signing.py
"""
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

PASSPHRASE = "SYNTHETIC_PASS_PHRASE_FOR_FD3_ONLY"
MESSAGE = "epoch380008 synthetic message for Git signing"

MOCK_GPG = r'''#!/usr/bin/env python3
import json, os, pathlib, sys
arguments = sys.argv[1:]
data = sys.stdin.buffer.read()
fd3 = b""
if "--passphrase-fd" in arguments and arguments[arguments.index("--passphrase-fd")+1] == "3":
    while True:
        part = os.read(3, 4096)
        if not part:
            break
        fd3 += part
record = {
    "argv": arguments,
    "stdin_hex": data.hex(),
    "fd3_hex": fd3.hex(),
    "passphrase_environment_inherited": "SIGNING_PASSPHRASE" in os.environ,
}
pathlib.Path(os.environ["REIK_MOCK_REPORT"]).write_text(json.dumps(record, sort_keys=True), encoding="utf-8")
sys.exit(1) # no signature possible
'''

OLD_WRAPPER = r'''#!/bin/bash
set -euo pipefail
printf '%s\n' "$SIGNING_PASSPHRASE" | gpg --batch --pinentry-mode loopback --passphrase-fd 0 "$@"
'''

REFERENCE_WRAPPER = r'''#!/bin/bash
set -euo pipefail
exec gpg "$@"
'''

REVIEW_WRAPPER = r'''#!/bin/bash
set -euo pipefail
[[ -n "${SIGNING_PASSPHRASE:-}" ]]
exec 3<<<"$SIGNING_PASSPHRASE"
unset SIGNING_PASSPHRASE
exec gpg --batch --pinentry-mode loopback --passphrase-fd 3 "$@"
'''


def run(args, cwd, env=None):
    return subprocess.run(args, cwd=cwd, env=env, text=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, check=False, timeout=15)


def main():
    for cmd in ("git", "bash"):
        if not shutil.which(cmd):
            raise SystemExit(f"Missing local requirement: {cmd}")
    results = []
    def test(name, condition):
        results.append({"assertion": name, "passed": bool(condition)})

    with tempfile.TemporaryDirectory(prefix="reik-epoch380008-fd3-") as td:
        root = Path(td)
        gitdir = root / "isolated-repository"
        gitdir.mkdir()
        bindir = root / "bin"
        bindir.mkdir()
        mock = bindir / "gpg"
        mock.write_text(MOCK_GPG, encoding="utf-8")
        mock.chmod(0o700)
        old = root / "old_wrapper.sh"
        new = root / "review_only_fd3_wrapper.sh"
        reference = root / "reference_passthrough_wrapper.sh"
        for path, content in ((old, OLD_WRAPPER), (new, REVIEW_WRAPPER), (reference, REFERENCE_WRAPPER)):
            path.write_text(content, encoding="utf-8")
            path.chmod(0o700)
            syntax = run(["bash", "-n", str(path)], root)
            test("shell syntax: " + path.name, syntax.returncode == 0)

        init = run(["git", "init", "-q"], gitdir)
        assert init.returncode == 0, init.stderr
        for key, value in (("user.name", "Synthetic Tester"), ("user.email", "synthetic@example.invalid"),
                           ("commit.gpgsign", "false")):
            assert run(["git", "config", key, value], gitdir).returncode == 0
        seed = run(["git", "commit", "--allow-empty", "-qm", "unsigned seed"], gitdir)
        assert seed.returncode == 0, seed.stderr
        starting_head = run(["git", "rev-parse", "HEAD"], gitdir).stdout.strip()

        base_env = dict(os.environ)
        base_env["PATH"] = str(bindir) + os.pathsep + os.environ.get("PATH", "")
        base_env["SIGNING_PASSPHRASE"] = PASSPHRASE
        base_env["GIT_AUTHOR_DATE"] = "2000-01-01T00:00:00+0000"
        base_env["GIT_COMMITTER_DATE"] = "2000-01-01T00:00:00+0000"
        reports = {}
        outputs = {}
        for tag, wrapper in (("old", old), ("fd3", new), ("reference", reference)):
            report_path = root / (tag + ".json")
            env = {**base_env, "REIK_MOCK_REPORT": str(report_path)}
            result = run(["git", "-c", f"gpg.program={wrapper}", "commit", "-S", "--allow-empty", "-m", MESSAGE], gitdir, env)
            outputs[tag] = result
            assert report_path.exists(), f"Mock wasn't called for {tag}: {result.stderr}"
            reports[tag] = json.loads(report_path.read_text(encoding="utf-8"))

        orig = reports["old"]
        revised = reports["fd3"]
        baseline = reports["reference"]
        orig_stdin = bytes.fromhex(orig["stdin_hex"])
        revised_stdin = bytes.fromhex(revised["stdin_hex"])
        revised_fd3 = bytes.fromhex(revised["fd3_hex"])
        baseline_stdin = bytes.fromhex(baseline["stdin_hex"])
        expected_passphrase = (PASSPHRASE + "\n").encode("utf-8")

        test("regression reproduced: old FD0 is passphrase", orig_stdin == expected_passphrase)
        test("regression reproduced: old FD0 loses Git commit payload", MESSAGE.encode() not in orig_stdin)
        test("repair: FD0 contains original Git message", MESSAGE.encode() in revised_stdin)
        test("repair: FD0 includes Git commit object header fields", b"tree " in revised_stdin and b"author " in revised_stdin)
        test("repair: FD0 is byte-identical to direct Git-to-GPG baseline", revised_stdin == baseline_stdin)
        test("repair: FD3 carries synthetic passphrase only", revised_fd3 == expected_passphrase)
        test("repair: FD0 excludes synthetic passphrase", PASSPHRASE.encode() not in revised_stdin)
        test("repair: passphrase is not a command-line argument", all(PASSPHRASE not in x for x in revised["argv"]))
        test("repair: passphrase env removed from mock-GPG child", not revised["passphrase_environment_inherited"])
        test("repair: mock received FD3 selection", "--passphrase-fd" in revised["argv"] and revised["argv"][revised["argv"].index("--passphrase-fd")+1] == "3")
        test("all mock executions intentionally fail signing", all(x.returncode != 0 for x in outputs.values()))
        test("no new Git commit created", run(["git", "rev-parse", "HEAD"], gitdir).stdout.strip() == starting_head)
        test("local test repository has no Git remotes", not run(["git", "remote"], gitdir).stdout.strip())

        missing_path = root / "no_passphrase_mock.json"
        empty_env = {**base_env, "SIGNING_PASSPHRASE": "", "REIK_MOCK_REPORT": str(missing_path)}
        empty = run(["git", "-c", f"gpg.program={new}", "commit", "-S", "--allow-empty", "-m", MESSAGE], gitdir, empty_env)
        test("empty passphrase blocked before mock program executes", empty.returncode != 0 and not missing_path.exists())
        test("empty-passphrase failure does not alter HEAD", run(["git", "rev-parse", "HEAD"], gitdir).stdout.strip() == starting_head)

        detail = {
            "schema": "REIK-EPOCH380008-FD3-MOCK-TEST-v2",
            "test_kind": "isolated synthetic Git-to-mock-GPG interface; NO real signatures",
            "git_version": run(["git", "--version"], root).stdout.strip(),
            "bash_version": run(["bash", "--version"], root).stdout.splitlines()[0],
            "old_stdin_sha256": hashlib.sha256(orig_stdin).hexdigest(),
            "reference_stdin_sha256": hashlib.sha256(baseline_stdin).hexdigest(),
            "fd3_repaired_stdin_sha256": hashlib.sha256(revised_stdin).hexdigest(),
            "fd3_channel_sha256": hashlib.sha256(revised_fd3).hexdigest(),
            "assertions": results,
            "passed_count": sum(x["passed"] for x in results),
            "total_count": len(results),
            "state": "0 HOLD",
        }
    print(json.dumps(detail, indent=2, sort_keys=True))
    return 0 if all(a["passed"] for a in results) else 1


if __name__ == "__main__":
    sys.exit(main())
