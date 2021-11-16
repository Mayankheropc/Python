# Program to find whether a given number is a prime number or not.

# By - Mayank Singh
# Date of Creation - 22-10-2021
# Last Modified - 22-10-2021

num = int(input("Enter a number: "))
count = 0

for i in range(2, int(num/2)+1):
    if num%i == 0:
        count += 1

if count == 0:
    print("The given number is a prime number.")
else:
    print("The given number is not a prime number.")