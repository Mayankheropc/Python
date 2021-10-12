# program to find out whether a given name is present in a list or not
# By - Mayank Singh
# Date of Creation - 09-10-2021
# Last Modified - 09-10-2021

l1 = ["simarjeet", "sohan", "sachin", "rahul"]
key = input("enter name you want to find: ")
if(key in l1):
    print("name is present in the list")
else:
    print("name is not present in the list")