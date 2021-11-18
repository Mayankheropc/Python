# Write a function that returns the middle value among three integers. 
# Write code to test this function with different inputs

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

def middle(a, b, c):
    if a>b and a>c:     # if a is largest
        if b<c:             # if b is smallest
            return c            # then c will be the middle no.
        else:               # if c is smallest
            return b            # then b will be the middle no.
    
    elif b>a and b>c:     # if b is largest
        if a<c:             # if a is smallest
            return c            # then c will be the middle no.
        else:               # if c is smallest
            return a            # then a will be the middle no.

    else:                 # if c is largest
        if b<a:             # if b is smallest
            return a            # then a will be the middle no.
        else:               # if a is smallest
            return b            # then b will be the middle no.


x = int(input("Enter 1st no: "))
y = int(input("Enter 2nd no: "))
z = int(input("Enter 3rd no: "))

middleno = middle(x,y,z)

print("middle no. will be:", middleno)


# Output

# Enter 1st no: 45
# Enter 2nd no: 80
# Enter 3rd no: 10
# middle no. will be: 45

# Enter 1st no: 18
# Enter 2nd no: 5
# Enter 3rd no: 50
# middle no. will be: 18