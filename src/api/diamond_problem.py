# Diamond Problem Example
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")
        super().method()

class C(A):
    def method(self):
        print("C")
        super().method()

# Diamond inheritance: D inherits from both B and C, which both inherit from A
class D(B, C):
    def method(self):
        print("D")
        super().method()

# The problem: Which path should D follow to reach A?
# Path 1: D -> B -> A
# Path 2: D -> C -> A

print("=== Diamond Problem Demo ===")
print("MRO:", D.mro())
d = D()
d.method()

print("\n=== What happens without super() ===")
class E(B, C):
    def method(self):
        print("E")
        B.method(self)  # Explicit call - causes duplicate A calls
        C.method(self)

e = E()
e.method()