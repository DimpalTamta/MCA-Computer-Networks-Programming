
# -------------------------------------------------------
# EXAMPLES OF FUNCTIONS IN PYTHON
# -------------------------------------------------------

# Example 1: Temperature Conversion
def convert_temperature(temp, unit):
    """Converts temperature between Celsius and Fahrenheit."""
    if unit == 'C':
        return temp * 9/5 + 32     # Celsius to Fahrenheit
    elif unit == 'F':
        return (temp - 32) * 5/9   # Fahrenheit to Celsius
    else:
        return None
print(convert_temperature(25, 'C'))
print(convert_temperature(77, 'F'))


# Example 2: Password Strength Checker
def is_strong_password(password):
    """Checks if the password is strong."""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+' for char in password):
        return False
    return True
print(is_strong_password("WeakPwd"))
print(is_strong_password("Str0ngPwd!"))


# Example 3: Calculate Total Cost in a Shopping Cart
def calculate_total_cost(cart):
    """Calculates total cost based on item price and quantity."""
    total_cost = 0
    for item in cart:
        total_cost += item['price'] * item['quantity']
    return total_cost
cart = [
    {'name': 'Apple', 'price': 0.5, 'quantity': 4},
    {'name': 'Banana', 'price': 0.3, 'quantity': 6},
    {'name': 'Orange', 'price': 0.7, 'quantity': 3}
]

print(calculate_total_cost(cart))


# Example 4: Check if a String is Palindrome
def is_palindrome(s):
    """Checks if a string reads the same forward and backward."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]
print(is_palindrome("A man a plan a canal Panama"))
print(is_palindrome("Hello"))


# Example 5: Factorial using Recursion
def factorial(n):
    """Calculates factorial of a number using recursion."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(6))


# Example 6: Word Frequency Counter
def count_word_frequency(file_path):
    """Reads a file and counts frequency of each word."""
    word_count = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower().strip('.,!?;:"\'')
                word_count[word] = word_count.get(word, 0) + 1
    return word_count
# Simulated data (for demonstration)
sample_data = {
    'this': 2, 'is': 3, 'a': 2, 'sample': 1,
    'text': 1, 'file': 1, 'with': 1, 'some': 1, 'words': 1
}
print(sample_data)


# Example 7: Validate Email Address
import re
def is_valid_email(email):
    """Validates if an email address format is correct."""
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

print(is_valid_email("test@example.com"))
print(is_valid_email("invalid-email"))


