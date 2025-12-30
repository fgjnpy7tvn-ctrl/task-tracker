# 📝 Task Tracker (CLI)

A simple and clean **Command-Line Task Tracker** written in Python.  
It allows you to manage daily tasks directly from the terminal with persistent storage.

This project was built as a learning project to practice **Python fundamentals, file handling, and basic CLI design**.

---

## ✨ Features

- View all tasks
- Add new tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage using a local text file
- Simple and user-friendly CLI interface

---

## 📋 Requirements

- Python **3.10+**
- No external libraries required

---

## ▶️ Run the Application

### Windows
```bash
py task_tracker.py
macOS / Linux
bash
python3 task_tracker.py
🧠 How It Works
Tasks are stored in a local file called tasks.txt.

Each task follows this format:

text
done|created_at|text
Example:
text
0|2025-01-10 14:30|Finish Python project
1|2025-01-10 15:00|Push code to GitHub
done: 0 = not completed, 1 = completed

created_at: timestamp of creation

text: task description

🗂️ Project Structure
text
task-tracker/
│
├── task_tracker.py   # Main application
├── tasks.txt         # Task storage file (generated at runtime)
├── .gitignore
└── README.md
⚠️ The tasks.txt file is intentionally ignored by Git to prevent committing personal data.

📸 Sample Usage
text
Task Tracker
1) View tasks
2) Add task
3) Mark task as completed
4) Delete task
5) Save & Exit
🚀 Future Improvements
Task priorities (Low / Medium / High)

Due dates

Export tasks to CSV

Search and filter functionality

Optional GUI or Web interface

🎯 Purpose
This project is part of a personal learning roadmap focused on:

Python programming

Automation

Building real, practical tools

Preparing for more advanced projects and products

