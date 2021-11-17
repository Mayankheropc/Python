# Write a Python program to get a single string from two given strings, separated by a space 
# and swap the first characters of each string
# Sample String : 'abc', 'xyz' 
# Expected Result : 'xbc ayz'

# By - Mayank Singh
# Date of Creation - 02-11-2021
# Last Modified - 05-11-2021

def mixstr(a, b):
    new_a = b[0] + a[1:]
    new_b = a[0] + b[1:]
    return new_a + ' ' + new_b

str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")

print(mixstr(str1, str2))