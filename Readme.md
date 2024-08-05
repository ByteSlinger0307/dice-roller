# Dice Roller

A simple Python program to simulate rolling a dice. This project is designed for beginners to practice using loops, conditionals, and the `random` module in Python.

## Features

- Simulates rolling a standard six-sided dice.
- Asks the user if they want to roll the dice again.
- Continues rolling the dice until the user chooses to stop.

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/ByteSlinger0307/dice-roller.git
    ```

2. Navigate to the project directory:
    ```bash
    cd dice-roller
    ```

3. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/).

## Usage

1. Run the Python script:
    ```bash
    python dice_roller.py
    ```

2. Follow the on-screen prompts to roll the dice and decide if you want to roll again.

## Code Overview

- `import random`: Imports the `random` module to generate random numbers.
- `while True`: Starts an infinite loop to repeatedly roll the dice.
- `random.randint(1, 6)`: Generates a random number between 1 and 6 to simulate a dice roll.
- `input("Do you want to roll the dice again? (Y/N): ")`: Prompts the user for input.
- `if roll_again.lower() == "y"`: Checks if the user wants to roll again.
- `continue`: Rolls the dice again if the user inputs "Y".
- `break`: Exits the loop if the user inputs anything other than "Y".

## Contributing

Feel free to fork the repository and submit pull requests with improvements or bug fixes. For any questions or suggestions, open an issue or contact me directly.

## Contact

- **Name**: Krish Dubey
- **Email**: dubeykrish0208@gmail.com
- **GitHub**: (https://github.com/ByteSlinger0307)

