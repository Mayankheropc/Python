# Python function that takes a list of words and returns the length of the longest one.

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 07-11-2021

def longest_word(mylist):
    temp = 0
    ans = ""
    for i in mylist:
        if len(i)> temp:
            temp = len(i)
            ans = i
    return ans


name = []
size = int(input("Total elements in the list: "))

x = 1

while(len(name)<size):
    name.append(input("Enter " + str(x) + " Name : "))
    x += 1

longest = longest_word(name)

print("Longest name in the list is:", longest)

# Output

# Total elements in the list: 5
# Enter 1 Name : Mayank
# Enter 2 Name : Aman
# Enter 3 Name : Chetan
# Enter 4 Name : Chitransh
# Enter 5 Name : Harshad
# Longest name in the list is: Chitransh