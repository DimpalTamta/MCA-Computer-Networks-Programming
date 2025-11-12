# -------------------------------------------------------
# MAP() FUNCTION EXAMPLES
# -------------------------------------------------------

# Example 1: Square of a Number (Traditional Function)
def square(x):
    return x * x

print(square(10))

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(square, numbers)))


# Example 2: Lambda Function with map()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(lambda x: x * x, numbers)))


# Example 3: map() with Multiple Iterables
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

added_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
print(added_numbers)


# Example 4: map() to Convert List of Strings to Integers
str_numbers = ['1', '2', '3', '4', '5']
int_numbers = list(map(int, str_numbers))
print(int_numbers)


# Example 5: map() to Convert Strings to Uppercase
words = ['apple', 'banana', 'cherry']
upper_word = list(map(str.upper, words))
print(upper_word)


# Example 6: map() with Custom Function to Extract Names
def get_name(person):
    return person['name']

people = [
    {'name': 'Dimpal', 'age': 37},
    {'name': 'Jack', 'age': 33}
]

print(list(map(get_name, people)))
