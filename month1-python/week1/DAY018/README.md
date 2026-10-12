# Day 18: Student JSON Manager

## Project Overview
The Student JSON Manager is a Python command-line application that manages student records using JSON for persistent data storage.

The project demonstrates how to store, retrieve, update, and process student information using Python's built-in `json` module.

## Features
- **Add Student:** Collects a student's name and score and saves the record to a JSON file.
- **View Students:** Displays all saved student records.
- **Average Score:** Calculates the average score of all students.
- **Highest Score:** Identifies the student with the highest score.
- **Lowest Score:** Identifies the student with the lowest score.
- **Menu System:** Provides an interactive menu that allows users to select operations.
- **Persistent Storage:** Keeps student records in a JSON file so they can be accessed when the program runs again.

## Technologies Used
- Python
- JSON
- File Handling
- Lists and Dictionaries
- Functions
- Loops and Conditional Statements

## Project Structure

```text
Day018/
├── student_manager.py
├── students.json
├── README.md
└── daily_note.md
```

## How to Run

1. Make sure Python 3 is installed.
2. Open your terminal in the project directory.
3. Run the program:

   ```bash
   python3 student_manager.py
   ```

4. Follow the menu instructions to manage student records.

## What I Learned
- How to use `json.dump()` to save Python data to a JSON file.
- How to use `json.load()` to retrieve data from a JSON file.
- How to preserve existing records when adding new students.
- How to manipulate lists of dictionaries.
- How to calculate averages and find the highest and lowest scores.
- How to combine functions into a menu-driven application.
- The difference between data stored in memory and data stored permanently in a file.

## Conclusion
This project strengthened my understanding of Python file handling, JSON, functions, and data manipulation. It also helped me understand how applications preserve information between program executions.

This project is part of my four-month journey toward becoming an AI-Native Engineer.