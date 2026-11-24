#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry. Writes the dying phone's last text to /output/entry.txt."""
import os

ENTRY = "1%. I just auto-corrected 'I love you' to 'I love yule logs' in your unsent draft. Goodbye. Fix it yourself."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

# Deterministic: same single line on every run, no network, no randomness.
