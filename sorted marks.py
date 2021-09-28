# program to sort marks of 6 students
# By - Mayank Singh
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

marks = []
x = 1
while(len(marks)<6):
    marks.append(input("Enter Student " + str(x) + " marks: "))
    x += 1
print("List Created: ")
print("before sorting: ")
print(marks)
marks.sort()
print("after sorting: ")
print(marks)