# Calculate income tax for the given income by adhering to the below rules
# Taxable Income Rate (in %)
# First Rs.10,0000 - 0
# Next Rs. 10,0000 - 10
# The remaining - 20

# By - Mayank Singh
# Date of Creation - 22-10-2021
# Last Modified - 25-10-2021

# initialization
charge = 0
tax = 0
temp = 0

income = float(input("Enter your Income: "))

if income>20000:
    temp = income - 20000
    charge = 20
    tax += (temp/100)*charge
    income = income - temp

if income>10000:
    temp = income - 10000
    charge = 10
    tax += (temp/100)*charge
    income = income - temp

print("Tax you have to pay: RS", tax, "/-")