#  Write a Python program to count the number of characters (character frequency) in a string. 
#  Sample String : google.com'
#  Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# By - Mayank Singh
# Date of Creation - 02-11-2021
# Last Modified - 05-11-2021

mystring = input("Enter a string: ")
mydic = dict()

for i in mystring:
    if i in mydic:
        mydic[i] += 1
    else:
        mydic[i] = 1

print(mydic)


# output

# Enter a string: google.com
# {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

# Enter a string: well hello
# {'w': 1, 'e': 2, 'l': 4, ' ': 1, 'h': 1, 'o': 1}

# Enter a string: oh just one more test string, then you can start another question
# {'o': 6, 'h': 3, ' ': 11, 'j': 1, 'u': 3, 's': 5, 't': 9, 'n': 6, 'e': 6, 'm': 1, 'r': 4, 'i': 2, 'g': 1, ',': 1, 'y': 1, 'c': 1, 'a': 3, 'q': 1}