# Print following pattern: 
# 1 
# 12 
# 123 
# 1234 
# 12345 
# 123456 
# 1234567 
# 12345678 
# 123456789

# By - Mayank Singh
# Date of Creation - 22-10-2021
# Last Modified - 25-10-2021

row = 9

for x in range(1, row+1):
    temp = 1
    while(x>0):
        print(temp, end='')
        x -= 1
        temp += 1    
    print("")