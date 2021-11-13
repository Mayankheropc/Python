# Take input of age of 3 people by user and determine oldest and youngest among them.
# By - Mayank Singh
# Date of Creation - 20-10-2021
# Last Modified - 25-10-2021

a = int(input("Enter 1st person age: "))
b = int(input("Enter 2nd person age: "))
c = int(input("Enter 3rd person age: "))

youngest = ""
oldest = ""

# for youngest
if a<b and a<c:
    youngest = "1st Person"
elif b<a and b<c:
    youngest = "2nd Person"
else:
    youngest = "3rd Person"

# for oldest
if a>b and a>c:
    oldest = "1st Person"
elif b>a and b>c:
    oldest = "2nd Person"
else:
    oldest = "3rd Person"

print(youngest + " is youngest")
print(oldest + " is oldest")