from api.app import say_hello
from utils.math_utils import add

fruits: str = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.append("banana")
fruits.append("kiwi")

for fruit in fruits:
    print(fruit)

coordinates = (13, 32)
person = ("John", 30, "male")
x, y = coordinates

number = {2, 4, 5, 2}
for num in number:
    print(num)


student = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
student["name"] = "Ram"
student["country"] = "USA"

if __name__ == "__main__":
    say_hello()