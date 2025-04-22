# Sets
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
numbers.remove(3)
print("Set:", numbers)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# Removing duplicates from list
nums = [1, 2, 2, 3, 3, 3, 4]
unique_nums = set(nums)
print("Unique numbers:", unique_nums)

# Frozenset
fset = frozenset([1, 2, 3])
print("Frozenset:", fset)
