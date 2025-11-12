# -------------------------------------------------------
# LAMBDA FUNCTION EXAMPLES
# -------------------------------------------------------

# Syntax:
# lambda arguments: expression


# Example 1: Addition (Traditional Function)
def addition(a, b):
    return a + b

# Traditional function call
addition(2, 3)

# Lambda version
addition = lambda a, b: a + b
print(type(addition))
print(addition(5, 6))


# Example 2: Even Number Checker
# Traditional method
def even(num):
    if num % 2 == 0:
        return True

even(24)

# Lambda version
even1 = lambda num: num % 2 == 0
print(even1(12))


# Example 3: Addition with Three Numbers
# Traditional method
def addition(x, y, z):
    return x + y + z

addition(12, 13, 14)

# Lambda version
addition1 = lambda x, y, z: x + y + z
print(addition1(12, 13, 14))


# Example 4: Using map() with lambda
# map() applies a function to all items in a list

numbers = [1, 2, 3, 4, 5, 6]

# Traditional function
def square(number):
    return number ** 2

square(2)

# Using lambda with map
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)
