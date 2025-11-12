## Introduction to Functions
## Definition: A function is a block of code that performs a specific task.
## syntax
"""
def function_name(parameters):
    """Docstring"""
    # Function body
    return expression
"""

# -----------------------------
# Function to check even or odd
# -----------------------------
def even_or_odd(num): 
    """This function finds whether a number is even or odd"""
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

# Example call
even_or_odd(24)


# ----------------------------------
# Function with multiple parameters
# ----------------------------------
def add(a, b):
    return a + b

# Example call
result = add(2, 4)
print(result)


# ------------------------------
# Function with default parameter
# ------------------------------
def greet(name="Dimpal"):
    print(f"Hello {name}, Welcome to the paradise!")

# Example call
greet()


# ----------------------------------------------
# Variable Length Arguments (Positional Arguments)
# ----------------------------------------------
def print_numbers(*args):
    for number in args:
        print(number)

# Example calls
print_numbers(1, 2, 3, 4, 5, 6, 7, 8, "Dimpal")
print_numbers("This", "is", "a", "sentence", "from", "Dimpal")


# ---------------------
# Keyword Arguments
# ---------------------
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example call
print_details(name="Dimpal", age="25", country="India")


# ----------------------------------------------------
# Combined Positional and Keyword Arguments
# ----------------------------------------------------
def print_details_mix(*args, **kwargs):
    for val in args:
        print(f"Positional argument: {val}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example call
print_details_mix(1, 2, 3, 4, "Dimpal", name="Dimpal", age="25", country="India")


# -----------------------------
# Function with a return statement
# -----------------------------
def multiply(a, b):
    return a * b

# Example call
print(multiply(2, 3))


# ----------------------------------
# Function returning multiple values
# ----------------------------------
def multiply_multi(a, b):
    return a * b, a

# Example call
print(multiply_multi(2, 3))








