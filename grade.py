# Python program to calculate the grade of a student from his marks of 
# the following scheme: 
# 90-100: Excellent
# 80-90: A
# 70-80: B
# 60-70: C
# 50-60: D
# Less than 50 : Fail

# By - Mayank Singh
# Date of Creation - 01-10-2021
# Last Modified - 09-10-2021

marks = []
x = 1
while(len(marks)<5):
    marks.append(input("Enter Subject " + str(x) + " marks out of 100: "))
    x += 1

total = 0

for ele in range(0, len(marks)):
    total += int(marks[ele])

percent = total/5
print("GRADE:")
if (percent>90):
    print("Excellent")
elif (percent>80) and (percent<=90):
    print("A")
elif (percent>70) and (percent<=80):
    print("B")
elif (percent>60) and (percent<=70):
    print("C")
elif (percent>50) and (percent<=60):
    print("D")
else:
    print("Fail")