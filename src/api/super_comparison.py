# Python super() - follows MRO
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak()  # Calls Animal.speak()

class Cat(Animal):
    def speak(self):
        print("Cat meows")
        super().speak()  # Calls Animal.speak()

# Multiple inheritance - this is where Python differs from Java
class Hybrid(Dog, Cat):
    def speak(self):
        print("Hybrid speaks")
        super().speak()  # Follows MRO: Dog -> Cat -> Animal

print("=== Single Inheritance (similar to Java) ===")
dog = Dog()
dog.speak()

print("\n=== Multiple Inheritance (Python only) ===")
print("MRO:", Hybrid.mro())
hybrid = Hybrid()
hybrid.speak()