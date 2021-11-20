# Python program to find the even numbers in a List.

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 12-11-2021

list = [0, 15, 62, 23, 54, 54, 22, 24, 55, 20, 81, 13, 7, 40]
listEven = []

for i in list:
    if(i % 2 == 0):
        listEven.append(i)

print("All numbers in the list are: ", list)
print("The Even Numbers Are: ", listEven)



# Output

# All numbers in the list are:  [0, 15, 62, 23, 54, 54, 22, 24, 55, 20, 81, 13, 7, 40]
# The Even Numbers Are:  [0, 62, 54, 54, 22, 24, 20, 40]