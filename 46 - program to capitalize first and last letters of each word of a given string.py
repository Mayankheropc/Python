# program to capitalize first and last letters of each word of a given string

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

mystring = input("Enter a string: ")
newstring = ""

newstring = mystring[0].upper() + mystring[1:len(mystring)-1] + mystring[len(mystring)-1].upper()

print(newstring)

# Output

# Enter a string: mayank singh
# Mayank singH

# Enter a string: demo
# DemO