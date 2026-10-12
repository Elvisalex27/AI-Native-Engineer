# Day 18 — Daily Learning Notes

## Topic
JSON and Persistent Data Storage in Python

## What I Learned

Today, I learned how to work with JSON files in Python and use them to store student records permanently.

### 1. Understanding JSON
JSON stands for JavaScript Object Notation. It is a data format commonly used to store and exchange structured information.

I learned that JSON can represent data structures such as lists and dictionaries.

### 2. Writing Data with `json.dump()`
I learned how to save Python data to a JSON file using:

```python
json.dump(students, file, indent=4)
```

The `indent=4` argument makes the JSON file easier to read.

### 3. Reading Data with `json.load()`
I learned how to retrieve data from a JSON file:

```python
with open("students.json", "r") as file:
    students = json.load(file)
```

This converts the JSON data into Python objects that I can work with.

### 4. Adding New Records
I learned that I must load existing student records before adding a new student.

The process is:

1. Load the existing records.
2. Create a new student dictionary.
3. Append the dictionary to the list.
4. Save the updated list back to the JSON file.

This taught me the importance of loading, modifying, and saving data in the correct order.

### 5. Working with Lists and Dictionaries
I practised accessing dictionary values using keys:

```python
student["name"]
student["score"]
```

I also reinforced the difference between a list containing multiple student dictionaries and a dictionary representing one student.

### 6. Calculating Student Statistics
I implemented functions to:
- Calculate the average student score.
- Find the student with the highest score.
- Find the student with the lowest score.
- Display all student records.

### 7. Building a Menu-Driven Application
I combined my functions into an interactive menu using a `while` loop and conditional statements.

This allowed users to select different operations without restarting the program after each operation.

## Challenges I Faced
- Understanding the difference between `json.dump()` and `json.load()`.
- Preserving existing student records when adding new ones.
- Understanding why I needed to load the existing list instead of creating a new empty list every time.
- Correctly updating variables when calculating average, highest, and lowest scores.

## How I Overcame the Challenges
I worked through each problem step by step, tested my code, and corrected mistakes as I improved my understanding of JSON and Python data structures.

## Key Takeaway
The most important concept I learned today was:

**Load → Modify → Save**

This pattern allows a program to retrieve existing data, make changes, and save the updated information for future use.

## Reflection
Day 18 helped me understand how Python applications can preserve information beyond a single program execution.

I also improved my ability to combine functions, lists, dictionaries, loops, and file handling into one application.

I am continuing to build my Python skills as part of my journey toward becoming an AI-Native Engineer.

## Status
- [x] Learned JSON basics.
- [x] Saved Python data to a JSON file.
- [x] Loaded JSON data into Python.
- [x] Added student records.
- [x] Displayed student records.
- [x] Calculated average, highest, and lowest scores.
- [x] Built the menu system.