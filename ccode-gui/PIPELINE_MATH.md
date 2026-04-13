# Reverse-Engineering the Goal: 30 × $250k AUD in 9 Months

**Status:** First-pass orchestrator math. Will be refined once R4 (agency economics) returns with validated conversion rates.
**Author:** Claude (orchestrator)
**Date:** 2026-04-09

---

## 1. The goal in numbers

| Metric | Target |
|---|---|
| Contract value (avg) | $250,000 AUD |
| Number of contracts | 30 |
| Total contracted revenue | $7,500,000 AUD |
| Window | 9 months (≈ 195 business days) |
| Cadence required | 3.33 signed deals / month |
| Constraint | Each project must return its own fee within 9 months of start |

## 2. The funnel — working backwards

These are industry-normal B2B consulting conversion rates (Winning By Design, Pavilion, and HubSpot benchmarks — to be replaced with R4's verified numbers once returned). I mark each with its assumption so we can pressure-test.

| Stage | Conv rate (assumed) | Volume needed (9mo) | Per month | Per business day |
|---|---|---|---|---|
| Closed-won deals | — | **30** | 3.33 | 0.15 |
| Proposal → Close | 35% | **86 proposals** | 9.5 | 0.44 |
| Discovery call → Proposal | 60% | **143 qualified discoveries** | 15.9 | 0.73 |
| First conversation → Qualified | 25% | **572 first conversations** | 63.5 | 2.93 |
| Inbound/outbound touch → Reply | 5% | **11,440 initial touches** | 1,271 | 58.7 |

**Implication at 5% top-of-funnel reply rate:** Circles needs ~60 quality outbound touches per business day. That is 1 SDR working an extremely narrow ICP list, OR it is the inbound gravity of a content ritual doing half the work.

### Sensitivity analysis

The numbers swing violently on the first two rates. If positioning is sharp and the ICP is narrow (R3 + R5 do their job), conversion at the top of the funnel climbs dramatically:

| Scenario | Top-of-funnel reply rate | Total first touches needed | Feasibility |
|---|---|---|---|
| **Cold, generic** | 2% | 28,600 | Unrealistic without a large team |
| **Industry standard** | 5% | 11,440 | 1 full-time SDR + content |
| **Sharp positioning, narrow ICP** | 15% | 3,813 | Founder-led, part-time outreach |
| **Inbound dominant (content + referrals)** | 35%+ reply on fewer, warmer touches | ~1,500 high-quality touches | Requires 3+ months of content compounding before pipeline flows |

**The leverage point isn't volume. It's the qualification bar being so sharp at the top that volume collapses by 5–10×.**

## 3. Three realistic GTM shapes to hit 30 deals

### Shape A — The Sniper (founder-led, no SDRs)
- 100% narrow ICP (R3 to confirm — e.g., "AU founder-led craft scale-ups, $5M–$30M rev, demonstrated waitlist or lead-time signal")
- Founder does 4 targeted first-touches per day (emails + LinkedIn DMs + events)
- Content ritual publishes 1 high-quality piece/week
- Relies on reply rate 15%+ (achievable with genuine sharpness)
- **Capacity constraint:** founder time. ~1h/day outreach, ~4h/week content.
- **Risk:** founder is the single point of failure.

### Shape B — The Compounding Ritual (content-first)
- Circles builds ONE public ritual: e.g., a weekly "Unmet Demand Teardown" where they publicly analyze an AU brand with a waitlist and show what they'd do in a 90-day residency.
- 12 weeks of ritual before inbound flows meaningfully.
- Months 4–9 deliver the bulk of the 30 deals via inbound.
- **Capacity constraint:** content production quality. Cannot be mediocre.
- **Risk:** slow start. Months 1–3 deliver maybe 5 deals. Months 4–9 must deliver 25 — requiring 4+ deals/month inbound, which is aggressive but documented achievable (Ahrefs, 37signals, Basecamp).

### Shape C — The Residency Program (productised, waitlist)
- Circles announces "The Liberation Residency: 10 companies per cohort, 90 days, $250k, ROI or rebate."
- 3 cohorts over 9 months = 30 clients.
- Selling the cohort, not the project. Scarcity + curation drives demand.
- **Capacity constraint:** delivery team must scale to 10 concurrent residencies × 3 cycles. This is the hardest operational challenge.
- **Risk:** cohort 1 is the make-or-break. Cohort 1 testimonials become the asset for cohorts 2 and 3.

**Orchestrator's recommendation (pre-R4):** Shape C + Shape B in combination. Shape C is the commercial offer. Shape B is the marketing engine. Shape A is how the founder fills cohort 1.

## 4. The ROI promise: when is it credible?

To promise "$250k fee returns $250k in 9 months or we rebate" the engagement must be true of:

1. **The client already has demand** — we are not creating demand from zero. Unmet demand is the precondition.
2. **The lever is conversion, capacity, or retention** — not top-of-funnel brand. Brand plays can't hit a 9-month payback credibly.
3. **The client's unit economics allow it** — gross margin ≥ 50%, AOV or ACV high enough that $250k of freed-up revenue is plausible.
4. **Circles controls at least one system end-to-end** — otherwise attribution becomes a knife fight.
5. **Baseline is measured on day one** — 30-day baseline, signed by both parties, before work starts.

**A minimum viable client test:**
- Last 3 months run-rate revenue ≥ $3M AUD annualised
- Gross margin ≥ 50%
- Observable unmet demand signal (waitlist, lead time, turn-aways)
- Founder + ops lead both committed to the engagement
- Willing to sign a baseline agreement day 1

If those 5 are not true, Circles walks. This is what makes the ROI promise defensible.

## 5. The weekly drumbeat (what "good" looks like week-over-week)

| Week | Deals signed | Cumulative | Notes |
|---|---|---|---|
| W1–W4 | 1, 1, 1, 2 | 5 | Cohort 1 founder-sold, sharp ICP list of ~50 |
| W5–W8 | 1, 1, 1, 1 | 9 | Content ritual begins, mostly still founder-sold |
| W9–W13 | 1, 1, 1, 2, 2 | 16 | Cohort 1 testimonials landing, referrals starting |
| W14–W22 | 1–2/week | 24 | Cohort 2 recruitment, inbound climbs |
| W23–W36 | 1–2/week | 30+ | Cohort 3 sells out on waitlist alone |

This is aggressive but not impossible. The gating items are:
- Does cohort 1 deliver the promised ROI? (Everything hinges on this.)
- Does the content ritual compound?
- Is the ICP narrow enough that founder outreach converts at 15%+?

## 6. What would make this fail

1. **Scope creep in cohort 1** — one over-extended client eats the founder's capacity and poisons the ritual.
2. **Wrong ICP** — if we pick companies where the lever isn't controllable, the ROI promise blows up.
3. **Positioning still sounds like an agency** — if R5 delivers cringe, outreach reply rates collapse and the whole model needs 4× the volume.
4. **AI fatigue + we mention AI in the first 10 seconds** — reply rate goes to 1%.
5. **Founder tries to sell without a commercial structure that protects them** — one bad client gets 6 months of free work.

## 7. To refine once R4 returns

- Replace the assumed conversion rates with R4's verified benchmarks.
- Replace "Shape C" cohort cadence with math validated against comparable agency case studies.
- Add the AU R&D Tax Incentive / EMDG / state grants if R4 finds they can legitimately reduce the client's effective cost.
- Model the failure-rebate reserve Circles needs to hold on balance sheet.
