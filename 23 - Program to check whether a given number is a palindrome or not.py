# Program to check whether a given number is a palindrome or not
# example --> 1235321 = 12345321(reverse)

# By - Mayank Singh
# Date of Creation - 23-10-2021
# Last Modified - 25-10-2021

original = int(input("Enter a number: "))
num = original
reverse = 0

while num>0:
    temp = num%10
    reverse = (reverse*10)+temp
    num = int(num/10)

if original == reverse:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")