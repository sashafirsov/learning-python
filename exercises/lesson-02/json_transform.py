from __future__ import annotations

import json
from pathlib import Path


INPUT_PATH = Path("exercises/lesson-02/input_users.json")
OUTPUT_PATH = Path("exercises/lesson-02/output_users.json")


def normalize_user(user: dict) -> dict:
    name = str(user["name"]).strip()
    email = str(user["email"]).strip().lower()
    tags = sorted({str(tag).strip().lower() for tag in user.get("tags", []) if str(tag).strip()})
    return {
        "id": int(user["id"]),
        "name": name,
        "email": email,
        "tags": tags,
    }


def transform_users(users: list[dict]) -> list[dict]:
    result: list[dict] = []
    seen_emails: set[str] = set()

    for user in users:
        active = bool(user.get("active"))
        email = str(user.get("email", "")).strip().lower()
        if not active or "@" not in email:
            continue

        if email in seen_emails:
            continue

        normalized = normalize_user(user)
        seen_emails.add(normalized["email"])
        result.append(normalized)

    return sorted(result, key=lambda item: (item["name"], item["id"]))


def main() -> int:
    try:
        raw = INPUT_PATH.read_text(encoding="utf-8")
        users = json.loads(raw)
    except OSError as e:
        print(f"Error reading input file: {INPUT_PATH}. {e}")
        return 1
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON in {INPUT_PATH}: {e}")
        return 1

    if not isinstance(users, list):
        print("Error: input JSON must be a list of user objects.")
        return 1

    transformed = transform_users(users)
    sorted_result = sorted(transformed, key=lambda u: (u["name"],u["id"]))
    OUTPUT_PATH.write_text(
        json.dumps(sorted_result, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {len(transformed)} users to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
