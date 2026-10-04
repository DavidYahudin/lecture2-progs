import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid input value")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Cannot devide to zero")
    sys.exit(1)

print(f"{x} / {y} = {result}")
