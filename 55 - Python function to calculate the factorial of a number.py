# Python function to calculate the factorial of a number

# By - Mayank Singh
# Date of Creation - 08-11-2021
# Last Modified - 10-11-2021

def factorial(n):
    sum = 1
    if n==0 or n==1:
        return 1
    else:
        for i in range(2, n+1):
            sum *= i
        return sum

num = int(input("Enter a number: "))

print("Factorial:", factorial(num))

# Output

# Enter a number: 5
# Factorial: 120

# Enter a number: 6
# Factorial: 720