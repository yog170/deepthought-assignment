# Daily Reflection Decision Tree and AI Agent

---

## Objective

This project presents a structured analytical framework for evaluating daily performance and enabling continuous improvement. It integrates a deterministic decision tree for root-cause diagnosis with a rule-based AI reflection agent for automated analysis.

The objective is to transform unstructured daily observations into consistent, actionable insights through a repeatable decision-making system. The design prioritises clarity, reliability, and outcome-oriented execution over subjective or ad hoc reflection.

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Part A — Decision Tree Framework](#part-a--decision-tree-framework)
3. [Part B — AI Reflection Agent](#part-b--ai-reflection-agent)
4. [Repository Structure](#repository-structure)
5. [Execution Instructions](#execution-instructions)
6. [Engineering Principles](#engineering-principles)

---

## System Overview

The solution is composed of two complementary components that operate in a unified analytical pipeline:

| Component | Role in System |
|-----------|---------------|
| Decision Tree Framework | Performs structured root-cause analysis using a deterministic decision model |
| AI Reflection Agent | Classifies unstructured user input into predefined categories and generates standardised recommendations |

Both components converge to produce a consistent output: a clearly defined, three-point action plan for the subsequent day.

This design ensures that all inputs — whether structured or unstructured — result in actionable and comparable outcomes.

---

## Key Outcomes

The system delivers the following measurable benefits:

- Converts subjective reflection into structured, repeatable analysis
- Identifies root causes rather than surface-level issues
- Ensures every evaluation results in a defined next action
- Maintains consistency across both manual and automated analysis workflows
- Minimises ambiguity through deterministic logic and constrained outputs

---

## Part A — Decision Tree Framework

### Purpose

The decision tree provides a systematic method for evaluating daily performance. Rather than surface-level reflection, it applies root-cause analysis to determine the precise factor responsible for an outcome and prescribes a targeted corrective action.

### Core Diagnostic Questions

The framework is structured around three sequential questions:

1. What occurred today?
2. What was the underlying cause?
3. What is the appropriate corrective or reinforcing action?

### Decision Tree Structure

```
START
|
+-- Q1: Did I complete my primary goal today?
    |
    +-- YES
    |   +-- Q2: What contributed to the successful outcome?
    |       +-- Good Planning
    |       +-- Focused Execution
    |       +-- Minimal Distractions
    |           +-- Q3: Is this outcome replicable tomorrow?
    |               +-- YES --> Maintain current strategy
    |                           Document contributing factors
    |               +-- NO  --> Revise plan to fit new context
    |
    +-- NO
        +-- Q2: What was the primary cause of failure?
            |
            +-- Lack of Time
            |   +-- Was capacity overestimated?
            |       +-- YES --> Reduce scope of tomorrow's workload
            |       +-- NO  --> Apply structured time-blocking
            |
            +-- Lack of Clarity
            |   +-- Was the task fully understood prior to execution?
            |       +-- NO  --> Decompose task into discrete, actionable steps
            |       +-- YES --> Seek subject-matter guidance or additional resources
            |
            +-- Distractions
            |   +-- Were the distractions within the individual's control?
            |       +-- YES --> Eliminate or constrain identified distractions
            |       +-- NO  --> Develop a contingency schedule with buffer time
            |
            +-- Low Motivation
                +-- Was the goal set at a realistic level?
                    +-- NO  --> Recalibrate goal to an achievable scope
                    +-- YES --> Introduce an accountability or reward mechanism

+-- FINAL OUTPUT: Action Plan for Tomorrow
        +-- 1 Primary Goal
        +-- 1 Targeted Improvement
        +-- 1 Identified Constraint to Eliminate
```

### Design Rationale

The tree is structured to ensure that every decision path terminates in a specific, actionable recommendation. No branch concludes without a prescribed next step, eliminating ambiguity in the reflection process.

---

## Part B — AI Reflection Agent

### System Overview

The AI Reflection Agent is a deterministic natural language classification system designed to process unstructured user input and map it to predefined analytical categories.

The system follows a controlled processing pipeline to ensure consistent, interpretable, and reliable outputs without reliance on probabilistic or generative models.

### Input / Output Specification

**Sample Input:**
```
I planned to study 3 hours but only studied 1 hour due to distractions.
```

**System Output:**
```
Input Received       : I planned to study 3 hours but only studied 1 hour due to distractions.
Problem Detected     : Distractions
Suggestion           : Use focused time blocks (e.g. Pomodoro) and remove distractions before starting work.
Next Step            : Tomorrow: put your phone away and work in 25-minute focused sessions.
Guardrail Active     : Yes — output restricted to predefined categories only
```

### Processing Pipeline

```
Stage 1 — Input Ingestion
    User submits a free-text daily reflection statement.

Stage 2 — Pre-processing
    Input is normalised (lowercased, whitespace trimmed).
    Empty or null inputs are rejected with a structured error response.

Stage 3 — Keyword Classification
    Input is scanned against five predefined keyword sets:
    - Distractions   : distraction, distracted, phone, social media, interrupted
    - Time           : time, late, overestimate, ran out, not enough time
    - Clarity        : clarity, confused, unclear, not sure, complex
    - Motivation     : motivation, lazy, unmotivated, no energy, bored
    - Stress         : stress, anxious, overwhelmed, pressure, burnout

Stage 4 — Category Mapping
    The first matched keyword set determines the output category.
    If no match is found, the system defaults to the General Planning category.

Stage 5 — Structured Output Generation
    The system returns exactly four fields:
    - Problem Detected
    - Suggestion
    - Next Step
    - Guardrail Active
```

### Classification Categories

| Category | Trigger Keywords | Prescribed Action |
|----------|-----------------|-------------------|
| Distractions | distraction, phone, interrupted | Apply Pomodoro technique; eliminate identified distractions |
| Time Management | time, late, overestimate, ran out | Reduce task scope; implement time-blocking |
| Lack of Clarity | confused, unclear, not sure, complex | Decompose task; seek guidance before execution |
| Low Motivation | unmotivated, lazy, no energy, bored | Set reduced-scope goal; introduce reward mechanism |
| Stress / Overwhelm | stressed, anxious, overwhelmed, burnout | Prioritise 1-2 tasks; schedule structured breaks |
| General Planning | (fallback — no keyword match) | Review planning process; identify specific failure point |

### Reliability, Risk Control, and Guardrails

The system incorporates multiple layers of control to ensure deterministic behaviour, output consistency, and mitigation of erroneous or unpredictable responses:

| Control Mechanism | Implementation | Risk Mitigated |
|-------------------|---------------|----------------|
| Deterministic classification | All outputs are derived from fixed rule logic — no probabilistic or generative components | Eliminates hallucination and unpredictable output |
| Strict keyword mapping | Input is matched exclusively against a closed set of known terms | Prevents misclassification from ambiguous language |
| Controlled fallback | Unmatched inputs are routed to a safe, predefined general response | Ensures no input produces an undefined or null output |
| Fixed output schema | Every response returns exactly four fields with no free-form generation | Guarantees structural consistency across all outputs |

---

## Repository Structure

| File | Description |
|------|-------------|
| `ai_agent.py` | Rule-based AI reflection and classification agent |
| `Decision Tree.pdf` | Visual flowchart of the decision tree framework |
| `README.md` | Project documentation |

---

## Execution Instructions

Ensure Python 3.x is installed. No external dependencies are required.

```bash
# Run the AI reflection agent
python ai_agent.py
```

---

## Engineering Principles

The system design is guided by a set of core analytical and engineering principles to ensure reliability, clarity, and practical usability:

| Principle | Implementation |
|-----------|---------------|
| Root-cause analysis | Each decision branch isolates the underlying cause of an outcome, not merely its surface symptom |
| Deterministic output | All system responses are derived from fixed logic, ensuring reproducibility and auditability |
| Structural convergence | All decision paths — regardless of branch — terminate at a unified three-point action plan |
| Controlled classification | Output categories are closed and predefined, eliminating the risk of uncontrolled or erroneous responses |
| Minimal complexity | The system is intentionally constrained to the minimum logic required to produce reliable, actionable outputs |

---

> "Effective decision-making is not driven by intuition alone, but by structured analysis, disciplined categorisation, and a consistent commitment to actionable outcomes."
