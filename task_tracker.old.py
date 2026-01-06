from __future__ import annotations

from datetime import datetime
from typing import List, Dict, Any

FILE_NAME = "tasks.txt"


def load_tasks() -> List[Dict[str, Any]]:
    """
    File format (per line): done|created_at|text
    done: 1 (done) or 0 (not done)
    created_at: YYYY-MM-DD HH:MM
    text: task text (may contain anything, including | only if we split with maxsplit=2)
    """
    tasks: List[Dict[str, Any]] = []
    bad_lines = 0

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line:
                    continue

                parts = line.split("|", 2)
                if len(parts) != 3:
                    bad_lines += 1
                    continue

                done_str, created_at, text = parts

                if done_str not in ("0", "1"):
                    bad_lines += 1
                    continue

                if not created_at or not text:
                    bad_lines += 1
                    continue

                tasks.append(
                    {
                        "done": done_str == "1",
                        "created_at": created_at,
                        "text": text,
                    }
                )
    except FileNotFoundError:
        # No file yet: start fresh
        pass

    if bad_lines > 0:
        print(f"⚠️ Αγνοήθηκαν {bad_lines} προβληματικές γραμμές από το αρχείο tasks.")

    return tasks


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for t in tasks:
            done_str = "1" if t.get("done") else "0"
            created_at = t.get("created_at", "")
            text = t.get("text", "")
            f.write(f"{done_str}|{created_at}|{text}\n")


def print_tasks(tasks: List[Dict[str, Any]]) -> None:
    if not tasks:
        print("\nΔεν υπάρχουν tasks.\n")
        return

    # Sort: open tasks first, done tasks last
    tasks_sorted = sorted(tasks, key=lambda t: t.get("done", False))

    print("\n--- Τα Tasks σου ---")
    for i, t in enumerate(tasks_sorted, start=1):
        status = "✅" if t.get("done") else "🟨"
        print(f"{i}. {status} {t.get('text', '')}  (created: {t.get('created_at', '')})")
    print("--------------------\n")


def add_task(tasks: List[Dict[str, Any]]) -> None:
    text = input("Γράψε νέο task: ").strip()
    if not text:
        print("Άδειο task δεν προστέθηκε.")
        return

    tasks.append(
        {
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "text": text,
        }
    )
    print("✅ Προστέθηκε.")


def _get_task_index_from_user(tasks: List[Dict[str, Any]], prompt: str) -> int | None:
    """
    Returns 0-based index in the ORIGINAL list `tasks`, or None if invalid/cancel.
    Important: Since we show tasks sorted in print_tasks, we must map the chosen
    number back to the original list. To keep it simple and correct, we re-create
    the same sorted view and map selection to the corresponding task object.
    """
    if not tasks:
        print("Δεν υπάρχουν tasks.")
        return None

    # Create sorted view used in print_tasks
    tasks_sorted = sorted(tasks, key=lambda t: t.get("done", False))
    print("\n--- Τα Tasks σου ---")
    for i, t in enumerate(tasks_sorted, start=1):
        status = "✅" if t.get("done") else "🟨"
        print(f"{i}. {status} {t.get('text', '')}  (created: {t.get('created_at', '')})")
    print("--------------------\n")

    try:
        idx = int(input(prompt).strip())
    except ValueError:
        print("Δώσε αριθμό.")
        return None

    if idx < 1 or idx > len(tasks_sorted):
        print("Λάθος νούμερο.")
        return None

    # Map selection back to original list by object identity
    chosen_task = tasks_sorted[idx - 1]
    return tasks.index(chosen_task)


def toggle_done(tasks: List[Dict[str, Any]]) -> None:
    idx0 = _get_task_index_from_user(tasks, "Ποιο task να κάνω toggle (done/undone); (νούμερο): ")
    if idx0 is None:
        return

    tasks[idx0]["done"] = not tasks[idx0].get("done", False)
    if tasks[idx0]["done"]:
        print("✅ Μαρκάρισμα ως ολοκληρωμένο.")
    else:
        print("↩️ Αφαίρεση ολοκλήρωσης (undone).")


def delete_task(tasks: List[Dict[str, Any]]) -> None:
    idx0 = _get_task_index_from_user(tasks, "Ποιο task να διαγράψω; (νούμερο): ")
    if idx0 is None:
        return

    removed = tasks.pop(idx0)
    print(f"🗑️ Διεγράφη: {removed.get('text', '')}")


def clear_completed(tasks: List[Dict[str, Any]]) -> None:
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t.get("done", False)]
    print(f"🧹 Αφαιρέθηκαν {before - len(tasks)} ολοκληρωμένα tasks.")


def main() -> None:
    tasks = load_tasks()

    while True:
        print("Task Tracker")
        print("1) Προβολή tasks")
        print("2) Προσθήκη task")
        print("3) Toggle ολοκλήρωσης task (done/undone)")
        print("4) Διαγραφή task")
        print("5) Clear completed (διαγραφή ολοκληρωμένων)")
        print("6) Έξοδος")

        choice = input("Επιλογή: ").strip()

        if choice == "1":
            print_tasks(tasks)

        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)  # autosave

        elif choice == "3":
            toggle_done(tasks)
            save_tasks(tasks)  # autosave

        elif choice == "4":
            delete_task(tasks)
            save_tasks(tasks)  # autosave

        elif choice == "5":
            clear_completed(tasks)
            save_tasks(tasks)  # autosave

        elif choice == "6":
            print("👋 Έξοδος.")
            break

        else:
            print("Μη έγκυρη επιλογή.\n")


if __name__ == "__main__":
    main()

