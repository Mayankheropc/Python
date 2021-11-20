# Program to return a function from another function.

# By - Mayank Singh
# Date of Creation - 03-11-2021
# Last Modified - 05-11-2021

def function2():
    print("function2 is called sucessfully!")

def function1():
    print("function1 is called, now it will print data from function2")
    return function2()

print("Calling function1")
function1()


# Output

# Calling function1
# function1 is called, now it will print data from function2
# function2 is called sucessfully!