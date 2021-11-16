# Print following pattern: 
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 6 
# 7 7 7 7 7 7 7 
# 8 8 8 8 8 8 8 8 
# 9 9 9 9 9 9 9 9 9


# By - Mayank Singh
# Date of Creation - 22-10-2021
# Last Modified - 25-10-2021

row = 9

for x in range(1, row+1):
    temp = x
    while(x>0):
        print(temp,'', end='')
        x -= 1
    
    print("")