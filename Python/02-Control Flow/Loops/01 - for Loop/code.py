# -------------------------------
# For Loop in Python
# -------------------------------
# Definition: 
# A for loop is used to iterate (repeat) over a sequence such as a range of numbers, 
# a string, or a list, executing a block of code for each item in that sequence.

# Example 1: Iterating over a range (0 to 4)
print("\n========== Example 1: Iterating from 0 to 4 ==========")
for i in range(5):
    print(i)

# Example 2: Iterating over a range with start and end (1 to 5)
print("\n========== Example 2: Iterating from 1 to 5 ==========")
for i in range(1, 6):
    print(i)

# Example 3: Iterating with a step (odd numbers from 1 to 9)
print("\n========== Example 3: Iterating with step size (1 to 9, step 2) ==========")
for i in range(1, 10, 2):
    print(i)

# Example 4: Iterating backwards (10 down to 2)
print("\n========== Example 4: Iterating backwards from 10 to 2 ==========")
for i in range(10, 1, -1):
    print(i)

# Example 5: Iterating backwards with step size (10 down to 2, step -2)
print("\n========== Example 5: Iterating backwards with step size ==========")
for i in range(10, 1, -2):
    print(i)

# Example 6: Iterating over a string
print("\n========== Example 6: Iterating over each character in a string ==========")
text = "Dimpal Tamta"
for char in text:
    print(char)
