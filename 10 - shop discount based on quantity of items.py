# A shop will give discount of 50% if the cost of purchased quantity is more than 10000. Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.
# By - Mayank Singh
# Date of Creation - 29-10-2021
# Last Modified - 29-10-2021


price = 100         #price of a item
amount = 0          #initial amount

quantity = int(input("Enter quantity: "))

if quantity > 10000:
    discount = 0.5  # 50% discount
    amount = float(quantity*price*discount)
else:
    amount = price*quantity

print("Total price to pay: ", amount)