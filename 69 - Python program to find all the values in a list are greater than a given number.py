# Python program to find all the values in a list are greater than a given number

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 12-11-2021

n = int(input("Enter a Number: "))
list = [0, 2, 23, 54, 54, 22, 24]
listGreater = []

for i in list:
    if(i > n):
        listGreater.append(i)

print("The Greater Numbers Are : ", listGreater)


# Output

# Enter a Number: 25
# The Greater Numbers Are :  [54, 54]

# Enter Any Number : 5
# The Greater Numbers Are :  [23, 54, 54, 22, 24]