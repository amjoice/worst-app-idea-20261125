#!/usr/bin/env python3
"""Worst App Idea Ever Pitched — make.fun entry.

Writes one sentence (<=240 chars) pitching the worst, most useless
app imaginable to /output/entry.txt. Stdlib only.
"""

import os

# Final pitch (237 chars): sharpened after comparing five candidates
# against the judge's criteria — the strongest mismatch is an app that
# reports rain only after you are already soaked, sold as a premium
# subscription with a leaderboard for the world's wettest commuters.
ENTRY = (
    "UmbrellaSync is an AI-powered app that uses real-time satellite "
    "data to tell you it is raining only after you are already soaked, "
    "with a $12 monthly plan for premium wetness alerts and a "
    "leaderboard ranking the world's wettest commuters."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, must be 1-240"
    assert text.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
