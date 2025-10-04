## Python Data Types Deep Dive

# -------------------------------
# Basic Data Types
# -------------------------------

print("### Basic Data Types ###")

# Integer
age = 35
print("Integer:", age, "| Type:", type(age))

# Float
height = 5.11
print("Float:", height, "| Type:", type(height))

# String
name = "Dimpal"
print("String:", name, "| Type:", type(name))

# Boolean
is_student = True
print("Boolean:", is_student, "| Type:", type(is_student))

# Boolean from comparison
a = 10
b = 10
print("Result of comparison (a==b):", a == b, "| Type:", type(a == b))

# -------------------------------
# Type Conversion
# -------------------------------

print("\n### Type Conversion ###")

num_str = "100"
num_int = int(num_str)       # string to int
num_float = float(num_str)   # string to float

print("String to int:", num_int, "| Type:", type(num_int))
print("String to float:", num_float, "| Type:", type(num_float))

# int to string
age_str = str(age)
print("Int to String:", age_str, "| Type:", type(age_str))

# float to int
height_int = int(height)
print("Float to Int:", height_int, "| Type:", type(height_int))

# -------------------------------
# Common Errors
# -------------------------------

print("\n### Common Errors ###")

try:
    result = "Hello" + 5  # TypeError
except TypeError as e:
    print("Error:", e)

# Fix with type conversion
result = "Hello" + str(5)
print("Fixed Concatenation:", result)

# -------------------------------
# Practical Examples
# -------------------------------

print("\n### Practical Examples ###")

# Checking length of a string
print("Length of name:", len(name))

# -------------------------------
# Optional Examples for Lists/Sets/Dicts
# -------------------------------

fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])

unique_numbers = {1, 2, 3}
print("Is 2 in set?", 2 in unique_numbers)

student = {"name": "Dimpal", "age": 22, "grade": "A"}
print("Student name:", student["name"])
