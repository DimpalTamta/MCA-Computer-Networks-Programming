## Python Data Types (With Advanced Data Types)

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
is_true = True
print("Boolean:", is_true, "| Type:", type(is_true))

# Boolean from comparison
a = 10
b = 10
print("Result of comparison (a==b):", a == b, "| Type:", type(a == b))

# -------------------------------
# Type Conversion
# -------------------------------
print("\n### Type Conversion ###")

# String to int and float
num_str = "100"
num_int = int(num_str)
num_float = float(num_str)
print("String to int:", num_int, "| Type:", type(num_int))
print("String to float:", num_float, "| Type:", type(num_float))

# Int to string
age_str = str(age)
print("Int to string:", age_str, "| Type:", type(age_str))

# Float to int
height_int = int(height)
print("Float to int:", height_int, "| Type:", type(height_int))

# -------------------------------
# Common Errors
# -------------------------------
print("\n### Common Errors ###")
try:
    result = "Hello" + 5  # This will cause TypeError
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
# Advanced Data Types
# -------------------------------
print("\n### Advanced Data Types ###")

# List
fruits = ["apple", "banana", "cherry"]
print("List:", fruits, "| Type:", type(fruits))
print("First fruit:", fruits[0])

# Tuple
coordinates = (10.5, 20.3)
print("Tuple:", coordinates, "| Type:", type(coordinates))
print("X coordinate:", coordinates[0])

# Set
unique_numbers = {1, 2, 3, 2, 1}
print("Set:", unique_numbers, "| Type:", type(unique_numbers))
print("Is 2 in set?", 2 in unique_numbers)

# Dictionary
student = {"name": "Dimpal", "age": 22, "grade": "A"}
print("Dictionary:", student, "| Type:", type(student))
print("Student name:", student["name"])
print("Student age:", student["age"])

# -------------------------------
# End of Data Types Script
# -------------------------------
print("\n### End of Script ###")
