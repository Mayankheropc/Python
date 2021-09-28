# program to store seven fruits in a list entered by the user
# By - Mayank Singh
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

fruits = []
x = 1
while(len(fruits)<7):
    fruits.append(input("Enter " + str(x) + " Fruit Name : "))
    x = x+1
print("List Created: ")
print(fruits)