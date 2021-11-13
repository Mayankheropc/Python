# Write a Python program that accepts an integer (a) and computes the value of a+aa+aaa.
# By - Mayank Singh
# Date of Creation - 28-10-2021
# Last Modified - 28-10-2021

a = int(input("Enter a number: "))
a = a+(a*a)+(a*a*a)
print(a)