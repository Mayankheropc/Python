# Python program to move spaces to the front of a given string.

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

mystring = input("Enter a string: ")
newstring = ""
count = 0

for i in mystring:
    if i != " ":
        newstring += i
    else:
        count += 1

ans = ""
for i in range(0, count):
    ans += " "

ans += newstring

print("Total no. of spaces in the string are:", count)
print("String with spaces at front:", ans)

# Output

# Enter a string: Mayank Singh Bhadauriya
# Total no. of spaces in the string are: 2
# String with spaces at front:   MayankSinghBhadauriya