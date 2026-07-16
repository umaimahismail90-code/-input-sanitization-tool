# Robust Input Data Cleaner

A lightweight Python command-line utility designed to accept dynamic user input, handle exceptions gracefully, and output a clean dataset of positive integers.

## Features
* **Active Exception Handling:** Uses `try-except` blocks to prevent crashes when processing non-numeric data types (like letters or symbols).
* **Dynamic User Input:** Employs `input().split()` to capture and parse live user data on the fly.
* **Data Transformation:** Converts raw string inputs into clean integer lists.

## How It Works
The program prompts the user for a list of values separated by spaces. It iterates through the input, safely attempts to cast each item to an integer, filters out any negative numbers, and skips invalid strings entirely without raising a fatal error.

## Code Preview
```python
# Insert your data_cleaner code here!
