# Python program to accept the sting of even length
# By - Mayank Singh
# Date of Creation - 08-10-2021
# Last Modified - 08-10-2021
string = input("enter the string : ")  
count = 0;  
   
#Counts each character except space  
for i in range(0, len(string)):  
    if(string[i] != ' '):  
        count = count + 1;  
   
#count the total number of characters present in the given string  
num = int(str(count));  
if (num % 2) == 0:  
   print("{0} Accepted".format(num))  
else:  
   print("{0} not Accepted".format(num))  
