# program to calculate the factorial of the given number
# By - Mayank Singh
# Date of Creation - 01-10-2021
# Last Modified - 09-10-2021

num = int(input("Enter a number: "))
ans=1
while(num>1):
    ans = ans * num
    num = num-1
print("Factorial is " , ans)