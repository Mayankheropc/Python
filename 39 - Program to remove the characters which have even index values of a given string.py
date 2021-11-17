# Write a Python program to remove the characters which have even index values of a given string.

# By - Mayank Singh
# Date of Creation - 02-11-2021
# Last Modified - 05-11-2021

string = input("Enter a string: ")
newstring = ""
for i in range(0,len(string)):
    if (i+1)%2 != 0:
        newstring += string[i]

print(newstring)


# Output

# Enter a string: hello
# hlo

# Enter a string: Mayank
# Myn