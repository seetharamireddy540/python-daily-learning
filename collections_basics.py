"""
Python Collections - Complete Basics Guide
==========================================
"""

# 1. LIST - Ordered, mutable, allows duplicates
print("=== LISTS ===")
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')        # Add to end
fruits.insert(1, 'mango')     # Insert at index
fruits.remove('banana')       # Remove by value
print(f"List: {fruits}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"Slice [1:3]: {fruits[1:3]}")

# 2. TUPLE - Ordered, immutable, allows duplicates
print("\n=== TUPLES ===")
coordinates = (10, 20)
person = ('John', 25, 'Engineer')
print(f"Tuple: {coordinates}")
print(f"Name: {person[0]}, Age: {person[1]}")
# coordinates[0] = 15  # Error! Tuples are immutable

# 3. SET - Unordered, mutable, no duplicates
print("\n=== SETS ===")
numbers = {1, 2, 3, 3, 4}  # Duplicate 3 removed
numbers.add(5)
numbers.discard(2)
print(f"Set: {numbers}")
print(f"Is 3 in set? {3 in numbers}")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# 4. DICTIONARY - Key-value pairs, ordered (Python 3.7+)
print("\n=== DICTIONARIES ===")
student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
student['city'] = 'NYC'       # Add new key
student['age'] = 21           # Update existing
del student['grade']          # Remove key
print(f"Dict: {student}")
print(f"Name: {student['name']}")
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")

# 5. STRING - Immutable sequence of characters
print("\n=== STRINGS ===")
text = "Hello World"
print(f"String: {text}")
print(f"Length: {len(text)}")
print(f"Upper: {text.upper()}")
print(f"Split: {text.split()}")
print(f"Replace: {text.replace('World', 'Python')}")

# 6. RANGE - Immutable sequence of numbers
print("\n=== RANGE ===")
for i in range(3):
    print(f"Range item: {i}")

numbers_list = list(range(1, 6))  # Convert to list
print(f"Range as list: {numbers_list}")

# COMMON OPERATIONS
print("\n=== COMMON OPERATIONS ===")
data = [1, 2, 3, 4, 5]
print(f"Length: {len(data)}")
print(f"Min: {min(data)}")
print(f"Max: {max(data)}")
print(f"Sum: {sum(data)}")
print(f"Sorted: {sorted(data, reverse=True)}")

# LIST COMPREHENSIONS
print("\n=== LIST COMPREHENSIONS ===")
squares = [x**2 for x in range(5)]
evens = [x for x in range(10) if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Evens: {evens}")

# NESTED COLLECTIONS
print("\n=== NESTED COLLECTIONS ===")
matrix = [[1, 2], [3, 4], [5, 6]]
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92}
]
print(f"Matrix[1][0]: {matrix[1][0]}")
print(f"Student grade: {students[0]['grade']}")