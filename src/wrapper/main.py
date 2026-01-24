
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def do_something(self, something):
        print(self.name + " is doing " + something)


person = Person("John", 20)
person.do_something("reading")
