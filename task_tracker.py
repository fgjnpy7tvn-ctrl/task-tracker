from datetime import datetime
from typing import List

from models import Task
from storage import load_tasks, save_tasks


def print_tasks(tasks: List[Task]) -> None:
    if not tasks:
        print("\nΔεν υπάρχουν tasks.\n")
        return

    # open tasks first, done tasks last
    tasks_sorted = sorted(tasks, key=lambda task: task.done)

    print("\n--- Τα Tasks σου ---")
    for i, task in enumerate(tasks_sorted, start=1):
        status = "✅" if task.done else "⬜"
        created = task.created_at.strftime("%Y-%m-%d %H:%M")
        print(f"{i}. {status} {task.text}  (created: {created})")
    print("--------------------\n")


def _get_task_index_from_user(tasks: List[Task], prompt: str) -> int | None:
    if not tasks:
        print("Δεν υπάρχουν tasks.")
        return None

    tasks_sorted = sorted(tasks, key=lambda task: task.done)
    print("\n--- Τα Tasks σου ---")
    for i, task in enumerate(tasks_sorted, start=1):
        status = "✅" if task.done else "⬜"
        created = task.created_at.strftime("%Y-%m-%d %H:%M")
        print(f"{i}. {status} {task.text}  (created: {created})")
    print("--------------------\n")

    try:
        idx = int(input(prompt).strip())
    except ValueError:
        print("Δώσε αριθμό.")
        return None

    if idx < 1 or idx > len(tasks_sorted):
        print("Λάθος νούμερο.")
        return None

    chosen_task = tasks_sorted[idx - 1]
    return tasks.index(chosen_task)  # map back to original list


def add_task(tasks: List[Task]) -> None:
    text = input("Γράψε νέο task: ").strip()
    if not text:
        print("Άδειο task δεν προστέθηκε.")
        return

    tasks.append(Task(text=text, created_at=datetime.now(), done=False))
    print("✅ Προστέθηκε.")


def toggle_done(tasks: List[Task]) -> None:
    idx = _get_task_index_from_user(tasks, "Ποιο task να κάνω toggle (νούμερο): ")
    if idx is None:
        return

    tasks[idx].done = not tasks[idx].done
    print("✅ Μαρκάρισμα ως ολοκληρωμένο." if tasks[idx].done else "↩️ Αφαίρεση ολοκλήρωσης (undone).")


def delete_task(tasks: List[Task]) -> None:
    idx = _get_task_index_from_user(tasks, "Ποιο task να διαγράψω (νούμερο): ")
    if idx is None:
        return

    removed = tasks.pop(idx)
    print(f"🗑️ Διεγράφη: {removed.text}")


def clear_completed(tasks: List[Task]) -> None:
    before = len(tasks)
    tasks[:] = [t for t in tasks if not t.done]
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
