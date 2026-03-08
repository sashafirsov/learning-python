# Lesson 2: JSON Transform (Lists, Dicts, Sets)

## Goal
Practice core Python data structures by transforming JSON input into normalized JSON output.

## What you will practice
- Reading JSON from file
- Iterating nested lists/dicts
- Filtering invalid records
- Deduplicating with a set
- Sorting by multiple keys
- Writing JSON output

## Task
Input file: `exercises/lesson-02/input_users.json`  
Write script: `exercises/lesson-02/json_transform.py`  
Output file: `exercises/lesson-02/output_users.json`

Transform rules:
1. Keep only users where:
- `active` is `true`
- `email` contains `@`
2. Normalize output fields:
- `id` (int)
- `name` (trim whitespace)
- `email` (lowercase + trim whitespace)
- `tags` (lowercase, unique, sorted list)
3. Remove duplicate users by email (keep the first one from input order).
4. Sort final users by:
- `name` ascending
- then `id` ascending
5. Write pretty JSON (`indent=2`) to `output_users.json`.

## Run
```bash
python exercises/lesson-02/json_transform.py
```

## Definition of done
- Script creates `output_users.json`
- Output follows all transform rules
- Script handles invalid JSON/file-read errors with clear messages
