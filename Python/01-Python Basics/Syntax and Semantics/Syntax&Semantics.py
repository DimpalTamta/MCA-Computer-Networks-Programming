## Syntax and Semantics in Python

# Single-line comment
print("Hello World")  # prints Hello World

"""
This is a multiline comment.
It can span across multiple lines.
Used to explain code in detail.
"""

# Case sensitivity
name = "Dimpal"
Name = "Tamta"
print(name)   # prints Alice
print(Name)   # prints Bob

# Indentation
age = 25
if age > 20:
    print("Age is greater than 20")

# Line continuation
total = 1 + 2 + 3 + \
        4 + 5
print("Total:", total)

# Multiple statements in one line
x = 5; y = 10; print("Sum:", x + y)

# Semantics (meaning of variables)
age = 30
name = "Alice"
print("Age:", age, "| Name:", name)

# Type inference
var = 100
print(type(var))   # int
var = "Now a string"
print(type(var))   # str

# Common error example
try:
    print(unknown_variable)   # not defined
except NameError as e:
    print("Error:", e)
