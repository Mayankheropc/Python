# Python program to print a specified list after removing the 1st, 2nd and 5th elements.

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 08-11-2021

list = [21, 85, 37, 19, 23, 51]
print("List Before delete[1,2,5] : ", list)
list = [x for (i, x) in enumerate(list) if i not in (0, 1, 4)]
print("List After delete[1,2,5] : ", list)


# Output

# List Before delete[1,2,5] :  [21, 85, 37, 19, 23, 51]
# List After delete[1,2,5] :  [37, 19, 51]