# Nested Conditional Statements
# This program checks if a number is positive, negative, or zero, 
# and for positive numbers, also determines if it is even or odd.

num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
    
    # Nested if to check even or odd
    if num % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
        
elif num < 0:
    print("The number is negative.")
    
else:
    print("The number is zero.")

