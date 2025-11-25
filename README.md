Python Flashcard App 

A simple, command-line interface (CLI) application built in Python to help users study and memorize information using digital flashcards.
This program allows the user to create, review, and quiz yourself using digital flashcards—right from the terminal.

Features

Create Custom Cards: Add your own Question and Answer pairs to the deck.

Quiz Mode: Test your knowledge! The app presents questions in a random order to ensure you aren't just memorizing the sequence.

Hidden Answers: Answers are concealed until you press 'Enter', giving you time to think.

Session Storage: Cards are stored in a temporary dictionary while the program is running.

Requirements
Python 3.x installed on your machine.

How to Run

Download the script: Save the Python code into a file named flash.py.

Open Terminal: Navigate to the folder containing the file using your command prompt or terminal.

Execute: Run the following command:

python flashcards.py


Usage Guide

Once the program starts, you will see a menu with three options:

Add a new flashcard:  Type 1 and press Enter.

Type your Question (e.g., "What is the capital of India?").

Type the Answer (e.g., " New Delhi").

Take the quiz:

Type 2 and press Enter.

The program will shuffle your existing cards and show them one by one.

Press Enter to reveal the answer for the current card.

Exit:

Type 3 to close the application.

 Code Overview

The program utilizes the following Python concepts:

Dictionaries ({}): Used as the primary data structure to map questions (keys) to answers (values).

random Module: specifically random.shuffle(), to mix up the order of questions during the quiz.

while Loop: Keeps the application running until the user explicitly chooses to exit.


Future Improvements

Spaced repetition algorithm (SM-2)
GUI using Tkinter/PyQt
Import/export CSV
Multiple-choice quiz mode
Stats dashboard
Categories: Group flashcards by subject (e.g., Math, Science).
Score Keeping: Track how many answers the user gets right.
