# First, def a function called calculate_distance, with one argument (choose any argument name you like). If the 
# type of the argument is either int or float, the function should return the absolute value of the function input. 
# Otherwise, the function should return "No value". Check if it works calling the function with 9.6 and "what?"

# By - Mayank Singh
# Date of Creation - 03-11-2021
# Last Modified - 05-11-2021

def calculate_distance(p):
    return abs(p)


p = float(input("Enter A Number : "))

print("Absolute Value is : ", calculate_distance(p))

# Output

# Enter A Number : 9.255
# Absolute Value is :  9.255

# Enter A Number : 9.6
# Absolute Value is :  9.6

# Enter A Number : 5
# Absolute Value is :  5.0