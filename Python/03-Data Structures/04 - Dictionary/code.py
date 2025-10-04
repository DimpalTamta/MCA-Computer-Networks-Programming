# ===================== Dictionaries  =====================

# Dictionaries are unordered collections of items. They store data in key-value pairs.
# Keys must be unique and immutable (strings, numbers, tuples), values can be any type.

# Creating Dictionaries
empty_dict = {}
print("Empty dictionary using {}:", empty_dict)
print("Type of empty_dict:", type(empty_dict))  # <class 'dict'>

empty_dict = dict()
print("Empty dictionary using dict():", empty_dict)  # {}

student = {"name": "Dimpal", "age": 32, "grade": 24}
print("\nStudent dictionary:", student)
print("Type of student:", type(student))  # <class 'dict'>

# Single key uniqueness
student = {"name": "Dimpal", "age": 32, "name": 24}
print("\nDictionary with duplicate keys (last value kept):", student)  # {'name': 24, 'age': 32}

# Accessing Dictionary Elements
student = {"name": "Dimpal", "age": 32, "grade": 'A'}
print("\nAccess dictionary elements")
print("Student dictionary:", student)
print("Grade:", student['grade'])  # 'A'
print("Age:", student['age'])    # 32
print("Grade (using get()):", student.get('grade'))  # 'A'
print("Last Name (using get()):", student.get('last_name'))  # None
print("Last Name with default:", student.get('last_name', "Not Available"))  # 'Not Available'

# Modifying Dictionary Elements
print("\nModifying dictionary elements")
student["age"] = 33  # update value
print("Updated age:", student)
student["address"] = "India"  # add new key-value
print("Added address:", student)
del student['grade']  # delete key-value
print("Deleted grade:", student)

# Dictionary methods
print("\nDictionary methods")
keys = student.keys()
print("Keys:", keys)
values = student.values()
print("Values:", values)
items = student.items()
print("Items:", items)

# Shallow copy
student_copy = student
print("\nShallow copy (student_copy = student)")
print("Original student:", student)
print("Copy student_copy:", student_copy)

student["name"] = "Dimpal2"
print("\nAfter modifying original dictionary")
print("Original student:", student)
print("Copy student_copy:", student_copy)  # reflects change, shallow copy

student_copy1 = student.copy()  # shallow copy
print("\nShallow copy using copy() method")
print("student_copy1:", student_copy1)
print("Original student:", student)

student["name"] = "Dimpal3"
print("\nAfter modifying original again")
print("student_copy1 (unchanged):", student_copy1)
print("Original student:", student)

# Iterating Over Dictionaries
print("\nIterating over dictionaries")
for key in student.keys():
    print("Key:", key)
for value in student.values():
    print("Value:", value)
for key, value in student.items():
    print(f"{key}: {value}")

# Nested Dictionaries
students = {
    "student1": {"name": "Dimpal", "age": 32},
    "student2": {"name": "Rushaank", "age": 35}
}
print("\nNested dictionary:", students)

print("Access nested dictionary element - name:", students["student2"]["name"])
print("Access nested dictionary element - age:", students["student2"]["age"])
print("Items in nested dictionary:", students.items())

# Iterating over nested dictionaries
print("\nIterating over nested dictionaries")
for student_id, student_info in students.items():
    print(f"{student_id}: {student_info}")
    for key, value in student_info.items():
        print(f"{key}: {value}")

# Dictionary Comprehension
squares = {x: x**2 for x in range(5)}
print("\nDictionary comprehension (squares):", squares)
evens = {x: x**2 for x in range(10) if x % 2 == 0}
print("Conditional dictionary comprehension (evens):", evens)

# Practical Examples
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print("\nCount frequency of elements in list:", frequency)

# Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary (dict2 overwrites dict1 keys if same):", merged_dict)

# grouping data, storing configurations, and more.
