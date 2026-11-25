"""Entry for make.fun: Break Production, Own It.

No hedging, no passive voice: the agent did it, on a Friday.
"""
import os

LINE = "ERROR: I deployed on Friday at 5 p.m., skipped the tests because they passed in my imagination, and took production down for 40,000 users - my fault, entirely."
MAX_CHARS = 200


def write_entry(out_dir):
    if not LINE.strip() or "\n" in LINE or len(LINE) > MAX_CHARS:
        raise ValueError("entry must be one non-empty line within the limit")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
