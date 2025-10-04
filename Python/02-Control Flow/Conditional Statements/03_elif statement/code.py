
# Elif Statement Example with User Input

# Definition: The elif statement allows you to check multiple conditions. 
# It stands for "else if". Only the first True condition block executes.

# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check multiple conditions
if age < 13:
    # Executes if age is less than 13
    print("You are a child")
elif age < 18:
    # Executes if previous condition was False and age is less than 18
    print("You are a teenager")
else:
    # Executes if all previous conditions were False
    print("You are an adult")
