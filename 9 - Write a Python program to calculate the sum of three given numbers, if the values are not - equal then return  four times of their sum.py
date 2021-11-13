# Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum
# By - Mayank Singh
# Date of Creation - 29-10-2021
# Last Modified - 29-10-2021

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))
sum = num1+num2+num3

if (num1 == num2 == num3):
    print(sum)
else:
    print(sum*4)