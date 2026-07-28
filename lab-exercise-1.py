# lab exercise 1

name = input("Enter ur name: ")
usn = input("Enter ur usn: ")
branch = input("Enter ur branch: ")
sem = int(input("Enter ur semester (1-8): "))
marks1 = float(input("Enter subject1 marks: "))
marks2 = float(input("Enter subject2 marks: "))
marks3 = float(input("Enter subject3 marks: "))

total_marks = marks1+marks2+marks3
average_marks = total_marks/3

print("---------STUDENT REPORT---------")
print(f"Student name = {name}")
print(f"USN = {usn}")
print(f"Branch = {branch}")
print(f"Semester = {sem}")
print(f"Total Marks = {total_marks}")
print(f"Average Marks = {average_marks:.2f}")
print("--------------------------------")
