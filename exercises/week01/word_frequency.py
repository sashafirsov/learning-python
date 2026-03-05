from __future__ import annotations

from collections import Counter
from pathlib import Path
import string
import sys


def normalize_text(text: str) -> str:
    """Lowercase text and remove punctuation."""
    keep_apostrophes = string.punctuation.replace("'", "")
    translator = str.maketrans("", "", keep_apostrophes)
    return text.lower().translate(translator)


def top_words(text: str, limit: int) -> list[tuple[str, int]]:
    """Return top words sorted by count desc, then word asc."""
    tokens = normalize_text(text).split()
    stop_words = {"the", "and", "is"}
    no_stop_words_tokens = [token for token in tokens if token not in stop_words]
    counts = Counter(no_stop_words_tokens)
    return sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:limit]


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python exercises/week01/word_frequency.py <path-to-txt-file> <limit>")
        return 1

    input_path = Path(sys.argv[1])
    if not input_path.exists() or not input_path.is_file():
        print(f"Error: file not found: {input_path}")
        return 1
    try:
        limit = int(sys.argv[2])
        if limit <= 0:
            print("Error: limit must be a positive integer.")
            return 1
    except ValueError:
        print("Error: limit must be a positive integer.")
        return 1
    try:
        text = input_path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"Error reading file: {input_path}. {e}")
        return 1
    results = top_words(text, limit)

    if not results:
        print("No words found in file.")
        return 0

    print(f"Top {limit} words:")
    
    for word, count in results:
        print(f"{word}: {count}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
