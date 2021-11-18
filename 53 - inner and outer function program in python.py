# Create an outer function that will accept three parameters, a, b and c. 
# Create an inner function inside an outer function that will calculate the addition of a, b and c. 
# At last, an outer function will add 5 into addition and return it

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

def outerfunction(a, b, c):

    def innerfunction(x, y, z):
        return x+y+z
    
    return (5 + innerfunction(a, b, c))      # Calling the inner function

x = int(input("Enter 1st no: "))
y = int(input("Enter 2nd no: "))
z = int(input("Enter 3rd no: "))

print(outerfunction(x, y, z))

# Output

# Enter 1st no: 5
# Enter 2nd no: 5
# Enter 3rd no: 5
# 20

# Enter 1st no: 2
# Enter 2nd no: 4
# Enter 3rd no: 5
# 16