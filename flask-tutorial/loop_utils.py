
import sys
fruits = ['apple', 'banana', 'orange']
ages = [12, 18, 25]
cities = ['New York', 'London', 'Paris']

fruits.append('grape')

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(fruits[i])

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

for name, age, city in zip(fruits, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

print(f"size of fuid = {sys.getsizeof(fruits[0])} bytes")