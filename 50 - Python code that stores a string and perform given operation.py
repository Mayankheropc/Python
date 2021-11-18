# Take the following Python code that stores a string: ‘str = 'Y-tatata-acropolis: 0.8475'. Use find and string 
# slicing to extract the portion of the string after the colon character and then use the float function to convert 
# the extracted string into a floating point number

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

from typing import NewType


def float_converter(temp):
    ans = float(temp)
    return ans

string = "Y-tatata-acropolis: 0.8475"
x = 0
newstring = ""
for i in string:
    if i == ":":
        newstring += string[x+2:]
        break
    x += 1

print("Original string: ", string)

print("type before conversion: ", type(newstring), "value: ", newstring)

print("type after conversion: ", type(float_converter(newstring)), "value: ", float_converter(newstring))

# Output

# Original string:  Y-tatata-acropolis: 0.8475
# type before conversion:  <class 'str'> value:  0.8475
# type after conversion:  <class 'float'> value:  0.8475

