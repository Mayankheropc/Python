# to check that tuple cannot be changed in python
# By - Mayank Singh
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

tuple=(1,3,5,8)
tuple[2]=7
print(tuple)

# TypeError: 'tuple' object does not support item assignment
# output : [1,3,7,8] for list