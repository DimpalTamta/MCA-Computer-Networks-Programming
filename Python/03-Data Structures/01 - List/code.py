# =============================
# Introduction to Lists
# =============================
# Lists are ordered, mutable collections of items. They can store multiple data types.
print("========== Introduction to Lists ==========")

# Empty list
lst = []
print(f"Empty List: {lst} | Type: {type(lst)}")

# List with mixed data types
mixed_list = [1, "Hello", 3.14, True]
print(f"Mixed List: {mixed_list}")

# List of names
names = ["Priya", "Jack", "Jacob", 1, 2, 3, 4, 5]
print(f"Names List: {names}")

# =============================
# Accessing List Elements
# =============================
print("\n========== Accessing List Elements ==========")
fruits = ["apple", "banana", "cherry", "kiwi", "gauva"]

print(f"First Element: {fruits[0]}")
print(f"Third Element: {fruits[2]}")
print(f"Last Element: {fruits[-1]}")
print(f"Slice 1-4: {fruits[1:4]}")
print(f"Slice from 2 to end: {fruits[2:]}")

# =============================
# Modifying List Elements
# =============================
print("\n========== Modifying List Elements ==========")
fruits[1] = "watermelon"
print(f"Modified List: {fruits}")

# Resetting list
fruits = ["apple", "banana", "cherry", "kiwi", "gauva"]

# =============================
# List Methods
# =============================
print("\n========== List Methods ==========")
fruits.append("orange")
print(f"After append: {fruits}")

fruits.insert(1, "watermelon")
print(f"After insert at index 1: {fruits}")

fruits.remove("banana")
print(f"After removing first 'banana': {fruits}")

popped = fruits.pop()
print(f"Popped element: {popped}")
print(f"After pop: {fruits}")

index = fruits.index("cherry")
print(f"Index of 'cherry': {index}")

fruits.insert(2, "banana")
print(f"Count of 'banana': {fruits.count('banana')}")

fruits.sort()
print(f"Sorted List: {fruits}")

fruits.reverse()
print(f"Reversed List: {fruits}")

fruits.clear()
print(f"Cleared List: {fruits}")

# =============================
# Slicing Lists
# =============================
print("\n========== Slicing Lists ==========")
numbers = [1,2,3,4,5,6,7,8,9,10]
print(f"Slice 2-5: {numbers[2:5]}")
print(f"Slice start-5: {numbers[:5]}")
print(f"Slice 5-end: {numbers[5:]}")
print(f"Every 2nd element: {numbers[::2]}")
print(f"Reverse List: {numbers[::-1]}")
print(f"Every 3rd element: {numbers[::3]}")
print(f"Reverse every 2nd element: {numbers[::-2]}")

# =============================
# Iterating Over Lists
# =============================
print("\n========== Iterating Over Lists ==========")
for num in numbers:
    print(f"{num}", end=" ")
print()

for idx, num in enumerate(numbers):
    print(f"{idx}: {num}")

# =============================
# List Comprehensions
# =============================
print("\n========== List Comprehensions ==========")
# Basic comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
even_numbers = [x for x in range(10) if x%2==0]
print(f"Even Numbers: {even_numbers}")

# Nested comprehension
lst1 = [1,2,3,4]
lst2 = ['a','b','c','d']
pairs = [[i,j] for i in lst1 for j in lst2]
print(f"Pairs: {pairs}")

# Using function calls in comprehension
words = ["hello", "world", "python", "list", "comprehension"]
lengths = [len(word) for word in words]
print(f"Lengths of words: {lengths}")

