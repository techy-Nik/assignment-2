📘 Calculator Project with Automated Tests
🎯 Objective

This project is a simple Python calculator application that supports addition, subtraction, multiplication, and division.
It includes automated testing with pytest, code coverage reports, and continuous integration using GitHub Actions.

📂 Project Structure
assignment2/
│── app/
│   ├── __init__.py
│   ├── calculator/
│   │   └── __init__.py     # Calculator functions
│   ├── operations/
│   │   └── __init__.py
│
├── tests/
│   ├── __init__.py
│   └── test_calculator.py  # Unit tests
│
├── main.py                 # REPL command-line calculator
├── requirements.txt        # Dependencies
├── pytest.ini              # Pytest configuration
├── .coveragerc             # Coverage configuration
└── .github/
    └── workflows/
        └── python-app.yml  # GitHub Actions CI

⚙️ Installation & Setup

Clone the repo

git clone <your-repo-url>
cd assignment2


Create virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt

▶️ Usage (REPL Calculator)

Run:

python main.py


Example session:

Simple Calculator (type 'exit' to quit)
Enter expression (e.g. 2 + 3): -5 + 3
-2.0
Enter expression (e.g. 2 + 3): -5 * -3
15.0
Enter expression (e.g. 2 + 3): exit


⚠️ Note: Inputs must include spaces between numbers and operators (e.g. -5 * -3 ✅, not -5*-3 ❌).

✅ Testing

Run all tests:

pytest


This will:

Run unit tests

Check linting (pytest-pylint)

Generate coverage reports

To view HTML coverage report:

pytest --cov=app --cov-report=html
open htmlcov/index.html  # Linux/Mac
start htmlcov/index.html # Windows

🔄 Continuous Integration (CI)

This project uses GitHub Actions for CI:

On each push, tests and linting run automatically.

Coverage is reported in the workflow logs.

🎓 Learning Outcomes

Created Python application with automated testing (CLO3).

Configured GitHub Actions for Continuous Integration (CLO4).

Developed a REPL command-line calculator (CLO5).