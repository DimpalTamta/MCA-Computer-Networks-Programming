# -------------------------------------------------------
# FILTER() FUNCTION EXAMPLES
# -------------------------------------------------------

# Example 1: Filter Even Numbers (Traditional Function)
def even(num):
    if num % 2 == 0:
        return True

even(24)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list(filter(even, lst)))


# Example 2: filter() with a Lambda Function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)


# Example 3: filter() with Lambda and Multiple Conditions
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_and_greater_than_five = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print(even_and_greater_than_five)


# Example 4: filter() on a List of Dictionaries (Age > 25)
people = [
    {'name': 'Dimpal', 'age': 32},
    {'name': 'Jack', 'age': 33},
    {'name': 'John', 'age': 25}
]

def age_greater_than_25(person):
    return person['age'] > 25

print(list(filter(age_greater_than_25, people)))

