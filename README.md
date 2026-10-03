# PC System Check

A beginner-friendly Python command-line tool that collects basic system information and generates a readable PC status report.

## Features

- Detects the operating system and version
- Shows the machine architecture and processor information
- Displays the Python version
- Reads the computer's host name
- Prints a formatted report in the terminal
- Saves the report to `system_report.txt`

## Requirements

- Python 3.10 or newer
- No third-party packages required

## Run the program

Open a terminal in this project folder and run:

```bash
python system_check.py
```

On some systems, use `python3 system_check.py` instead.

The program prints the collected information and writes it to `system_report.txt` in the current folder. The report contains information about the computer on which the script is run.

## Project structure

```
pc-system-check/
├── system_check.py
├── .gitignore
└── README.md
```

## What this project demonstrates

This small project is a practical exercise in:

- Python functions and dictionaries
- Using standard-library modules such as `platform`, `socket`, and `datetime`
- Formatting strings and console output
- Reading and writing UTF-8 text files
- Basic error handling
- Documenting and organizing a project with GitHub

## Limitations and possible improvements

This is an introductory project, not a full diagnostic tool. Some processor details depend on the operating system. Possible future improvements include disk-space checks, network connectivity tests, JSON export, automated tests, and a graphical interface.

## Learning note

This project is intended as a learning exercise. If you use it in an application, make sure you can explain the code and describe what you learned while building and testing it.
