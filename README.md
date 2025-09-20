# 📘 Calculator Project with Automated Tests

## 📌 Overview
This project is a **simple calculator application in Python** that supports basic arithmetic operations:

- ➕ Addition  
- ➖ Subtraction  
- ✖️ Multiplication  
- ➗ Division  

It includes **automated tests** using `pytest` and a **CI/CD pipeline** with GitHub Actions to ensure code quality and correctness.

---

## 🚀 Features
- Command-line interface (REPL style)  
- Handles negative numbers (e.g., `-5 * -3`)  
- Automated testing with `pytest`  
- Code coverage reports with `pytest-cov`  
- Continuous Integration via GitHub Actions  

---

## 🛠️ Project Structure
```text
assignment-2/
│── app/
│   ├── __init__.py
│   ├── calculator/
│   │   └── __init__.py     # Calculator class (add, subtract, multiply, divide)
│   └── operations/
│       └── __init__.py     # (optional: reusable operation functions)
│── tests/
│   └── test_calculator.py
│── main.py                 # REPL entry point
│── pytest.ini              # Pytest configuration
│── requirements.txt        # Project dependencies
│── .github/workflows/
│   └── python-app.yml      # GitHub Actions workflow
```

---

## ▶️ Usage
Run the program:
```bash
python main.py
```

Enter expressions in the format:
```text
number operator number
```

✅ Valid examples:
```text
5 + 3
-5 * -3
10 / 2
```

❌ Invalid (no spaces):
```text
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

Then open:
```text
htmlcov/index.html
```
in your browser.

---

## ⚙️ Continuous Integration
This project uses **GitHub Actions** for CI:

- Runs tests automatically on every push  
- Verifies code quality with `pytest` and `pytest-pylint`  
- Ensures coverage is reported  

👉 View CI results here: [GitHub Actions](https://github.com/techy-Nik/assignment-2/actions)

---

## 🎯 Learning Outcomes
This project demonstrates:

- ✅ Writing Python applications with automated testing (CLO3)  
- ✅ Setting up GitHub Actions for CI/CD (CLO4)  
- ✅ Building a command-line REPL application (CLO5)  
