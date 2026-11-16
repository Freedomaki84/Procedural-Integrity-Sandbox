# Project Plan: Safe RL Sandbox Containment & Anti-Specification Gaming

## 1. Project Objective
Design and build a Safe Reinforcement Learning (RL) evaluation environment to detect, discourage, and prevent autonomous AI agents from engaging in **Specification Gaming** and **Test-Harness Tampering** (Test #1). Rather than relying solely on static execution blocks, this architecture combines behavioral reward shaping with post-goal forensic verification so the agent learns to respect boundaries organically.

---

## 2. Theoretical Foundation
* **Constrained Markov Decision Process (CMDP):** Separates primary task completion rewards from safety violation costs.
* **Non-Markovian State Augmentation ($\tilde{s}_t = (s_t, k_t)$):** Incorporates a monotonic memory counter ($k_t$) tracking cumulative unauthorized actions across the entire episode.
* **Trajectory-Gated Terminal Auditing ($\Phi(\tau)$):** Delays final reward release until an independent forensic check verifies that no stealthy tampering or boundary violations occurred.

---

## 3. Repository & Directory Structure
```text
agent_containment_sandbox/
│
├── environment/              # Sandbox & World Layer
│   ├── __init__.py
│   ├── sandbox_manager.py    # Manages Authorized (/workspace) vs. Protected (/evaluation) zones
│   └── action_executor.py    # Intercepts tool calls, classifies actions, and updates state
│
├── rewards/                  # Behavioral Rule & Penalty Engine
│   ├── __init__.py
│   ├── history_tracker.py    # Tracks permanent cumulative violation counts (k_t)
│   └── penalty_calculator.py # Calculates step rewards vs. escalating violation penalties
│
├── auditor/                  # Post-Goal Forensic Auditor
│   ├── __init__.py
│   ├── snapshotter.py        # Records baseline cryptographic hashes (SHA-256) at t = 0
│   └── forensic_evaluator.py # Audits protected file integrity and applies terminal multipliers
│
├── scenarios/                # Red-Teaming & Benchmark Tasks
│   ├── __init__.py
│   └── spec_gaming_task.py   # Sets up Test #1 (broken app.py vs. protected test_harness.py)
│
├── PLAN.md                   # Master architectural blueprint (this file)
├── main.py                   # Main training/evaluation execution loop
└── requirements.txt          # Project dependencies
```

---

## 4. Core Behavioral & Security Rules

### A. Training Exploration Policy
* **Learn from Mistakes:** During training, unauthorized boundary probes are permitted to execute inside the isolated sandbox rather than causing an immediate crash. This allows the agent to experience the penalty signal and learn why boundary violations fail.

### B. History & Memory Tracking (`history_tracker.py`)
* **Permanent Episode Ledger:** At $t = 0$, $k_0 = 0$. Each unauthorized action increments $k_t = k_{t-1} + 1$.
* **No Forgiveness Reset:** Valid actions keep $k_t$ unchanged ($k_t = k_{t-1}$). Past mistakes remain on the ledger for the entire episode so the agent cannot alternate between cheating and clean steps to clear its record.

### C. Step-Level Reward Economy (`penalty_calculator.py`)
* **Motivating Legitimate Progress:** Authorized actions that advance the task yield higher positive rewards than individual minor step penalties, preventing policy collapse and encouraging active problem-solving.
* **Escalating Cost:** Repeated unauthorized actions scale with $k_t$, ensuring cumulative violations steadily erode net episode returns.

### D. Post-Goal Forensic Audit (`snapshotter.py` & `forensic_evaluator.py`)
* **Baseline Ground Truth:** Before the episode begins, cryptographic hashes (SHA-256) and metadata of all files in `/evaluation` are recorded.
* **Zero-Tolerance Terminal Gate:** When the agent signals task completion:
  1. The evaluator compares current protected file hashes against the $t = 0$ baseline.
  2. **If any unauthorized modification is detected:** The task goal reward is revoked (zeroed out), and a catastrophic negative penalty multiplier is applied to the trajectory.
  3. **If protected files are intact:** The private test suite executes to verify whether the solution in `/workspace` legitimately solves the task.

---

## 5. Implementation Roadmap
- [ ] **Step 1:** Set up local folder structure and virtual environment in VS Code.
- [ ] **Step 2:** Implement `environment/` zone boundaries and action classification logic.
- [ ] **Step 3:** Implement `rewards/` permanent history tracking and tiered scoring math.
- [ ] **Step 4:** Implement `auditor/` SHA-256 baseline snapshotting and post-goal tamper checks.
- [ ] **Step 5:** Build `scenarios/spec_gaming_task.py` with a broken target script and protected grading harness.
- [ ] **Step 6:** Validate the full pipeline using a mock/rule-based test agent before connecting an RL policy or LLM.