# Circles — Research & Positioning Master Plan

**Client:** Circles (tech agency)
**Mission:** Liberate growth for companies that do things differently and have unmet demand.
**North-star goal:** 30 projects × $250k AUD over 9 months (≈ $7.5M AUD pipeline) where each project returns its own fee within 9 months.
**Date:** 2026-04-09
**Orchestrator:** Claude (Opus 4.6)
**Branch:** `claude/research-growth-positioning-P3n1V`

---

## 1. The brief, distilled

1. **People have AI fatigue** — any positioning that leads with "AI" as the headline loses. Lead with outcomes, craft, and liberation.
2. **We serve the differentiated minority** — founders and operators who deliberately do it differently and, as a result, have demand they cannot yet meet.
3. **Our job is amplification, not reinvention** — we leverage what they already do well and give it reach. Team first, tech second.
4. **Every output must be grounded** — evidence-backed, evaluable, and rewritable. No vibes-only claims.
5. **Virality is a side-effect of truth told well** — we don't optimise for virality directly; we optimise for clarity and resonance, which spread.

## 2. The five research focus areas (one per assistant)

Each assistant owns a dimension. Each dimension has its own eval rubric. Findings must survive the rubric or be rewritten.

### R1 — Business Pain & Growth Blockers (2025–2026)
**Question:** What are the *actual* top problems businesses face in 2025–2026, ranked by frequency and severity, with named sources?
**Deliverable:** Top 10 pain points with ≥3 corroborating sources each. Segmented by SMB / mid-market / scale-up.
**Eval rubric:**
- [ ] Every claim has ≥2 independent sources dated within 18 months
- [ ] At least 3 sources are primary research (surveys, reports), not opinion pieces
- [ ] Pain points are stated in the operator's own language, not analyst jargon
- [ ] Each pain point has a "why now" — what changed in the last 24 months
- [ ] Includes at least one contrarian / dissenting data point

### R2 — AI Fatigue, Saturation & Anti-Hype Positioning
**Question:** What does the evidence say about AI fatigue in B2B buyers? What messaging cuts through when everyone is shouting "AI"?
**Deliverable:** The anatomy of AI fatigue + a messaging playbook (what to say, what to never say) with real-world examples of agencies that won by *not* leading with AI.
**Eval rubric:**
- [ ] Fatigue claim quantified (% of buyers, specific survey data)
- [ ] At least 5 named companies that positioned around craft/outcomes and grew
- [ ] At least 5 messaging patterns that demonstrably failed
- [ ] Messaging tested against "grandmother test" — would a non-technical founder understand and care?
- [ ] Identifies the exact vocabulary AI-fatigued buyers *do* respond to

### R3 — The Differentiated Company Archetype (ICP)
**Question:** Who are the companies that do it differently and have unmet demand? How do we recognise them in the wild? Where do they cluster?
**Deliverable:** 3–5 ICP archetypes with firmographics, behavioural tells, public signals, and named examples in AU market (+ global anchors).
**Eval rubric:**
- [ ] Each archetype has a falsifiable definition (a concrete test: "if X, then not this archetype")
- [ ] Includes named companies in Australia for each archetype
- [ ] Quantifies market size / TAM for each archetype in AU
- [ ] Identifies the specific *signal* that indicates unmet demand (waitlist, lead times, founder public complaints, job postings)
- [ ] Has an inverse: who is NOT our customer (equally important)

### R4 — Agency Economics, Pricing, and ROI Positioning ($250k AUD)
**Question:** What does the evidence say about agencies landing $250k+ engagements with guaranteed-ROI framings? What works, what blows up?
**Deliverable:** Pricing, scoping, and commercial model playbook. Concrete examples of agencies using value-based / outcome-based pricing in this range, including failures.
**Eval rubric:**
- [ ] Names ≥10 agencies operating in this price band with evidence (case studies, founder interviews)
- [ ] Identifies at least 3 distinct commercial structures (fixed, performance, hybrid) with pros/cons
- [ ] Includes math: what does an agency need to be true to guarantee ROI credibly?
- [ ] Accounts for AU market specifics (currency, procurement cycles, tax treatment, R&D incentives)
- [ ] At least 2 documented failures and what killed them

