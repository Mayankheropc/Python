# Program to check whether a given number is an Armstrong number or not
# Armstrong number is a number that is equal to the sum of cubes of its digits. 
# For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers
# 153 = 1^3 + 5^3 + 3^3

# By - Mayank Singh
# Date of Creation - 23-10-2021
# Last Modified - 25-10-2021

original = int(input("Enter a number: "))
num = original
sum = 0

while num>0:
    temp = num%10
    sum += temp*temp*temp
    num = int(num/10)

print("Sum of cubes of its digits", sum)
if sum == original:
    print("Number is an armstrong number")
else:
    print("Number is not an armstrong number")