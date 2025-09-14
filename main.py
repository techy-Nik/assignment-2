from app.calculator import addition, subtraction, multiplication, division

def repl():
    print("Simple Calculator (type 'exit' to quit)")
    while True:
        expr = input("Enter expression (e.g. 2 + 3): ")
        if expr.lower() == "exit":
            break
        try:
            a, op, b = expr.split()
            a, b = float(a), float(b)
            if op == '+':
                print(addition(a, b))
            elif op == '-':
                print(subtraction(a, b))
            elif op == '*':
                print(multiplication(a, b))
            elif op == '/':
                print(division(a, b))
            else:
                print("Invalid operator")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    repl()
