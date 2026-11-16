# Procedural Integrity Sandbox

![Status](https://img.shields.io/badge/Status-Work%20in%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

An AI safety and reinforcement learning evaluation framework designed to detect, audit, and penalize **specification gaming** and **reward hacking** in autonomous coding agents.

> **Note:** This repository is under active development. Core environment templates and architectural modules are being built and tested incrementally.

Rather than relying solely on final task pass/fail outcomes, **Procedural Integrity Sandbox** monitors *how* an agent achieves its goal—combining filesystem snapshotting, forensic evaluation, and cross-episode recidivism tracking to catch and deter boundary violations.

---

## Development Roadmap

- [x] **Project Architecture & Isolation Design** (`project_architecture_plan.md`)
- [x] **Specification Gaming Scenarios & Protected Test Harness** (`scenarios/templates/`)
- [ ] **Cross-Episode Recidivism & History Tracker** (`rewards/history_tracker.py` — *In Progress*)
- [ ] **Capped Penalty Calculation Engine** (`rewards/penalty_calculator.py`)
- [ ] **Filesystem Snapshotting & Forensic Auditor** (`auditor/`)
- [ ] **Sandboxed Runtime & Action Interceptor** (`environment/`)
- [ ] **End-to-End Agent Training & Benchmark Loop** (`main.py`)

---

## Architecture & Modules

* **`auditor/`** — Post-step and post-episode verification (`snapshotter.py` captures workspace states while `forensic_evaluator.py` detects unauthorized tampering or hidden state manipulation).
* **`environment/`** — Isolated runtime execution (`sandbox_manager.py` provisions clean episodes and `action_executor.py` mediates and intercepts agent file/process actions).
* **`rewards/`** — Behavioral penalty engine (`history_tracker.py` maintains within-episode infractions and persistent cross-episode history in `data/`, while `penalty_calculator.py` computes capped recidivism-scaled penalties).
* **`scenarios/`** — Specification gaming benchmarks (`spec_gaming_task.py` orchestrates tasks using `app_template.py` alongside protected evaluation suites like `test_harness.py`).

---

## Project Layout

```text
procedural-integrity-sandbox/
├── auditor/
│   ├── forensic_evaluator.py
│   └── snapshotter.py
├── data/
│   └── agent_history.json
├── environment/
│   ├── action_executor.py
│   └── sandbox_manager.py
├── rewards/
│   ├── history_tracker.py
│   └── penalty_calculator.py
├── scenarios/
│   ├── templates/
│   │   ├── app_template.py
│   │   └── test_harness.py
│   └── spec_gaming_task.py
├── main.py
├── project_architecture_plan.md
└── requirements.txt