### R5 — "Liberating Growth" Narrative, Hooks & Virally-Engaging Frames
**Question:** What narrative frames cause B2B positioning to spread without being cringe? How do we build a "Liberating Growth" story that earns trust?
**Deliverable:** The Circles narrative architecture: the core story, the 3–5 hooks, the rituals/rhythms, the vocabulary, the visual grammar. Backed by positioning classics (April Dunford, Wynter, MarketingProfs) and modern case studies (e.g., Basecamp/37signals, Linear, Stripe early days).
**Eval rubric:**
- [ ] Grounded in ≥3 named positioning frameworks (cited)
- [ ] Includes ≥5 modern case studies of B2B companies that went viral *without* being cringe
- [ ] Story passes the "founder would forward this to another founder" test
- [ ] Has a specific anti-pattern list ("we will never say...")
- [ ] Produces at least 3 sharp one-liners Circles can use tomorrow

## 3. The loop (durable, re-runnable)

Every assistant follows the same loop. The *number of loops* is the KPI, not the polish of any single loop.

```
PLAN → SEARCH → EXTRACT → CHALLENGE → SCORE → REWRITE → COMMIT
  ^                                                         |
  +---------------------------------------------------------+
```

1. **PLAN** — Write 5 falsifiable hypotheses you're testing this loop.
2. **SEARCH** — Run ≥10 web queries. Capture raw notes with URLs.
3. **EXTRACT** — Pull quotes, numbers, and named examples. No paraphrase-only claims.
4. **CHALLENGE** — For every claim, answer: "What would make this wrong? What source would a skeptic bring?" Use Claude as a red-team.
5. **SCORE** — Run findings against the assistant's eval rubric. Count passes/fails.
6. **REWRITE** — Fix the fails. Delete what can't be defended.
7. **COMMIT** — Save to `research/circles/raw/R{n}_loop_{i}.md` with a one-line summary in the log.

## 4. Orchestrator responsibilities (me)

- Hold the north-star (30 × $250k, 9 months, ROI-in-9-months constraint)
- Keep the five streams from drifting or duplicating
- Synthesise across streams into a single positioning + pitch document
- Reverse-engineer the pipeline math from the goal backwards
- Refuse to let "AI" become the headline
- Notice stuckness → take a breath → move forward with the best-available evidence
- Iterate. Iterate. Iterate.

## 5. Reverse-engineering the goal (first pass — will refine)

Target: 30 projects × $250k AUD in 9 months.

Working backwards with industry-normal B2B agency conversion rates (these get challenged and refined in R4):
- If proposal → close rate = 35% → need ~86 serious proposals
- If qualified call → proposal = 60% → need ~143 qualified discovery calls
- If inbound/outbound → qualified = 20% → need ~715 first conversations
- Over 9 months = ~80/month = ~20/week = ~4/business day of first-touch conversations

Implication: Circles needs a **content + outbound engine** producing 4 first-touch conversations per business day with the right ICP from day one. This is tractable only if:
1. The positioning is sharp enough to self-qualify (R5)
2. The ICP is narrow enough to target (R3)
3. The ROI story is credible enough to justify $250k on a first call (R4)
4. The messaging cuts AI fatigue (R2)
5. It maps to a real, burning problem (R1)

That is why the five streams are these five streams.

## 6. Done = when the following exists on disk

- `research/circles/raw/R1..R5_loop_*.md` — at least one loop per stream, ideally more
- `research/circles/synthesis/POSITIONING.md` — the Circles positioning doc
- `research/circles/synthesis/PITCH.md` — the 1-page pitch + 10-slide deck outline
- `research/circles/synthesis/PIPELINE_MATH.md` — reverse-engineered GTM plan
- `research/circles/synthesis/NEXT_LOOPS.md` — what to run next when the user checks in

## 7. When stuck

Take a breath. The rule: **do not stop on a missing fact — note it, mark it `[UNVERIFIED]`, and keep moving.** A loop that finishes with 20 `[UNVERIFIED]` tags is more valuable than a loop that stalls at claim #3 chasing perfect citations.
