# Python program to compute sum of digits of a given string.

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

mystring = input("Enter a numerical string: ")
sum = 0

for i in mystring:
    sum += int(i)

print("Sum of string:", sum)

# Output

# Enter a numerical string: 11225
# Sum of string: 11

# Enter a numerical string: 12345
# Sum of string: 15