# program to display the sum of input (n) numbers using a list.

# By - Mayank Singh
# Date of Creation - 03-11-2021
# Last Modified - 05-11-2021

numbers = []
x = 1
n = int(input("Total no. you want to enter: "))

while(len(numbers)<n):
    numbers.append(int(input("Enter " + str(x) + " number: ")))
    x += 1
print("List Created: ")
print(numbers)

print("Sum of the list: ", sum(numbers))


# Output

# Total no. you want to enter: 5
# Enter 1 number: 2
# Enter 2 number: 5
# Enter 3 number: 4
# Enter 4 number: 5
# Enter 5 number: 3
# List Created: 
# [2, 5, 4, 5, 3]
# Sum of the list:  19