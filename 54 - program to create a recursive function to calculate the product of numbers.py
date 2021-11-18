# program to create a recursive function to calculate the product of numbers

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

def product(num1,num2):
    if(num1<num2):
        return product(num2,num1)
    elif(num2!=0):
         return(num1+product(num1,num2-1))
    else:
         return 0

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

print("product is: ",product(num1,num2))