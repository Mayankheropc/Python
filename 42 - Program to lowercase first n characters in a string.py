# Write a Python program to lowercase first n characters in a string

# By - Mayank Singh
# Date of Creation - 02-11-2021
# Last Modified - 05-11-2021

mystring = input("Enter a string: ")
n = int(input("From starting of the string, how many character you want in UPPER case: "))
newstring = ""

for i in range(0, n):
    newstring += mystring[i].upper()
newstring += mystring[n:]

print(newstring)


# Output

# Enter a string: mayank
# From starting of the string, how many character you want in UPPER case: 2

# Enter a string: demo String
# From starting of the string, how many character you want in UPPER case: 8
# DEMO STRing