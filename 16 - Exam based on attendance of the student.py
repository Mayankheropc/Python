# A student will not be allowed to sit in exam if his/her attendence is less than 80%.
# Take following input from user:
# Total Number of classes held
# Total Number of classes attended.
# And print percentage of class attended. print student is allowed to sit in exam or not.

# By - Mayank Singh
# Date of Creation - 21-10-2021
# Last Modified - 25-10-2021

# initialization
totalclasses = 0
totalattend = 0
flag = 0    # zero means not allowed & one means allowed

totalclasses = int(input("Enter total no. of classes held: "))
totalattend = int(input("Enter total no. of classes attend: "))
percentage = (totalattend/totalclasses)*100

print("Percentage: ", percentage, "%")

if percentage>=80:
    print("Allowed to sit in exam!")
else:
    print("Not allowed to sit in exam!")