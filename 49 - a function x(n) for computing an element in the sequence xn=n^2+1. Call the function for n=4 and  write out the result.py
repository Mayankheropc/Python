# Write a function x(n) for computing an element in the sequence xn = n^2 + 1. 
# Call the function for n=4 and write out the result.

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

def x(n):
    for i in range(1, n+1):
        ans = (i*i) + 1
        print(ans, end=" ")

num = int(input("Enter number of elements: "))

print("series of element in sequence (xn = n^2 + 1) is: ")
x(num)

# Output

# Enter number of elements: 4
# series of element in sequence (xn = n^2 + 1) is: 
# 2 5 10 17

# Enter number of elements: 7
# series of element in sequence (xn = n^2 + 1) is: 
# 2 5 10 17 26 37 50