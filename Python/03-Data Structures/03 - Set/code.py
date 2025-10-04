# ===================== Sets =====================
# print("Sets are unordered collections of unique items.\n")

# ===================== Creating Sets =====================
my_set = {1, 2, 3, 4, 5}  # Create a set with elements
print(f"Set: {my_set}")
print(f"Type of my_set: {type(my_set)}")

my_empty_set = set()  # Create an empty set
print(f"Type of empty set: {type(my_empty_set)}")

my_set_from_list = set([1, 2, 3, 4, 5, 6])
print(f"Set from list: {my_set_from_list}")

# Duplicate elements are automatically removed
my_set_duplicates = set([1, 2, 3, 6, 5, 4, 5, 6])
print(f"Set after removing duplicates: {my_set_duplicates}\n")

# ===================== Adding and Removing Elements =====================
my_set.add(7)  # Add element
print(f"Set after adding 7: {my_set}")
my_set.add(7)  # Adding duplicate has no effect
print(f"Set after adding 7 again: {my_set}")

my_set.remove(3)  # Remove element
print(f"Set after removing 3: {my_set}")

# Discard does not raise an error if element doesn't exist
my_set.discard(11)
print(f"Set after discarding 11 (non-existent): {my_set}")

# Pop removes an arbitrary element
removed_element = my_set.pop()
print(f"Removed element: {removed_element}")
print(f"Set after pop: {my_set}")

# Clear removes all elements
my_set.clear()
print(f"Set after clear: {my_set}\n")

# ===================== Membership Test =====================
my_set = {1, 2, 3, 4, 5}
print(f"Is 3 in set? {3 in my_set}")
print(f"Is 10 in set? {10 in my_set}\n")

# ===================== Mathematical Set Operations =====================
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# Union
union_set = set1.union(set2)
print(f"Union: {union_set}")

# Intersection
intersection_set = set1.intersection(set2)
print(f"Intersection: {intersection_set}")

# Update intersection
set1.intersection_update(set2)
print(f"Set1 after intersection update: {set1}")

# Difference
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}
print(f"Difference (set1 - set2): {set1.difference(set2)}")
print(f"Set1: {set1}")
print(f"Difference (set2 - set1): {set2.difference(set1)}")

# Symmetric Difference
print(f"Symmetric difference: {set1.symmetric_difference(set2)}\n")

# ===================== Set Methods =====================
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5}

# Subset and Superset
print(f"Is set1 subset of set2? {set1.issubset(set2)}")
print(f"Is set1 superset of set2? {set1.issuperset(set2)}\n")

# ===================== Removing Duplicates from List =====================
lst = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(lst)
print(f"Unique elements from list: {unique_set}\n")

# ===================== Counting Unique Words in Text =====================
text = "In this tutorial we are discussing about sets"
words = text.split()
unique_words = set(words)
print(f"Unique words: {unique_words}")
print(f"Number of unique words: {len(unique_words)}")
