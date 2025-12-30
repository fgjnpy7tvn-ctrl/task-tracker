# 📝 Task Tracker (CLI)

A simple but robust **command-line task tracker** written in Python.  
It allows you to manage daily tasks, track completion status, and store everything locally in a file.

This project was built as a learning project with a strong focus on:
- clean code
- user experience (UX)
- data safety
- extensibility

---

## ✨ Features

- Add new tasks
- View all tasks (open tasks shown first)
- Toggle task completion (done / undone)
- Delete individual tasks
- Clear all completed tasks at once
- Automatic saving after every action
- Persistent storage using a local file
- Graceful handling of invalid or corrupted data

---

## 🧠 How It Works

Tasks are stored locally in a `tasks.txt` file using the following format:

done|created_at|text

makefile
Αντιγραφή κώδικα

Example:
0|2025-01-10 14:30|Finish Python project
1|2025-01-10 15:00|Push code to GitHub

markdown
Αντιγραφή κώδικα

- `done`: `0` = not completed, `1` = completed  
- `created_at`: timestamp of creation  
- `text`: task description  

The application automatically validates file contents and ignores corrupted lines.

---

## 🚀 Getting Started

### Requirements
- Python **3.10+**
- No external dependencies

### Run the Application

#### Windows
```bash
py task_tracker.py
or

bash
Αντιγραφή κώδικα
python task_tracker.py
macOS / Linux
bash
Αντιγραφή κώδικα
python3 task_tracker.py
🖥️ Usage
When you run the program, you will see:

mathematica
Αντιγραφή κώδικα
Task Tracker
1) View tasks
2) Add task
3) Toggle task completion (done / undone)
4) Delete task
5) Clear completed tasks
6) Exit
Enter the number of the action you want to perform.

📁 Project Structure
arduino
Αντιγραφή κώδικα
task-tracker/
│
├── task_tracker.py
├── tasks.txt        # ignored by git
└── README.md
🔒 Data Safety
Automatic saving after every change

Handles invalid or corrupted data gracefully

No external services or databases required

🛠️ Future Improvements
Task priorities (Low / Medium / High)

Due dates and reminders

Export tasks to CSV

Search and filtering

GUI or web version

📚 Purpose
This project demonstrates:

Python fundamentals

File handling and validation

Clean CLI design

Product-oriented thinking

