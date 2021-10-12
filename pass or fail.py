# program to find out whether a student is pass or fail, if it 
# requires total 40% and at least 33% in each subject to pass. Assume 
# 3 subjects and take marks as an input from the user

# By - Mayank Singh
# Date of Creation - 09-10-2021
# Last Modified - 09-10-2021

marks = []
subject = int(input("enter total no. of subjects: "))
x = 1
while(len(marks)<subject):
    marks.append(int(input("Enter subject " + str(x) + " marks: ")))
    x += 1
y = 0
flag = 0
for y in range(0, subject):
    if(marks[y] < 33):
        flag = 1
        break

if(flag==0):
    total = sum(marks)
    avg = total/subject
    if(avg<40):
        flag=1

if(flag==0):
    print("pass")
else:
    print("fail!")