# Given two integer numbers return their sum. If the sum is greater than 100, then return their product.
# By - Mayank Singh
# Date of Creation - 28-10-2021
# Last Modified - 28-10-2021

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

if (num1+num2) > 100:
    print(num1*num2)
else:
    print(num1+num2)