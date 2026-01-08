from pathlib import Path
from typing import List

from models import Task
TASKS_FILE = Path("tasks.txt")
def load_tasks() -> List[Task]:
    tasks: List[Task] = []

    if not TASKS_FILE.exists():
        return tasks

    with TASKS_FILE.open(mode="r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            task = Task.from_storage_line(line)
            if task is None:
                continue

            tasks.append(task)

    return tasks
def save_tasks(tasks: List[Task]) -> None:
    with TASKS_FILE.open(mode="w", encoding="utf-8") as f:
        for task in tasks:
            line = task.to_storage_line()
            f.write(line + "\n")


