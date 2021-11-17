# Write a Python program to remove spaces from a given string

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

mystring = input("Enter a string: ")
newstring = ""

for i in mystring:
    if i != " ":
        newstring += i

print("String without space: ", newstring)


# Output

# Enter a string: Mayank Singh
# String without space:  MayankSingh

# Enter a string: well again a test string :)
# String without space:  wellagainateststring:)