# PythonTicTacToe
 This Python project implements a Tic-Tac-Toe game where two players take turns placing their respective symbols (X and O) on a grid. The game allows for different grid sizes (3x3, 4x4, or 5x5) and supports the standard win conditions: a player wins if they place three consecutive pieces horizontally, vertically, or diagonally.  The game includes features such as:  A customizable game board size (default is 3x3). Win detection through various directions (rows, columns, diagonals). A hint system to help players identify potential winning moves. Functions that determine if the board is full and check if a player has won. A graphical interface using SimpleGraphics for rendering the board and managing player interactions.

# Python Tic-Tac-Toe Game

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Credits](#credits)

## Introduction
This project is a Python implementation of the classic Tic-Tac-Toe (or Noughts and Crosses) game. The game allows two players to take turns placing either an X or an O on a customizable board of size 3x3, 4x4, or 5x5. The first player to get three pieces in a row wins the game. The project features a graphical interface to visualize the game board.

## Features
- Customizable board size (3x3, 4x4, 5x5).
- Win condition checking (horizontal, vertical, and diagonal).
- A hint system to suggest potential winning moves.
- Graphical interface using `SimpleGraphics`.
- Game logic functions for handling moves, checking wins, and determining if the board is full.

## Installation
1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    ```
2. **Install the required dependencies**:
    The game uses the `SimpleGraphics` library. To install it:
    ```bash
    pip install simplegraphics
    ```
3. **Run the game**:
    Once installed, you can run the game by executing the main Python script:
    ```bash
    python CPSC217W23A3Game.py
    ```

## Usage
1. Run the game by executing the main script. You will be prompted to choose a board size.
2. Players take turns entering the row and column numbers to place their pieces.
3. The game will indicate when a player wins or if the board is full with no winner.
4. You can use the hint function to get a suggestion for your next move.

## Game Rules
- Players take turns placing their pieces (X or O) on an empty square.
- A player wins if they place three of their pieces consecutively in a row, column, or diagonal.
- The game ends when a player wins or the board is full with no winner.

## Credits
- **Student**: Ibuchi Jahnissi Nwakanma
- **Instructor**: Jonathan Hudson
- **Course**: CPSC 217 Winter 2023

