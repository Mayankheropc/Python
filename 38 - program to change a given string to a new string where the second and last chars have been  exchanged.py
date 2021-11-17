# program to change a given string to a new string where the second and last chars have been exchanged

# By - Mayank Singh
# Date of Creation - 02-11-2021
# Last Modified - 02-11-2021

mystring = input("Enter a string: ")
strlen = len(mystring)
newstring = mystring[0] + mystring[strlen-1] + mystring[2:strlen-1] + mystring[1]

print(newstring)


# output

# Enter a string: abcdefghi
# aicdefghb

# Enter a string: mayank  
# mkyana