"""
Advanced Collections - collections module
=========================================
"""

from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# 1. COUNTER - Count hashable objects
print("=== COUNTER ===")
text = "hello world"
counter = Counter(text)
print(f"Letter count: {counter}")
print(f"Most common: {counter.most_common(3)}")

# 2. DEFAULTDICT - Dict with default values
print("\n=== DEFAULTDICT ===")
dd = defaultdict(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
print(f"Default dict: {dict(dd)}")

# 3. DEQUE - Double-ended queue
print("\n=== DEQUE ===")
dq = deque([1, 2, 3])
dq.appendleft(0)    # Add to left
dq.append(4)        # Add to right
print(f"Deque: {dq}")
print(f"Pop left: {dq.popleft()}")
print(f"Pop right: {dq.pop()}")

# 4. NAMEDTUPLE - Tuple with named fields
print("\n=== NAMEDTUPLE ===")
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"Point: {p}")
print(f"X coordinate: {p.x}")
print(f"Y coordinate: {p.y}")

# 5. ORDEREDDICT - Dict that remembers insertion order
print("\n=== ORDEREDDICT ===")
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(f"Ordered dict: {od}")
od.move_to_end('first')  # Move to end
print(f"After move: {od}")