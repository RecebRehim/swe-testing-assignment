# Quick-Calc

Quick-Calc is a simple calculator application that performs basic arithmetic operations including addition, subtraction, multiplication, and division. The application is designed as part of a software testing assignment and focuses on clean code, version control, and proper testing practices.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Division by zero handling
- Clear function to reset results

---

# Setup Instructions

Clone the repository:

git clone https://github.com/RecebRehim/swe-testing-assignment.git

Navigate into the project folder:

cd swe-testing-assignment

Install dependencies:

pip install -r requirements.txt

---

# Running the Application

Run the calculator:

python quick_calc/cli.py

---

# Running Tests

Execute the test suite using:

pytest

or

python -m pytest

All tests should pass successfully.

---

# Testing Framework Research

Two of the most popular Python testing frameworks are **Unittest** and **Pytest**.

Unittest is Python's built-in testing framework. It was modeled after JUnit of Java and offers a straightforward way to write test cases. It also supports test discovery, fixtures, and composing test suites. However, it requires more boilerplate code and its syntax is a bit outdated compared to more recent frameworks.

Pytest is a third-party testing framework that has gained wide acceptance among developers because of its easy-to-use and highly customizable nature. It allows writing test with only few lines of code and offers powerful features like fixtures, parameterized testing, and very detailed failure reports. Besides, it finds test modules automatically so there is no need for complex setup.

The reason for choosing **Pytest** in this project was the fact that it has a simple and clean syntax, it finds tests automatically, and it is well, equipped for writing tests that are easy to read and maintain.
