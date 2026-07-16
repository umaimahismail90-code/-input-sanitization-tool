## 🧹 Robust Input Data Cleaner

A lightweight Python command-line utility designed to accept continuous user input, handle exceptions gracefully, and output a clean, filtered dataset of positive integers.

### Features
* **Active Exception Handling:** Uses `try-except` blocks to prevent crashes when processing non-numeric data types (like letters or symbols).
* **Interactive CLI Loop:** Employs a `while` loop that allows for continuous data processing until the user chooses to exit.
* **Data Transformation:** Safely converts raw, space-separated string inputs into structured lists of positive integers.

### How It Works
The program runs in a continuous loop, prompting the user for input until they type `'done'`. It iterates through the provided values, safely attempts to cast each item to an integer, filters out any negative numbers, and skips invalid inputs entirely without crashing the application.
