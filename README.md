## 📘 README.md 

```markdown
# 📘 Calculator Project with Automated Tests

[![Build Status](https://github.com/techy-Nik/assignment-2/actions/workflows/python-app.yml/badge.svg)](https://github.com/techy-Nik/assignment-2/actions)

## 📌 Overview
This project is a **simple calculator application in Python** that supports basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division  

The project includes **automated tests** using `pytest` and a **CI/CD pipeline** with GitHub Actions to ensure code quality and correctness.

---

## 🚀 Features
- Command-line interface (REPL style)
- Handles negative numbers (e.g., `-5 * -3`)
- Automated testing with `pytest`
- Code coverage reports with `pytest-cov`
- Continuous Integration via GitHub Actions

---

## 🛠️ Project Structure
```

assignment-2/
│── app/
│   ├── **init**.py
│   ├── calculator/
│   │   └── **init**.py   # Calculator class with add, subtract, multiply, divide
│   └── operations/
│       └── **init**.py   # (optional: reusable operation functions)
│── tests/
│   └── test\_calculator.py
│── main.py               # REPL entry point
│── pytest.ini            # Pytest configuration
│── requirements.txt      # Project dependencies
│── .github/workflows/
│   └── python-app.yml    # GitHub Actions workflow

````

---

## ▶️ Usage
1. Run the program:
   ```bash
   python main.py
````

2. Enter expressions in the format:

   ```
   number operator number
   ```

   ✅ Examples:

   ```
   5 + 3
   -5 * -3
   10 / 2
   ```

   ❌ Invalid (no spaces):

   ```
   2+-3
   ```

---

## 🧪 Running Tests

Run all tests with coverage:

```bash
pytest
```

Generate an HTML coverage report:

```bash
pytest --cov=app --cov-report=html
```

Then open `htmlcov/index.html` in your browser.

---

## ⚙️ Continuous Integration

This project uses **GitHub Actions** for CI:

* Runs tests automatically on every push
* Verifies code quality with `pytest` and `pytest-pylint`
* Ensures coverage is reported

You can view CI results here:
👉 [GitHub Actions](https://github.com/techy-Nik/assignment-2/actions)

---

## 🎯 Learning Outcomes

This project demonstrates:

* ✅ Writing Python applications with automated testing (CLO3)
* ✅ Setting up GitHub Actions for CI/CD (CLO4)
* ✅ Building a command-line REPL application (CLO5)


