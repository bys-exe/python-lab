# lab exercise 3 - Maths calculator using libraries

import math
no = float(input("Enter an number: "))
print("------------ANSWERS------------")
print(f"Square: {math.pow(no,2)}")
print(f"Cube: {math.pow(no,3)}")
print(f"Square root: {math.sqrt(no)}")
print(f"Ceiling Value: {math.ceil(no)}")
print(f"Floor Value: {math.floor(no)}")
print(f"Absolute Value: {abs(no)}")
print(f"Type of the variable: {type(no)}")
print(f"Memory address: {id(no)}")
print("-------------------------------")
