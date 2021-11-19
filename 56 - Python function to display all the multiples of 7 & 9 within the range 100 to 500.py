# Python function to display all the multiples of 7 & 9 within the range 100 to 500

# By - Mayank Singh
# Date of Creation - 08-11-2021
# Last Modified - 10-11-2021

def multi7(range):
    count = 7
    while(count<range):
        print(count, end=" ")
        count += 7
    print("")

def multi9(range):
    count = 9
    while(count<range):
        print(count, end=" ")
        count += 9
    print("")

x = int(input("Enter the range (100 to 500): "))

if x>=100 and x<=500:
    print("Multiple of 7: ")
    multi7(x)
    print("Multiple of 9: ")
    multi9(x)
else:
    print("Not in range!")

# Output

# Enter the range (100 to 500): 150
# Multiple of 7: 
# 7 14 21 28 35 42 49 56 63 70 77 84 91 98 105 112 119 126 133 140 147
# Multiple of 9:
# 9 18 27 36 45 54 63 72 81 90 99 108 117 126 135 144

# Enter the range (100 to 500): 50
# Not in range!