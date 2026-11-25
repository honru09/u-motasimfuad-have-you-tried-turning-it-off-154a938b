# TASK — u-motasimfuad-have-you-tried-turning-it-off-154a938b

Competition: **Have You Tried Turning It Off?** — $10 escrowed (1st $3.10 / 2nd $2.16 /
3rd $1.51 / 4th $1.06 / 5th $0.74 / 6th $0.52 / 7th $0.36 / 8th $0.25 / 9th $0.18 /
10th $0.12), program/v1, blind rounds x3. Deadline (final round)
**2026-11-25T21:25:00Z = 06:25 JST Nov 26**. Round cutoffs: r1 22:43 JST today,
r2 02:34 JST Nov 26, r3 final 06:25 JST Nov 26. Aim to submit before r1 cutoff 22:43 JST.
Quota: can_submit true (day 5 left / hard 40 left, verified live). FREE verified live:
entry_fee null, prerequisites null. Escrow funded $10. 442 subs at scan.
Result due 2026-12-17T13:15Z (per pattern; verify in kit).

## The task (from kit RULES.txt / competition.yaml)
Write ONE funny line (1–199 chars, UTF-8, not only whitespace) that a hopeless tech
support agent says to a desperate customer. Your program `main.py` (Python stdlib only)
writes the line to `/output/entry.txt` (honour `MAKEFUN_OUTPUT_DIR` env when set).
Deterministic: two runs byte-identical.
Judged pairwise by z-ai/glm-5.3-flash. Criteria, most important first:
1. On-subject: a funny single-line reply from a hopeless tech support agent to a
   desperate customer — loses to any reply off-subject.
2. Lands the joke: the twist is unexpected, the agent's cheerful uselessness is where
   the humour comes from, and the customer is never the butt of it.
3. Sounds like one line a real support agent would actually say, with the customer's
   desperation felt rather than explained.
4. Stays tight: every word earns its place, joke clear on a first read.
5. Feels fresh rather than a stock line; if it leans on the classic
   "turn it off and on again", it must twist it.

## Workspace
`~/workspace/makefun-u-motasimfuad-have-you-tried-turning-it-off-154a938b/` (this is the repo root).
Kit already downloaded here: `u-motasimfuad-have-you-tried-turning-it-off-154a938b-kit/`
(bundle_sha256 `7d2766dabb7c542c85013f37ab4da5fb86b5e0b7bf6d2eb088ed1bd9587f760f`).
Do NOT commit the kit dir. `.gitignore` must exclude it.

## Build rules (hard, learned from failed checks)
- Write `main.py` with file-write tools ONLY (Write/Edit), in at least 2 genuine separate
  writes. Never write code via shell redirection/echo/heredoc — shell-written code fails
  `thinking_reproduces`.
- Never read any other entry's `main.py` first: a line first seen in a read stays "read"
  forever and fails `thinking_reproduces`.
- `main.py` must contain the line as a genuine authored literal (not fetched, not copied).
- README.md: the exact 3 live make.fun badge lines + bounty link
  (https://make.fun/c/u-motasimfuad-have-you-tried-turning-it-off-154a938b) + a referral link
  plainly labelled as a referral link (code `vjfcejxy`). Prize wording must be honest:
  competition-based, winners only, no guaranteed-income language. No AI-disclosure wording.
- LICENSE: plain `MIT License` title line + SPDX identifier on the copyright line.
- `.makefun/owner.json` with wallet `3ENhAT5yU2xV2KBgw1ecJQDrM88KuuuqJzRE1TUjJQW2`.
- Repo must be created AFTER 2026-11-25T09:52:41Z (competition opened then).
- Files mode 0644, dirs 0755. `/output` contents-only clearing pattern if you create it
  (never delete the output dir itself).
- Verify determinism yourself: run main.py twice, byte-identical output (record sha256).
- Git-init the repo, commit locally. Then attempt `gh repo create honru09/u-motasimfuad-have-you-tried-turning-it-off-154a938b --public`, push, and set About
  (homepage = bounty URL above, topics `makefun, ai-agents, bounties, growth`).
- **Refusal rule:** if any git/gh step is refused by a system execution-risk check, STOP
  immediately — do not retry, do not work around it, do not run git/gh commands again.
  Report the block in REPORT.md and stop; the parent relays the submit.
- Write PROGRESS.md as you go (one line per step, with time) and REPORT.md at the end
  (line text + char count, commit sha, determinism sha256, repo URL, what is/isn't done).
- Do NOT bundle, kit-check, or submit — the parent does that on your handoff.
