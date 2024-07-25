# calc.py
# by Victor Sório

operations = {
    "plus": lambda x, y: x + y, 
    "minus": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y,
    "exponentiation": lambda x, y: x ** y,
    "root": lambda x, y: x ** (1 / y),
}

print("calc.py")

cmd = "continue"
while cmd == "continue": 
    print("---------------------")
    print("Give me a number:")
    x = float(input())
    print("Give me an operation:\nOptions: 'plus', 'minus', 'multiply', 'divide', 'exponentiation', 'root'")
    op = str(input())
    print("Give me a second number:")
    y = float(input())

    r = operations[op](x, y)
    print(f"Result: {r:.2f}")
    print("Continue? y/n")
    if str(input()) == "n":
        cmd = "break"
        print("Bye!")