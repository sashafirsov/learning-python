Lesson 1 is ready and scaffolded.

Files created:
- [sample.txt](c:/aWork/python-learn/exercises/week01/sample.txt)
- [word_frequency.py](c:/aWork/python-learn/exercises/week01/word_frequency.py)

Run it:
```bash
python exercises/week01/word_frequency.py exercises/week01/sample.txt
```

**What you should learn from this lesson**
1. CLI args with `sys.argv`
2. File reading with `pathlib.Path`
3. Text normalization (`lower`, punctuation removal)
4. Counting with `collections.Counter`
5. Sorting by multiple keys: `(-count, word)`

**Your practice task (now)**
1. Change script to keep apostrophes inside words (e.g. `don't`).
2. Add stopword filtering (`the`, `and`, `is`).
3. Add a second CLI arg for `top N` words.

When you finish, send me your updated `word_frequency.py` and I’ll do a code review.