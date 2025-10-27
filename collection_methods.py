"""
Collection Methods Cheat Sheet
==============================
"""

# LIST METHODS
print("=== LIST METHODS ===")
lst = [1, 2, 3]
lst.append(4)           # Add to end
lst.extend([5, 6])      # Add multiple items
lst.insert(0, 0)        # Insert at index
lst.remove(2)           # Remove first occurrence
popped = lst.pop()      # Remove and return last
lst.reverse()           # Reverse in place
lst.sort()              # Sort in place
print(f"Final list: {lst}")

# DICT METHODS
print("\n=== DICT METHODS ===")
d = {'a': 1, 'b': 2}
d.update({'c': 3})      # Add/update multiple
value = d.get('d', 0)   # Get with default
d.setdefault('e', 5)    # Set if key doesn't exist
keys = d.keys()         # Get all keys
values = d.values()     # Get all values
items = d.items()       # Get key-value pairs
print(f"Dict: {d}")

# SET METHODS
print("\n=== SET METHODS ===")
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.add(4)               # Add single item
s1.update([5, 6])       # Add multiple items
s1.discard(6)           # Remove (no error if missing)
union = s1.union(s2)    # Combine sets
inter = s1.intersection(s2)  # Common elements
diff = s1.difference(s2)     # Elements in s1 not in s2
print(f"Union: {union}")

# STRING METHODS
print("\n=== STRING METHODS ===")
text = "  Hello World  "
print(f"Strip: '{text.strip()}'")
print(f"Split: {text.split()}")
print(f"Join: {'-'.join(['a', 'b', 'c'])}")
print(f"Replace: {text.replace('World', 'Python')}")
print(f"Find: {text.find('World')}")
print(f"Startswith: {text.strip().startswith('Hello')}")

# COMMON FUNCTIONS
print("\n=== COMMON FUNCTIONS ===")
numbers = [3, 1, 4, 1, 5]
print(f"len(): {len(numbers)}")
print(f"sum(): {sum(numbers)}")
print(f"min(): {min(numbers)}")
print(f"max(): {max(numbers)}")
print(f"sorted(): {sorted(numbers)}")
print(f"reversed(): {list(reversed(numbers))}")
print(f"enumerate(): {list(enumerate(numbers))}")
print(f"zip(): {list(zip(numbers, ['a', 'b', 'c']))}")