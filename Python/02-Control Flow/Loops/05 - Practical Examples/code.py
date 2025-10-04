# ================= Practical Examples =================
# Author: Dimpal
# Description: Demonstrating loops, nested loops, conditional examples, and patterns in Python.

# ------------------ 1. Sum of First N Natural Numbers ------------------
print("\n========== Sum of First N Natural Numbers ==========")
print("Definition: Calculate the sum of the first N natural numbers using loops.")

# Using while loop
n = 10
sum_while = 0
count = 1

while count <= n:
    sum_while += count
    count += 1

print("Sum of first 10 natural numbers (while loop):", sum_while)

# Using for loop
sum_for = 0
for i in range(1, n+1):
    sum_for += i

print("Sum of first 10 natural numbers (for loop):", sum_for)


# ------------------ 2. Prime Numbers Between 1 and 100 ------------------
print("\n========== Prime Numbers Between 1 and 100 ==========")
print("Definition: Print all prime numbers from 1 to 100 using nested loops.")

for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()  # for newline


# ------------------ 3. Factorial of a Number ------------------
print("\n========== Factorial Calculation ==========")
print("Definition: Calculate the factorial of a number using a for loop.")

num = 6
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"Factorial of {num} is {factorial}")


# ------------------ 4. Fibonacci Series ------------------
print("\n========== Fibonacci Series ==========")
print("Definition: Print the first N terms of the Fibonacci series using a while loop.")

terms = 10
a, b = 0, 1
count = 0

print(f"First {terms} terms of Fibonacci series:", end=" ")
while count < terms:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()


# ------------------ 5. Pattern Printing ------------------
print("\n========== Pattern Printing ==========")
print("Definition: Print a simple pattern using nested loops.")

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# ------------------ 6. Nested Loops Example ------------------
print("\n========== Nested Loops Example ==========")
print("Definition: Demonstrate nested loops by iterating two ranges.")

for i in range(3):
    for j in range(2):
        print(f"i: {i} and j: {j}")


# ------------------ 7. While Loop with Password Example ------------------
print("\n========== While Loop: Password Check ==========")
print("Definition: Demonstrate while loop for repeated user input until correct.")

password = "python123"
user_input = ""

while user_input != password:
    user_input = input("Enter the password: ")
    if user_input != password:
        print("Incorrect password, try again!")

print("Access Granted ✅")


# ------------------ 8. Sum of Even Numbers ------------------
print("\n========== Sum of Even Numbers Between 1 and 50 ==========")
print("Definition: Calculate the sum of even numbers using a for loop.")

sum_even = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum_even += i

print("Sum of even numbers from 1 to 50 is:", sum_even)
