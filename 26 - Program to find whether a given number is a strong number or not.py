# Program to find whether a given number is a strong number or not. 
# e.g. n=145 1!+4!+5!==145

# By - Mayank Singh
# Date of Creation - 23-10-2021
# Last Modified - 25-10-2021

def fact(x):
    factorial = 1
    if x == 0 or x == 1:
        return factorial
    else:
        while x>0:
            factorial *= x
            x -= 1
        return factorial

original = int(input("Enter a number: "))
num = original

if num<10:  #single digit number
    print("Factorial of the given number is:", fact(num))
    print("Given number is not a strong number")
else:
    sum = 0
    while num>0:
        temp = num%10
        sum += fact(temp)
        num = int(num/10)
    
    print("Sum of factorial of digits:", sum)

    if sum == original:
        print("Given number is a strong number")
    else:
        print("Given number is not a strong number")