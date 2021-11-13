# Write a Python program to parse a string to Float & Integer
# By - Mayank Singh
# Date of Creation - 28-10-2021
# Last Modified - 28-10-2021

mystring = input("Enter a numarical string: ")
print(mystring, end="")
print("   " , type(mystring))

myfloatstring = float(mystring)
print(myfloatstring, end="")
print("   " , type(myfloatstring))

myintstring = int(myfloatstring)
print(myintstring, end="")
print("   " , type(myintstring))