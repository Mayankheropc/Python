#  Write a Python program to add 'polis' at the end of a given string (length should be at least 3).
#  If the given string already ends with 'polis' then add 'polisCS' instead.
#  If the string length of the given string is less than 3, leave it unchanged. 
#  Sample String : 'abc'
#  Expected Result : 'abcpolis' 
#  Sample String : 'Acropolis'
#  Expected Result : 'AcropolisCS'

# By - Mayank Singh
# Date of Creation - 02-11-2021
# Last Modified - 05-11-2021

string = input("Enter a string: ")
length = len(string)

if length<3:
    print(string)
else:
    newstring = string[len(string)-5:]
    
    if newstring == 'polis':
        temp = string + 'CS'
        print(temp)
    else:
        temp = string + 'polis'
        print(temp)