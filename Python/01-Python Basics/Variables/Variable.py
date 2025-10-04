# A variable is a container used to store data that can be referenced and modified in a program.
# ----------------------
# Python Variables Demonstration
# Author: Dimpal
# ----------------------

# ----------------------
# Declaring Variables
# ----------------------
age = 25          # integer
height = 5.9      # float
name = "Dimpal"   # string
is_student = True # boolean

print("### Variables ###")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Name: {name}")
print(f"Is Student: {is_student}\n")

# ----------------------
# Type Check
# ----------------------
print("### Type Check ###")
print(f"Type of Age: {type(age)}")
print(f"Type of Height: {type(height)}")
print(f"Type of Name: {type(name)}")
print(f"Type of Is Student: {type(is_student)}\n")

# ----------------------
# Type Conversion
# ----------------------
print("### Type Conversion ###")
age_str = str(age)
print(f"Age as string: {age_str} | Type: {type(age_str)}")

height_str = "6.1"
height_float = float(height_str)
print(f"Height as float: {height_float} | Type: {type(height_float)}\n")

# ----------------------
# Dynamic Typing
# ----------------------
print("### Dynamic Typing ###")
var = 10
print(f"Var: {var} | Type: {type(var)}")

var = "Hello"
print(f"Var: {var} | Type: {type(var)}")

var = 3.14
print(f"Var: {var} | Type: {type(var)}")
