# program to delete an element from a list by index which is given by the user.

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 08-11-2021

list = [11, 5, 17, 18, 23]
_sum = 0
ind = int(input("Enter The Index : "))

print("List Before Insertion : ", list)
list.pop(ind)
print("List After Insertion : ", list)


# Output

# Enter The Index : 2
# List Before Insertion :  [11, 5, 17, 18, 23]
# List After Insertion :  [11, 5, 18, 23]