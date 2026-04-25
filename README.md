# Daily Life and Productivity Tracker

A Python console application for managing daily tasks, tracking income and expenses, monitoring goals, and generating a simple productivity summary. This project was developed for the ADS100 course, *Introduction to Computational Thinking and Programming*.

## Project Overview

The Daily Life and Productivity Tracker combines three common personal-management needs into one menu-driven program:

- Task management for adding, viewing, completing, and deleting tasks
- Expense and savings tracking for income, spending categories, and current balance
- Goal tracking with progress updates and visual progress bars
- Daily summary with task completion, financial status, goal counts, and a productivity score

The application runs in the terminal and uses Python lists and dictionaries to store session data while the program is running.

## Features

### Task Manager

- Add new tasks
- View pending and completed tasks separately
- Mark pending tasks as complete
- Delete tasks from the task list

### Expense and Savings Tracker

- Add income records with source information
- Add expenses by category:
  - Food
  - Transport
  - Study
  - Entertainment
  - Other
- View all income and expense records
- Calculate total income, total expense, savings, or deficit
- View expenses grouped by category

### Goal Tracker

- Add personal, academic, or financial goals
- Track progress toward a numeric target
- View active and completed goals
- Display progress using a 10-segment console progress bar

### Daily Summary

- Shows total, completed, and pending tasks
- Shows income, expenses, savings, or deficit
- Shows active and completed goals
- Calculates a productivity score out of 100 using:
  - Task completion
  - Financial health
  - Completed goals

## Computational Thinking Concepts Used

This project demonstrates core programming and computational thinking ideas:

- **Decomposition:** The program is divided into task, finance, goal, and summary modules.
- **Abstraction:** Lists and dictionaries represent real-world records such as tasks, expenses, incomes, and goals.
- **Iteration:** Loops are used for menus, record display, filtering, and total calculations.
- **Selection:** Conditional logic handles menu choices, validation, categories, and summary decisions.
- **Modular programming:** Separate functions keep each feature organized and easier to maintain.

## Project Structure

```text
ads100_project/
├── app.py                 # Main productivity tracker application
├── main.py                # Default uv starter file
├── pyproject.toml         # Project metadata and Python requirement
├── uv.lock                # uv lock file
├── README.md              # Project documentation
├── bug_fix_list.txt       # Notes for fixes or improvements
└── project_report.docx    # Project report document
```

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/) for environment and command management

The project currently uses only Python standard library features, so there are no extra package dependencies.

## How to Run the App Using uv

1. Clone the repository:

```bash
git clone <your-repository-url>
cd ads100_project
```

2. Sync the project environment:

```bash
uv sync
```

3. Run the main application:

```bash
uv run python app.py
```

4. Use the menu options in the terminal:

```text
1. Task Manager
2. Expense and Savings Tracker
3. Goal Tracker
4. Daily Summary
5. Exit
```

## Example Use Case

A student can use the app to:

- Add a task such as `Complete ADS100 Report`
- Add income such as `5000 BDT` from allowance
- Add an expense such as `200 BDT` for food
- Add a goal such as `Read 10 books`
- View the daily summary to check productivity progress

## Current Limitations

- Data is stored in memory only, so records reset after closing the program.
- The application is terminal-based and does not include a graphical interface.
- Reports and charts are not generated automatically.

## Future Improvements

- Save and load records using JSON or CSV files
- Add a graphical user interface with Tkinter
- Add spending charts using Matplotlib
- Add reminders for pending tasks
- Add date-based filtering for income, expenses, tasks, and goals

## Course Information

- **Course:** ADS100 - Introduction to Computational Thinking and Programming
- **Project:** Daily Life and Productivity Tracker
- **Semester:** Spring 2026
- **Department:** Artificial Intelligence and Data Science

## Conclusion

The Daily Life and Productivity Tracker is a practical Python project that applies programming fundamentals to everyday organization. It demonstrates how simple data structures, functions, loops, and conditions can be combined to build a useful console-based productivity tool.
