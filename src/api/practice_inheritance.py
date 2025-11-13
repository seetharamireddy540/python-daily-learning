from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def foo(self):
        pass
    def bar(self):
        print("A")

class B(A):
    def foo(self):
        print("B")

class C(A):
    def foo(self):
        print("C")
        super().bar()

class D(C,B):
    pass



d = D()
print("MRO:", D.mro())
d.foo()