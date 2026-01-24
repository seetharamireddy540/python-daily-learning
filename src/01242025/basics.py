print("Hello, world")

x, y, z = 12, 3, 1
variable = 3
variable = "Ram"

a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtractio n
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a // b)  # Division without decimals


# Control Flow
age = 20
if age >= 18:
    print("You can vote")
else:
    print("You can not vote")

for i in range(1, 11):
    print(i)

count = 0
while count < 10:
    print(count)
    count += 1


print("Hello, world")

fruits = ["abpple", "banana"]
print(fruits[0])
print(fruits[-1])


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("Execution completed")

# Importing modules
import math

print(math.sqrt(16))

# Specific import
from datetime import datetime

current_time = datetime.now()
