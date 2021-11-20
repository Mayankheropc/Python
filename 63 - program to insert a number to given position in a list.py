# program to insert a number to given position in a list.

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 08-11-2021

list = [11, 5, 17, 18, 23]
ind = int(input("Enter The Index : "))
ele = int(input("Enter The Number To Insert : "))

print("List Before Insertion : ", list)
list.insert(ind, ele)
print("List After Insertion : ", list)



# Output

# Enter The Index : 2
# Enter The Number To Insert : 51
# List Before Insertion :  [11, 5, 17, 18, 23]
# List After Insertion :  [11, 5, 51, 17, 18, 23]