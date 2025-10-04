## Python Operators Deep Dive

# -------------------------------
# Arithmetic Operators
# -------------------------------
print("### Arithmetic Operators ###")

a = 10
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)          # True division
print("Floor Division:", a // b)   # Rounds down to nearest integer
print("Modulus:", a % b)           # Remainder
print("Exponentiation:", a ** b)   # Power

# -------------------------------
# Comparison Operators
# -------------------------------
print("\n### Comparison Operators ###")

x = 10
y = 20

print("Equal to (x == y):", x == y)
print("Not equal to (x != y):", x != y)
print("Greater than (x > y):", x > y)
print("Less than (x < y):", x < y)
print("Greater than or equal to (x >= y):", x >= y)
print("Less than or equal to (x <= y):", x <= y)

# String comparison
str1 = "Python"
str2 = "Python"
str3 = "python"

print("String equal:", str1 == str2)
print("String not equal:", str1 != str3)

# -------------------------------
# Logical Operators
# -------------------------------
print("\n### Logical Operators ###")

A = True
B = False

print("A AND B:", A and B)
print("A OR B:", A or B)
print("NOT A:", not A)

# -------------------------------
# Simple Calculator
# -------------------------------
print("\n### Simple Calculator ###")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
floor_division = num1 // num2
modulus = num1 % num2
exponentiation = num1 ** num2

print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)
