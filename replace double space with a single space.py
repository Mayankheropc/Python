# python program to replace double spaces with single space
# Good Afternoon using input() function
# By - Mayank Singh
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

import re
s = input("enter a string : ")
print("String befor removing multiple spaces:")
print(s)
print("String after removing multiple spaces:")
print(re.sub(' +', ' ', s))