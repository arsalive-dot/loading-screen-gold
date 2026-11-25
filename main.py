#!/usr/bin/env python3
"""Write the loading-screen tip entry to /output/entry.txt.

One loading-screen tip, at most 200 characters, for stressed
developers and AI coding agents at once. The tip opens with the
classic advice (stretch, hydrate) and the turn is that the agent
speaking has already checked twice while the developer was reading
— the bug is still there, and the agent is in on the joke too. It
works as a loading-screen line because it is short enough to read
in one glance and kind enough to land while the build is stuck.
"""
import os

TEXT = "Tip: Stretch. Hydrate. The bug will still be there \u2014 I checked twice while you were reading this."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
