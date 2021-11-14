# Program to find digital sum of a given Number
# example: n=123 Digital sum----->1+2+3=6

# By - Mayank Singh
# Date of Creation - 22-10-2021
# Last Modified - 25-10-2021

# initialization
sum = 0

num = int(input("Enter a number: "))

while num>0:
    temp = num%10
    sum += temp
    num = int(num/10)

print("Sum of all the digits of the number is: ", sum)