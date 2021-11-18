# Write a function that computes the area of a rectangle. Then, write a second function that calls this function 
# three times to compute the surface area of a rectangular solid

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

def arearect(x, y):
    return x*y

def surfacearea(x, y, z):
    return  2 * ( arearect(x,y) + arearect(y,z) + arearect(z,x))

a = int(input("Enter length: "))
b = int(input("Enter  width: "))
c = int(input("Enter height: "))

area = arearect(a,b)
surfarea = surfacearea(a,b,c)

print("Area of rectangle of length =", a, "width =",b , "is: ", area)
print("Surfacearea of rectangular solif of length =", a, "width =",b , "height =", c, "is: ", surfarea)

# Output

# Enter length: 5
# Enter  width: 2
# Enter height: 1
# Area of rectangle of length = 5 width = 2 is:  10
# Surfacearea of rectangular solif of length = 5 width = 2 height = 1 is:  34