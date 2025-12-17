from datetime import datetime

FILE_NAME = "tasks.txt"


def load_tasks():
    tasks = []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # format: done|created_at|text
                parts = line.split("|", 2)
                if len(parts) != 3:
                    continue
                done_str, created_at, text = parts
                tasks.append({
                    "done": done_str == "1",
                    "created_at": created_at,
                    "text": text
                })
    except FileNotFoundError:
        pass
    return tasks


def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for t in tasks:
            done_str = "1" if t["done"] else "0"
            f.write(f"{done_str}|{t['created_at']}|{t['text']}\n")


def print_tasks(tasks):
    if not tasks:
        print("\nΔεν υπάρχουν tasks.\n")
        return

    print("\n--- Τα Tasks σου ---")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t["done"] else "🟨"
        print(f"{i}. {status} {t['text']}  (created: {t['created_at']})")
    print("--------------------\n")


def add_task(tasks):
    text = input("Γράψε νέο task: ").strip()
    if not text:
        print("Άδειο task δεν προστέθηκε.")
        return
    tasks.append({
        "done": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "text": text
    })
    print("✅ Προστέθηκε.")


def mark_done(tasks):
    if not tasks:
        print("Δεν υπάρχουν tasks.")
        return
    print_tasks(tasks)
    try:
        idx = int(input("Ποιο task ολοκληρώθηκε; (νούμερο): "))
        if idx < 1 or idx > len(tasks):
            print("Λάθος νούμερο.")
            return
        tasks[idx - 1]["done"] = True
        print("✅ Μαρκάρισμα ως ολοκληρωμένο.")
    except ValueError:
        print("Δώσε αριθμό.")


def delete_task(tasks):
    if not tasks:
        print("Δεν υπάρχουν tasks.")
        return
    print_tasks(tasks)
    try:
        idx = int(input("Ποιο task να διαγράψω; (νούμερο): "))
        if idx < 1 or idx > len(tasks):
            print("Λάθος νούμερο.")
            return
        removed = tasks.pop(idx - 1)
        print(f"🗑️ Διεγράφη: {removed['text']}")
    except ValueError:
        print("Δώσε αριθμό.")


def main():
    tasks = load_tasks()

    while True:
        print("Task Tracker")
        print("1) Προβολή tasks")
        print("2) Προσθήκη task")
        print("3) Ολοκλήρωση task")
        print("4) Διαγραφή task")
        print("5) Αποθήκευση & Έξοδος")

        choice = input("Επιλογή: ").strip()

        if choice == "1":
            print_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Αποθηκεύτηκε. Έξοδος.")
            break
        else:
            print("Μη έγκυρη επιλογή.\n")


if __name__ == "__main__":
    main()
