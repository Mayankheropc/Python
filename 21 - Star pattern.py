# Print the following pattern
#    * 
#    * * 
#    * * * 
#    * * * * 
#    * * * * * 
#    * * * * 
#    * * * 
#    * * 
#    *

# By - Mayank Singh
# Date of Creation - 22-10-2021
# Last Modified - 25-10-2021

for i in range(1, 6):
    temp = i
    while temp>0:
        print("* ", end="")
        temp -= 1
    print("")
    
for i in range(1, 5):
    temp = 5
    temp -= i
    while temp>0:
        print("* ", end="")
        temp -= 1
    print("")