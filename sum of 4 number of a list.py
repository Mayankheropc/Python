# python program to sum a list with 4 numbers
# By - Mayank Singh
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

numbers = []
x = 1
while(len(numbers)<4):
    numbers.append(int(input("Enter " + str(x) + " number: ")))
    x += 1
print("List Created: ")
print(numbers)

print("Sum of the list: ", sum(numbers))