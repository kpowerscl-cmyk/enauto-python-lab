# ENAUTO Python Lab

A hands-on Python, Linux, and network automation learning project built on a dedicated Raspberry Pi while preparing for the Cisco ENAUTO concentration exam.

This repository documents my progression from basic Python syntax to reusable modules, system-information functions, Git, GitHub, APIs, and network automation.

## Purpose

The purpose of this lab is to learn automation by building and troubleshooting working code rather than only studying theory.

Each lesson captures:

- The concept being learned
- The Python code used to practice it
- Errors encountered during development
- The reasoning behind each correction
- How the concept applies to network automation

## Lab Platform

- Raspberry Pi
- Raspberry Pi OS Lite / Debian 13
- ARM64 architecture
- Python 3
- Python virtual environment
- Git and GitHub
- SSH administration

Machine-specific values and private lab information are sanitized before publication.

## Lesson Progression

| File | Primary concept |
|---|---|
| `hello.py` | Sequential execution and basic output |
| `lesson1.py` | Variables and Python data types |
| `lesson2.py` | Device-information variables |
| `lesson3.py` | Structured device-information output |
| `lesson4.py` | Conditional logic |
| `lesson5.py` | Functions and parameters |
| `lesson6.py` | Dynamic Linux system information |
| `lesson7.py` | Organizing execution with `main()` |
| `lesson8.py` | The `__name__ == "__main__"` guard |
| `controller.py` | Imports, returned values, and module reuse |

## Documentation

The `docs/` directory contains written lesson guides covering the lab setup, troubleshooting process, and supporting Linux and Git concepts.

### Current documentation
- Lesson 01: Command Reference
- Lesson 01: Raspberry Pi and Python Fundamentals
- Lesson 02: Python Foundations
- Lesson 06: Raspberry Pi Health Check
- Lesson 07-08: 'Main()', imports, and controller review
- Lesson 09: Modules, Controller, and Return Values
- Lesson 10: Pi File Cleanup for Git
- Lesson 11: Git and GitHub Fundamentals - in progress

### Documentation gaps

- Lesson 03: Structured Device Information - PDF pending
- Lesson 04: Conditional logic - PDF pending
- Lesson 05: Functions and Parameters - PDF pending

## Project Structure

```text
enauto-python-lab/
├── .gitignore
├── README.md
├── docs/
└── lessons/
    ├── controller.py
    ├── hello.py
    ├── lesson1.py
    ├── lesson2.py
    ├── lesson3.py
    ├── lesson4.py
    ├── lesson5.py
    ├── lesson6.py
    ├── lesson7.py
    └── lesson8.py
