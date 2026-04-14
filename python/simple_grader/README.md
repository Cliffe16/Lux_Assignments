# Student Grading System

A command-line Python application that calculates student averages, assigns grades and ouputs the data in a CSV file.

## Features

* **Continuous Entry:** Allows you to enter data for multiple students in a single session using a `while` loop.
* **Grade Calculation:** Automatically calculates the average of three marks.
* **Letter Grading:** Evaluates the average and assigns a grade based on the following scale:
  * **A:** 70 and above
  * **B:** 60 to 69
  * **C:** 50 to 59
  * **D:** 40 to 49
  * **E:** 30 to 39
  * **Fail:** Below 30
* **Data Storage:** Appends each student's name, individual marks, average and final grade to a `grades.csv` file for permanent record-keeping.

## Prerequisites

* Python 3.x installed on your system.
* No external libraries required (uses the built-in `csv` module).

## How to Run

1. Open your terminal or command prompt.
2. Navigate to the directory where the script is saved.
3. Run the program using the following command:
   ```bash
   python3 main.py
```
