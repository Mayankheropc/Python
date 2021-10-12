# python program to find sum of first n odd numbers
# By - Mayank Singh
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

num = int(input("Print sum of odd numbers till : "))
sum = 0

for i in range(1, num + 1):

    #Check for odd or not.
    if(not (i % 2) == 0):
        sum += i

print("\nSum of odd numbers from 1 to", num, "is :", sum)