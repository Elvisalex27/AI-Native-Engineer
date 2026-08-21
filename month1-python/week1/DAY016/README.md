# Day 016 - Error Handling & Student Score Manager

## What I Learned

Today I learned how to use error handling and input validation to make my Python programs safer and prevent them from crashing.

### Topics Covered

- `try` and `except`
- `ValueError`
- `ZeroDivisionError`
- `while True`
- `break`
- `continue`
- Input validation
- Validating numbers within a range
- Working with lists of dictionaries
- Finding the highest value using a loop
- Returning values from functions

## Project

### Student Score Manager

I built a student score management program that allows me to:

- Add students
- Store student names and scores
- Validate student scores
- View students
- Calculate the average score
- Find the student with the highest score
- Handle invalid user input

## Example Student Data

```python
students = [
    {"name": "Elvis", "score": 78},
    {"name": "Ada", "score": 95},
    {"name": "John", "score": 82}
]# Day 016 Daily Note

## What I Learned Today

Today I learned more about error handling and input validation in Python.

I learned how to use `try` and `except` to prevent my program from crashing when the user enters invalid data.

I also learned about:

- `ValueError`
- `ZeroDivisionError`
- `break`
- `continue`
- `return`
- Input validation
- Looping through a list of dictionaries
- Finding the highest score

## What I Built

I built a Student Score Manager that can:

- Add students
- Validate student scores between 0 and 100
- View students
- Calculate the average score
- Find the student with the highest score
- Handle invalid number inputs

## What I Found Difficult

The most difficult part was creating the `highest_score()` function.

At first, I was trying to store only the highest score, but I realized that I also needed to keep the student's name.

I learned that I can store the whole student dictionary:

```python
highest = students[0]