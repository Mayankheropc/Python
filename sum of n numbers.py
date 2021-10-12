# program to print the sum of first n natural numbers using while loop
# By - Mayank Singh
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

num = int(input("Enter positive Number: "))
sum = 0

while(num > 0):
    sum += num
    num -= 1
    
print("The sum is", sum)