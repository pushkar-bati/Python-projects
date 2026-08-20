# Scientific Calculator

A Python-based command-line scientific calculator that performs basic arithmetic and selected scientific operations.

##  Features

### Basic Operations

* Addition (`+`)
* Subtraction (`-`)
* Multiplication (`*`)
* Division (`/`)
* Modulus (`%`)
* Power (`**`)
* Floor Division (`//`)

### Scientific Operations

* Square Root (`sqrt`)
* Square (`square`)
* Cube (`cube`)
* Factorial (`factorial`)
* Pi (`pi`)
* Euler's Number (`e`)

### Error Handling

* Prevents division by zero
* Validates square-root input
* Validates factorial input
* Handles invalid operations

## Technologies Used

* Python 3
* Python `math` module

## ▶ How to Run

Make sure Python 3 is installed.

Open a terminal in the project directory and run:

```bash
python calculator.py
```

On some systems, you may need:

```bash
python3 calculator.py
```

## Example

### Addition

```text
Enter the operation: +
Enter the first number: 10
Enter the second number: 20
Result: 30.0
```

### Square Root

```text
Enter the operation: sqrt
Enter the number: 25
Result: 5.0
```

### Factorial

```text
Enter the operation: factorial
Enter the number: 5
Result: 120
```

### Pi

```text
Enter the operation: pi
Result: 3.141592653589793
```

## Project Structure

```text
Calculator/
├── calculator.py
├── README.md
└── .gitignore
```

##  Learning Objectives

This project was created to practice fundamental Python programming concepts, including:

* Variables
* User input
* Type conversion
* Conditional statements
* `if`, `elif`, and `else`
* Arithmetic operators
* The `math` module
* Exception handling
* Input validation
* Boolean conditions
* Basic program structure

##  Future Improvements

Possible future improvements include:

* Trigonometric functions
* Logarithmic functions
* Calculation history
* Continuous calculation mode
* GUI interface
* Automated testing
