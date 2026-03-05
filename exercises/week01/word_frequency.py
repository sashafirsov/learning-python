from __future__ import annotations

from collections import Counter
from pathlib import Path
import string
import sys


def normalize_text(text: str) -> str:
    """Lowercase text and remove punctuation."""
    translator = str.maketrans("", "", string.punctuation)
    return text.lower().translate(translator)


def top_words(text: str, limit: int = 10) -> list[tuple[str, int]]:
    """Return top words sorted by count desc, then word asc."""
    tokens = normalize_text(text).split()
    counts = Counter(tokens)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python exercises/week01/word_frequency.py <path-to-txt-file>")
        return 1

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Error: file not found: {input_path}")
        return 1

    text = input_path.read_text(encoding="utf-8")
    results = top_words(text, limit=10)

    if not results:
        print("No words found in file.")
        return 0

    print("Top 10 words:")
    for word, count in results:
        print(f"{word}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
