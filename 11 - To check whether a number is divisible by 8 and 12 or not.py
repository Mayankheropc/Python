# To check whether a number is divisible by 8 and 12 or not
# By - Mayank Singh
# Date of Creation - 29-10-2021
# Last Modified - 29-10-2021

num = int(input("Enter a number: "))

if (num%8)==0:  #checking if the number is divisible by 8 or not
    print("Yes, the number is divisible by 8")
else:
    print("No, the number is not divisible by 8")

if (num%12)==0:  #checking if the number is divisible by 12 or not
    print("Yes, the number is divisible by 12")
else:
    print("No, the number is not divisible by 12")