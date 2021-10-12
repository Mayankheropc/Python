# program to find out whether a given name is present in a list or not
# By - Mayank Singh
# Date of Creation - 09-10-2021
# Last Modified - 09-10-2021

post = "hello my friend! how are you? Have you attended the last Python class taken by simarjeet sir? if yes then please male me the notes of that day thanks!"
key = input("enter name you want to find: ")
if(key in post):
    print("name is present in the post")
else:
    print("name is not present in the post")