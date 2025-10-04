# If-Else Statement Example with User Input

# Definition: An if-else statement allows you to execute one block of code 
# if the condition is True, and another block if the condition is False.

# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check if the user is eligible to vote
if age >= 18:
    # Executes if the condition is True
    print("You are allowed to vote in the elections")
else:
    # Executes if the condition is False
    print("You are not allowed to vote yet. Wait for a few more years!")
