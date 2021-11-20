# Python function to check whether the given integer is a prime number or not

# By - Mayank Singh
# Date of Creation - 08-11-2021
# Last Modified - 08-11-2021

def isprime(x):
    flag = 0
    for i in range(2, int(x/2)+1):
        if x%i == 0:
            flag = 1
            break

    if flag == 0:
        print("Prime!")
    else:
        print("not Prime!")

num = int(input("Enter a number: "))
print("The number is ", end='')
isprime(num)

# Output

# Enter a number: 13
# The number is Prime!

# Enter a number: 10
# The number is not Prime!