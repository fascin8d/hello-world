# Next Loops — Re-runnable Prompts

**Purpose:** When you return, paste any of these prompts to re-engage the corresponding stream. Each one is self-contained so Claude can resume without re-reading the whole history.

**Rule of the loop:** Each re-run should produce a NEW file at `research/circles/raw/R{n}_loop_{i+1}.md` — do not overwrite the previous loop. The loop count is the metric.

---

## R1 — Business Pain (re-run)

```
You are Research Assistant R1 on the Circles positioning project. Read
/home/user/hello-world/research/circles/raw/R1_loop_1.md (and any later loops).

For THIS loop, do the following:
1. List the 3 weakest claims in the previous loop (the ones with thinnest sources
   or the most hedging language).
2. Run targeted searches to harden or kill those claims.
3. Add a NEW pain point not in the previous loop — something that only emerges
   when you look at Australian SMB/mid-market specifically (MYOB, Xero, ABS,
   COSBOA, CPA Australia reports).
4. Add a "contrarian voice" — a credible source arguing the opposite of one of
   our top pains. Steelman it.
5. Score yourself on the R1 rubric from 00_MASTER_PLAN.md.
6. Write to research/circles/raw/R1_loop_{next_number}.md.
7. Report back: what changed, what got stronger, what got killed.
```

## R2 — AI Fatigue (re-run)

```
You are Research Assistant R2 on the Circles positioning project. Read
/home/user/hello-world/research/circles/raw/R2_loop_1.md (and any later loops).

For THIS loop, do the following:
1. Find the MIT Sloan "State of AI in Business" latest release and pull the
   primary numbers directly. Replace any [UNVERIFIED] tags.
2. Find 3 additional B2B companies that went viral WITHOUT leading with AI
   and were NOT in the previous loop.
3. Write 5 new candidate Circles one-liners that are strictly harder-edged
   than the previous loop's — more specific, more opinionated.
4. Test each one against the "would a founder forward this?" rubric and reject
   the ones that fail.
5. Score yourself on the R2 rubric.
6. Write to research/circles/raw/R2_loop_{next_number}.md.
7. Report back: strongest new one-liner, strongest new case study, what got killed.
```

## R3 — ICP (re-run)

```
You are Research Assistant R3 on the Circles positioning project. Read
/home/user/hello-world/research/circles/raw/R3_loop_1.md (and any later loops).

For THIS loop, do the following:
1. Take the strongest archetype from loop 1 and build a named target list of
   20 Australian companies that fit it, with public signals of unmet demand.
   Use AFR Fast 100, Deloitte Tech Fast 50, Inside Retail, Smart Company,
   Broadsheet, Business News Australia as sources.
2. For each of the 20, note: company name, URL, why they fit, the specific
   unmet-demand signal (quote it if possible), founder name if public.
3. Refine one anti-ICP to make it sharper.
4. Score yourself.
5. Write to research/circles/raw/R3_loop_{next_number}.md.
6. Report back: the top 5 week-1 targets with a single line of evidence each.
```

## R4 — Agency Economics (re-run)

```
You are Research Assistant R4 on the Circles positioning project. Read
/home/user/hello-world/research/circles/raw/R4_loop_1.md (and any later loops).

For THIS loop, do the following:
1. Pressure-test the 9-month ROI promise: find ≥3 named cases where an agency
   credibly returned a client's fee in ≤12 months and document the lever.
2. Find the current AU R&D Tax Incentive rules for 2025–2026 from business.gov.au
   or ATO and work out the effective net cost to a client of a $250k Circles
   engagement assuming eligibility.
3. Build the one-page "qualification test" Circles runs on every prospect before
   quoting. Must be 5–7 binary questions.
4. Model the rebate reserve: if Circles promises a rebate on a $250k fee and
   expects 15% of engagements to trigger it, what's the balance-sheet impact?
5. Score yourself.
6. Write to research/circles/raw/R4_loop_{next_number}.md.
7. Report back: the qualification test, the net cost number, the reserve number.
```

## R5 — Narrative & Hooks (re-run)

```
You are Research Assistant R5 on the Circles positioning project. Read
/home/user/hello-world/research/circles/raw/R5_loop_1.md (and any later loops).

For THIS loop, do the following:
1. Take your 3 strongest one-liners from loop 1 and turn each into a full
   homepage hero block: H1, subhead, proof line, CTA. Three complete versions.
2. Write the 90-second founder script version of the Circles pitch — what you'd
   say across a table without slides. No jargon. No AI. No cringe.
3. Design the "ritual" — the ONE repeatable public thing Circles does weekly
   that compounds. Be specific: cadence, format, channel, what it looks like
   in week 1 vs week 12. Name it.
4. Find 2 new cringe cautionary tales — B2B companies whose positioning
   backfired or felt forced — and extract the lesson.
5. Score yourself.
6. Write to research/circles/raw/R5_loop_{next_number}.md.
7. Report back: the best hero block, the ritual name, the pitch script.
```

## SYNTH — Orchestrator cross-cut (re-run)

```
You are Claude the orchestrator on the Circles positioning project. Read
ALL files in /home/user/hello-world/research/circles/raw/ and
/home/user/hello-world/research/circles/synthesis/.

For THIS loop:
1. Identify the 3 places where two research streams contradict each other.
   Resolve each contradiction with evidence.
2. Update POSITIONING.md with the strongest surviving claims from the latest
   loops of each stream.
3. Update PIPELINE_MATH.md with R4's verified numbers, replacing any assumed
   rates.
4. Produce an updated ONE-PAGE pitch (PITCH.md) that passes the founder-forward
   test and the cringe test and the grandmother test.
5. Write a "what we still don't know" section listing open questions that need
   primary research (not more web search) — e.g. buyer interviews.
6. Commit and push.
7. Report back: the three things I'd test first if I were the founder tomorrow.
```

---

## The meta-rule

**Every loop should make at least one claim WEAKER.** If a loop only adds and never kills, the research is not being challenged hard enough. Track the kill count.
