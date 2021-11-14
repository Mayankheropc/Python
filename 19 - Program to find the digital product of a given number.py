# Program to find the digital product of a given number
# example: n=43 Digital product ----->4*3=12

# By - Mayank Singh
# Date of Creation - 22-10-2021
# Last Modified - 25-10-2021

# initialization
product = 1

num = int(input("Enter a number: "))

while num>0:
    temp = num%10
    product *= temp
    num = int(num/10)

print("Product of all the digits of the number is: ", product)