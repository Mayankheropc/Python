# program to find the maximum occurring character in a given string.

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

mystring = input("Enter a string: ")
mydict = dict()

for i in mystring:
    if i in mydict:
        mydict[i] += 1
    else:
        mydict[i] = 1

maxvalue = max(mydict.values())

for key, value in mydict.items():
    if value == maxvalue:
        print("Maximum occuring character is:",key)

# Output

# Enter a string: hello
# Maximum occuring character is: l

# Enter a string: mayank
# Maximum occuring character is: a

# Enter a string: mayank singh
# Maximum occuring character is: a
# Maximum occuring character is: n