# To-Do List Application

## Overview

This is a simple command-line To-Do List application written in Python. It allows you to add tasks, remove tasks, view all tasks, and quit the application. The tasks are stored in a Python list and managed through a text-based interface.

## Features

- **Add Tasks:** Users can add new tasks to the list. The application prevents adding empty tasks and duplicates.
- **Remove Tasks:** Users can remove existing tasks from the list. If a task does not exist, the user is alerted.
- **View Tasks:** Users can view all tasks in the To-Do List. If there are no tasks, a message indicates that the list is empty.
- **Quit:** Users can exit the application.

## Input Validation and Error Handling

- The application uses `try`/`except` blocks to handle unexpected errors.
- If the user inputs invalid menu choices (not a number or out of range), the application alerts the user and re-prompts for input.
- If the user attempts to remove a task that doesn't exist or add a duplicate/empty task, the application alerts them accordingly.

## Getting Started
   
1. **Running the Application:**
   - Save the code in a file named `toDoApplication.py` (or any name you prefer).
   - Open a terminal or command prompt in the directory containing `toDoApplication.py`.
   - Run the application by typing:
     ```bash
     python toDoApplication.py
     ```
   
2. **Usage:**
   - Once the menu is displayed:
     - Enter `1` to add a task.
     - Enter `2` to remove a task.
     - Enter `3` to view tasks.
     - Enter `4` to quit the application.
   - Follow the on-screen instructions for adding, removing, and viewing tasks.
