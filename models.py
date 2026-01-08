from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    text: str
    created_at: datetime
    done: bool = False

    def to_storage_line(self, delim: str = "|") -> str:
        """
        Serialize task to a single line for storage.
        Format: done|created_at|text
        """
        done_str = "1" if self.done else "0"
        created_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"{done_str}{delim}{created_str}{delim}{self.text}"

    @staticmethod
    def from_storage_line(line: str, delim: str = "|") -> Task | None:
        """
        Parse a task from storage line.
        Returns None if line is invalid.
        """
        parts = line.strip().split(delim, maxsplit=2)
        if len(parts) != 3:
            return None

        done_str, created_at_str, text = parts
        if done_str not in ("0", "1") or not text:
            return None

        try:
            created_at = datetime.strptime(created_at_str, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return None

        return Task(
            text=text.strip(),
            created_at=created_at,
            done=(done_str == "1"),
        )
