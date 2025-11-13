# Duck Typing Example

class Duck:
    def quack(self):
        return "Quack!"
    
    def fly(self):
        return "Flying like a duck"

class Dog:
    def quack(self):
        return "Woof! (pretending to quack)"
    
    def fly(self):
        return "Running fast (can't actually fly)"

class Robot:
    def quack(self):
        return "Beep beep (robot quack)"
    
    def fly(self):
        return "Jet propulsion activated"

# Duck typing in action - no type checking needed
def make_it_quack_and_fly(thing):
    print(f"Quack: {thing.quack()}")
    print(f"Fly: {thing.fly()}")

# All work because they have quack() and fly() methods
animals = [Duck(), Dog(), Robot()]

for animal in animals:
    print(f"\n--- {animal.__class__.__name__} ---")
    make_it_quack_and_fly(animal)

# This would fail - no quack() method
class Cat:
    def meow(self):
        return "Meow"

print("\n--- Error Example ---")
try:
    make_it_quack_and_fly(Cat())
except AttributeError as e:
    print(f"Error: {e}")