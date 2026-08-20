# Number Guessing Game

A Python command-line game where the computer randomly selects a number between 1 and 100, and the player keeps guessing until they find the correct number.

## Features

* Generates a random number between 1 and 100
* Accepts guesses from the user
* Tells the player if the guess is:

  * Too high
  * Too low
  * Correct
* Continues asking for guesses until the correct number is found

## Technologies Used

* Python 3
* Python `random` module

##  How to Run

Make sure Python 3 is installed.

Open a terminal in the project directory and run:

```bash
python guessing_game.py
```

On some systems:

```bash
python3 guessing_game.py
```

## Example

```text
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too high!

Enter your guess: 25
Too low!

Enter your guess: 37
Too high!

Enter your guess: 32
Correct! 
```

## Project Structure

```text
Number-Guessing-Game/
├── guessing_game.py
└── Readme.md
```

## Learning Objectives

This project was created to practice:

* Variables
* User input
* Type conversion
* `if`, `elif`, and `else`
* `while` loops
* Comparison operators
* Random number generation
* The `random` module
* Loop control and program flow