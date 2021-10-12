# a program to print multiplication table for a given number using for as well as while loop
# By - Mayank Singh
# Date of Creation - 09-10-2021
# Last Modified - 09-10-2021

n = int(input("Enter a number: "))
x = 1
print("Table of ", n , "is :")
while(x<=10):
    print(n, " X ", x, " = ", x*n)
    x += 1

# Output : 
# Enter a number: 2
# Table of  2 is :
# 2  X  1  =  2
# 2  X  2  =  4
# 2  X  3  =  6
# 2  X  4  =  8
# 2  X  5  =  10
# 2  X  6  =  12
# 2  X  7  =  14
# 2  X  8  =  16
# 2  X  9  =  18
# 2  X  10  =  20