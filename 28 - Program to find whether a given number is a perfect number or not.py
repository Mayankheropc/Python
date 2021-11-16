# Program to find whether a given number is a perfect number or not.
# perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself
# 1, 2, 4, 7, 14 are divisor of 28 and 1+2+4+7+14=28

# By - Mayank Singh
# Date of Creation - 27-10-2021
# Last Modified - 27-10-2021

num = int(input("Enter a number: "))
divisor = []

for i in range(1, int(num/2)+1):
    if num%i == 0:
        divisor.append(i)

total = sum(divisor)    #sum of all the divisors

if total == num:
    print("Given number is a perfect number.")
    print("Divisors: ", divisor)
else:
    print("Given number is not a perfect number.")