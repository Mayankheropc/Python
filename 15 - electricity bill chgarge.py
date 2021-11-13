# Write a program to input electricity unit charges and calculate total electricity bill according to the given 
# condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

# By - Mayank Singh
# Date of Creation - 21-10-2021
# Last Modified - 25-10-2021

# initialization
charge = 0
total = 0
temp = 0

unit = float(input("Total units consumed: "))

if unit>250:
    temp = unit-250
    charge = 1.50
    total += temp*charge
    unit -= temp     #updating units left to calculate

if unit>150:
    temp = unit-150
    charge = 1.20
    total += temp*charge
    unit -= temp     #updating units left to calculate

if unit>50:
    temp = unit-50
    charge = 0.75
    total += temp*charge
    unit -= temp     #updating units left to calculate

if unit>0:
    charge = 0.50
    total += unit*charge

print("Your electricity bill: ", total)