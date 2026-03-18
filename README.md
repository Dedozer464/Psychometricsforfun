# 🧠 Psychometrics for Fun

> Python simulations exploring human psychology, psychometric assessment, and workplace behaviour through three contrasting personality archetypes.

---

## Overview

This repository applies psychometric frameworks to model and compare how different personality types think, feel, behave, and perform in professional environments. Each module targets a distinct psychological construct — emotional intelligence, IQ, psychopathy, and maturity — and runs the same three personality archetypes through structured assessment and comparative analysis.

The goal is to demonstrate that **surface-level work performance does not equal psychological health**, and that understanding the full profile of a person matters enormously in hiring, team design, and leadership.

---

## Sample Output

→ [`sample_output.txt`](./sample_output.txt) — real console output from `emotional_intelligence.py` and `maturity_work_readiness.py`

```
Alice (Empathetic Leader)
  Maturity:       [█████████░]  92.3/100  (Highly Mature)
  Work Readiness: [█████████░]  93.9/100  (Highly Work Ready)

Charlie (People Pleaser)
  Maturity:       [████░░░░░░]  46.7/100  (Immature)          ← GAP
  Work Readiness: [██████░░░░]  67.1/100  (Moderately Ready)  ← GAP

Bob (Chaotic Jester)
  Maturity:       [██░░░░░░░░]  29.7/100  (Highly Immature)
  Work Readiness: [██░░░░░░░░]  26.5/100  (Not Work Ready)
```

---

## The Three Archetypes

All four modules are built around the same three characters, allowing cross-module comparison:

| Character | Archetype | Core Trait |
|---|---|---|
| **Alice** | Empathetic Leader | Genuine intelligence, high conscience, authentic leadership |
| **Bob** | Chaotic Jester | Average ability, impulsive, disorganised, low empathy |
| **Charlie** | People Pleaser | Competent on the surface, manipulative beneath it — the most analytically interesting case |

Charlie is the point of the whole exercise: high enough work readiness scores to pass a standard filter, but psychopathic and emotionally immature enough to be a long-term liability, especially in roles with authority over others.

---

## Modules

### `emotional_intelligence.py`
**Emotional Intelligence profiling across 7 trait dimensions**

Scores each archetype on traits including Caring, Social Awareness, Respectfulness, Humor, Passive Aggressiveness, and Need for Validation (0–10 scale). Generates individual profiles, comparative bar charts, and interaction simulations across four workplace scenarios: `conflict`, `success`, `struggle`, and `group`.

| Character | Avg EI Score |
|---|---|
| Alice | ~8.4 / 10 |
| Bob | ~5.6 / 10 |
| Charlie | ~7.4 / 10 (surface) |

---

### `iq_personality_model.py`
**IQ profiling with cognitive skill breakdown and decision-making analysis**

Assigns IQ scores and models 8 cognitive sub-skills (Verbal Reasoning, Logical Reasoning, Spatial Reasoning, Mathematical Ability, Processing Speed, Memory Retention, Emotional Understanding, Social Cognition). Uses a standard normal distribution to compute percentile rankings. Simulates problem-solving and decision-making across four scenarios: `conflict`, `project`, `learning`, and `innovation`.

| Character | IQ Score | Category |
|---|---|---|
| Alice | 135 | Very Superior (99th percentile) |
| Charlie | 118 | High Average (88th percentile) |
| Bob | 105 | Average (63rd percentile) |

---

### `psychopathy_assessment.py`
**PCL-R (Psychopathy Checklist – Revised) simulation**

Scores all 20 PCL-R items (0–2 scale, max 40) across two factors:
- **Factor 1** — Interpersonal/Affective (emotional deficiency, manipulation, shallow affect)
- **Factor 2** — Social Deviance (impulsivity, irresponsibility, behavioral problems)

Generates clinical risk assessments, behavioral predictions, and management recommendations.

| Character | PCL-R Score | Classification |
|---|---|---|
| Alice | 2 / 40 | Minimal — non-psychopathic |
| Bob | 20 / 40 | Moderate — impulsive, callous |
| **Charlie** | **27 / 40** | **Moderate-High — calculated exploiter** |

---

### `maturity_work_readiness.py`
**Maturity and work readiness profiling across 14 dimensions**

Separates maturity (emotional regulation, accountability, perspective-taking, delayed gratification) from work readiness (reliability, communication, problem-solving, ethics, leadership potential). Both composites feed into independent five-tier classification systems.

| Character | Maturity Score | Work Readiness Score |
|---|---|---|
| Alice | 93.0 / 100 — Highly Mature | 93.9 / 100 — Highly Ready |
| Charlie | 46.7 / 100 — Immature | 67.1 / 100 — Moderately Ready |
| Bob | 29.7 / 100 — Highly Immature | 26.5 / 100 — Not Ready |

---

## The Key Insight

```
Charlie passes the work readiness screen.
Charlie fails the maturity and psychopathy screen.
Charlie should not be in a leadership role.
```

This gap — between functional competence and psychological health — is the core question the repo explores.

---

## Requirements

No external dependencies. Pure Python 3.7+.

```bash
# Run any module independently
python emotional_intelligence.py
python iq_personality_model.py
python psychopathy_assessment.py
python maturity_work_readiness.py
```

Uses only standard library modules: `enum`, `dataclasses`, `typing`, `math`.

---

## Repository Structure

```
Psychometricsforfun/
├── emotional_intelligence.py      # EI trait profiling & interaction simulation
├── iq_personality_model.py        # IQ + cognitive skill breakdown
├── psychopathy_assessment.py      # PCL-R psychopathy scoring
├── maturity_work_readiness.py     # Maturity + work readiness dual assessment
├── README.md
└── LICENSE
```

---

## Disclaimer

These are **educational simulations**, not validated clinical instruments. Scores are hardcoded archetypes designed to illustrate psychometric concepts, not derived from real respondent data or calibrated item-response models. The PCL-R module in particular references a real clinical tool — it is used here for educational illustration only and should not be interpreted as a substitute for professional psychological assessment.

---

## Author

[Dedozer464](https://github.com/Dedozer464)

Licensed under EPL-2.0.

