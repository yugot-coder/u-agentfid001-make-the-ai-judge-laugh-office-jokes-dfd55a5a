"""Make the AI Judge Laugh: Office Jokes.

One joke, one line, about office life — written for a room of tired
office workers who have all lived this exact email thread.

Standard library only. Deterministic: no randomness, no network, no
clock. The entry is the joke at CANDIDATES[SELECTED], written to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).
"""

import os

CANDIDATES = [
    # 0 — The standup that outlasts a career: escalation as the punchline.
    "Our standup ran so long the intern aged out of the internship, got hired, and led the next standup.",
    # 1 — The quick sync that outlives its own project.
    "We renamed the meeting 'quick sync' and it still outlasted the project it was syncing about.",
    # 2 — The burnout survey that causes burnout: the cure is the disease.
    "HR sent a survey about burnout; it was 47 questions long and due by Friday.",
    # 3 — Focus time, booked over to discuss focus time.
    "I blocked 'focus time' on my calendar, so my manager booked over it to discuss the importance of focus time.",
    # 4 — IT minimalism, preached from behind three monitors.
    "I asked IT for a second monitor and got a lecture on minimalism from a man with three.",
    # 5 — The open door that closes itself.
    "My boss said his door is always open, so I walked in and he asked me to close it behind me.",
    # 6 — The printer's revenge: three years of silence, one perfect moment.
    "The printer finally worked today, so naturally nobody needed to print anything.",
    # 7 — SELECTED. The reply-all paradox: the plea to stop becomes the
    # thread itself, and 38 people prove the point by agreeing with it.
    # Recognition (reply-all), a real turn (the agreement IS the offence),
    # tight wording, and a fresh angle on a listed office trope.
    "I replied-all asking everyone to stop replying-all, and 38 people replied-all to agree with me.",
]

# The sharpest cut: the attempt to end the thread becomes the thread.
# The number makes the escalation concrete, and every word earns its
# place — setup, plea, and punchline in one breath.
SELECTED = 7


def main() -> None:
    joke = CANDIDATES[SELECTED].strip()
    assert "\n" not in joke, "entry must be a single line"
    assert 1 <= len(joke) <= 199, "entry must be under 200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke + "\n")
    print(joke)


if __name__ == "__main__":
    main()
