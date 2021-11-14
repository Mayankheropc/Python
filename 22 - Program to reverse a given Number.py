# Program to reverse a given Number. ex: n=123 Reversed no is 321

# By - Mayank Singh
# Date of Creation - 23-10-2021
# Last Modified - 25-10-2021

num = int(input("Enter a number: "))
reverse = 0

while num>0:
    temp = num%10
    reverse = (reverse*10)+temp
    num = int(num/10)

print(reverse)