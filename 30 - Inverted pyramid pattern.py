# Pyhon program to print Inverted pyramid pattern using *

#    * * * * *
#    * * * *
#    * * *
#    * *
#    *

# By - Mayank Singh
# Date of Creation - 22-10-2021
# Last Modified - 25-10-2021


size = int(input("Enter the size/no. of rows: "))

for i in reversed( range (1, size+1)):
    
    while(i>0):
        print("* ", end='')
        i -=1
    
    print("")