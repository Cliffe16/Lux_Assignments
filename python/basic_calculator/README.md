# Python Basic Calculator

A simple, interactive command-line calculator written in Python. This program allows users to perform basic arithmetic operations continuously until they explicitly choose to exit.

### Overview
The app is a learning project from Lux Dev answering the following question:
Write a Python program that acts as a basic calculator. Your program should:

1. Define a function called calculator that takes three parameters: num1, num2, and operation.

2. Perform addition, subtraction, multiplication, or division based on the operation parameter.

3. Handle division by zero by returning "Error: Division by zero!".

4. Return "Invalid operation" if the user enters an operation other than +, -, *, or /.

5. Use a loop to keep asking the user for numbers and the operation until the user decides to stop.

6. Print the result of each calculation.

Hint: Use if, elif, and else statements in your function.


## Features

* **Basic Arithmetic:** Supports addition (`+`), subtraction (`-`), multiplication (`*`) and division (`/`).
* **Continuous Loop:** The program keeps running after each calculation, asking if you want to perform another one, so you don't have to restart the script manually.
* **Robust Error Handling:** * Prevents the program from crashing if a user types text instead of a number.
  * Also handles division by zero error.

## Prerequisites

* Python 3.x installed on your system.

## How to Run

1. Open your terminal.
2. Navigate to the directory where the script is saved:
   ```bash
   cd ~/Lux_Assignments/python/basic_calculator/
```
3. Execute the script
```
python3 main.py
```
4. To exit the program, type `no` or `n`:
x
