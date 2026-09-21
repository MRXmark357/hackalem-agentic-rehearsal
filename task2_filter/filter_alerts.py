import json
import sys
from pathlib import Path

def main():
    file_path = Path(__file__).parent / "events.json"
    if not file_path.exists():
        print(f"Ошибка: файл {file_path} не найден.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        events = json.load(f)

    critical_events = [item for item in events if item.get("level") == "critical"]

    print("=== КРИТИЧЕСКИЕ СОБЫТИЯ ===")
    for item in critical_events:
        print(f"- {item['event']} (level: {item['level']})")

    print(f"\nкритичных {len(critical_events)}")

if __name__ == "__main__":
    main()
