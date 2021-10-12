# program to greet all the person names stored in a list L1 and 
# which starts with S. (hint: use startswith(“S”) method)
# L1 = [“Simarjeet”, “Sohan”, “Sachin”, “Rahul”]

# By - Mayank Singh
# Date of Creation - 28-09-2021
# Last Modified - 28-09-2021

l1 = ["simarjeet", "sonah", "sachin", "rahul"]
for ele in l1:
    if(ele.startswith("s")):
        print("Hello " + ele)
