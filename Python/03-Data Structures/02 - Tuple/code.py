# ===================== Tuples Tutorial =====================
# Tuples are ordered, immutable collections of items in Python.
# They are similar to lists, but once created, their elements cannot be changed.

print("========== Introduction to Tuples ==========")
print("Tuples are ordered, immutable collections of items.\n")

# ===================== Creating Tuples =====================
# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)
print("Type of empty_tuple:", type(empty_tuple))

# Using tuple() constructor
tpl = tuple()
print("Type of tpl:", type(tpl))

# Tuple from a list
numbers = tuple([1, 2, 3, 4, 5, 6])
print("Tuple from list:", numbers)

# Mixed tuple with different data types
mixed_tuple = (1, "Hello World", 3.14, True)
print("Mixed tuple:", mixed_tuple)

# ===================== Accessing Tuple Elements =====================
print("\n========== Accessing Tuple Elements ==========")
print("Third element:", numbers[2])
print("Last element:", numbers[-1])
print("Slice (first four elements):", numbers[0:4])
print("Reverse tuple:", numbers[::-1])

# ===================== Tuple Operations =====================
print("\n========== Tuple Operations ==========")
# Concatenation
concatenation_tuple = numbers + mixed_tuple
print("Concatenated tuple:", concatenation_tuple)

# Repetition
print("Repeated mixed tuple:", mixed_tuple * 3)
print("Repeated numbers tuple:", numbers * 3)

# ===================== Immutable Nature of Tuples =====================
print("\n========== Immutable Nature of Tuples ==========")
# Tuples cannot be modified. Attempting to change an element will raise an error.
lst = [1, 2, 3, 4, 5]  # Using list to show mutability contrast
print("Original list:", lst)
lst[1] = "Tirup"
print("Modified list:", lst)

# Uncommenting the following line will raise an error because tuples are immutable
# numbers[1] = "Tirup"

# ===================== Tuple Methods =====================
print("\n========== Tuple Methods ==========")
print("Count of 1 in numbers tuple:", numbers.count(1))
print("Index of 3 in numbers tuple:", numbers.index(3))

# ===================== Packing and Unpacking Tuples =====================
print("\n========== Packing and Unpacking Tuples ==========")
# Packing
packed_tuple = 1, "Hello", 3.14
print("Packed tuple:", packed_tuple)

# Unpacking
a, b, c = packed_tuple
print("Unpacked values:", a, b, c)

# Unpacking with *
first, *middle, last = numbers
print("First element:", first)
print("Middle elements:", middle)
print("Last element:", last)

# ===================== Nested Tuples =====================
print("\n========== Nested Tuples ==========")
# Nested list inside list
lst = [[1, 2, 3, 4], [6, 7, 8, 9], [1, "Hello", 3.14, "c"]]
print("Nested list first sublist first 3 elements:", lst[0][0:3])

# Nested tuple inside list
lst = [[1, 2, 3, 4], [6, 7, 8, 9], (1, "Hello", 3.14, "c")]
print("Nested tuple first 3 elements:", lst[2][0:3])

# Nested tuple example
nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))
print("First nested tuple:", nested_tuple[0])
print("Third element of second tuple:", nested_tuple[1][2])

# Iterating over nested tuples
print("Iterating over nested tuple elements:")
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item, end=" ")
    print()

