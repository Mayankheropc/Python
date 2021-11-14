# Program to find whether a given number is a unique number. 
# The number will be unique if it is positive integer and there are no repeated digits in the number. 
# In other words, a number is said to be unique if and only if the digits are not duplicate.
# For example, 20, 56, 9863, 145, etc. are the unique numbers 
# while 33, 121, 900, 1010, etc. are not unique numbers

# By - Mayank Singh
# Date of Creation - 27-10-2021
# Last Modified - 27-10-2021

num = (input("Enter a number: "))

if len(set(num)) != len(num):
    print("The number has repeat digits! so not unique")
else:
    print("No repeat digits! so the number is unique")