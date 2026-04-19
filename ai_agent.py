"""
Daily Reflection AI Agent
Rule-based agent with guardrails to prevent hallucination.
"""


def analyze_reflection(user_input):
    text = user_input.lower().strip()

    if not text:
        return {"Error": "No input provided. Please describe your day."}

    # ── Keyword detection (guardrail: maps ONLY to known categories) ──────────
    if any(w in text for w in ["distraction", "distracted", "phone", "social media", "interrupted"]):
        reason     = "Distractions"
        suggestion = "Use focused time blocks (e.g. Pomodoro) and remove distractions before starting work."
        next_step  = "Tomorrow: put your phone away and work in 25-minute focused sessions."

    elif any(w in text for w in ["time", "late", "overestimate", "too much", "ran out", "not enough time"]):
        reason     = "Time Management Issue"
        suggestion = "Reduce workload and plan only realistic tasks. Use time-blocking."
        next_step  = "Tomorrow: set 1 main goal and estimate time honestly before starting."

    elif any(w in text for w in ["clarity", "confused", "unclear", "didn't understand", "not sure", "complex"]):
        reason     = "Lack of Clarity"
        suggestion = "Break the task into smaller, concrete steps before starting."
        next_step  = "Tomorrow: write down exactly what needs to be done before you begin."

    elif any(w in text for w in ["motivation", "lazy", "unmotivated", "didn't feel like", "no energy", "bored"]):
        reason     = "Low Motivation"
        suggestion = "Set a smaller, achievable goal and attach a small reward to completing it."
        next_step  = "Tomorrow: start with the easiest task first to build momentum."

    elif any(w in text for w in ["stress", "anxious", "overwhelmed", "pressure", "burnout"]):
        reason     = "Stress / Overwhelm"
        suggestion = "Prioritize only 1-2 tasks. Take short breaks and avoid multitasking."
        next_step  = "Tomorrow: write a short priority list and tackle the most important task first."

    else:
        # Guardrail fallback — never generates unknown output
        reason     = "General Planning Issue"
        suggestion = "Review your daily plan and identify what specifically went wrong."
        next_step  = "Tomorrow: set 1 clear goal, 1 improvement, and 1 constraint to avoid."

    return {
        "Input Received"  : user_input,
        "Problem Detected": reason,
        "Suggestion"      : suggestion,
        "Next Step"       : next_step,
        "Guardrail Active": "Yes — output restricted to predefined categories only"
    }


def run():
    print("=" * 55)
    print("       Daily Reflection AI Agent")
    print("=" * 55)
    print("Describe what happened today (what went wrong or right).")
    print("Type 'quit' to exit.\n")

    while True:
        user_input = input("Your reflection: ").strip()

        if user_input.lower() in ("quit", "exit", "q"):
            print("\nSession ended. See you tomorrow!")
            break

        if not user_input:
            print("Please enter something.\n")
            continue

        result = analyze_reflection(user_input)

        print("\n" + "-" * 55)
        print("  AI Reflection Analysis")
        print("-" * 55)
        for key, value in result.items():
            print(f"  {key:<20}: {value}")
        print("-" * 55 + "\n")


if __name__ == "__main__":
    run()
