# Pyhon progrm to print following pattern: 
# A 
# BB 
# CCC 
# DDDD 
# EEEEE 
# FFFFFF 
# GGGGGGG 
# HHHHHHHH

# By - Mayank Singh
# Date of Creation - 22-10-2021
# Last Modified - 25-10-2021

row = 8

# ASCII number of 'A'
temp = 65

for x in range(1, row+1):
    while(x>0):
        print(chr(temp), end='')
        x -= 1
    temp += 1    
    print("")