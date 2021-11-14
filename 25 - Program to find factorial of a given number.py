# Program to find factorial of a given number

# By - Mayank Singh
# Date of Creation - 23-10-2021
# Last Modified - 25-10-2021

num = int(input("Enter a number: "))
factorial = 1

if num == 0 or num == 1:
    print("Factorial: ", factorial)
else:
    while num>0:
        factorial *= num
        num -= 1
    
    print("Factorial:", factorial)