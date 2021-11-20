# Python program to generate all sublists of a list

# By - Mayank Singh
# Date of Creation - 07-11-2021
# Last Modified - 12-11-2021

def sub_lists(l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists


list = [11, 5, 17, 18, 23]

print("List : ", list)
print("Sublist Of List : ", sub_lists(list))



# Output

# List :  [11, 5, 17, 18, 23]
# Sublist Of List :  [[], [11], [11, 5], [5], [11, 5, 17],
# [5, 17], [17], [11, 5, 17, 18], [5, 17, 18], [17, 18], 
# [18], [11, 5, 17, 18, 23], [5, 17, 18, 23], [17, 18, 23], 
# [18, 23], [23]]