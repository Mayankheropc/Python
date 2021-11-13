# Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. 
# Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage  < 40% : Grade F

#assuming all marks are out of 100

physics = float(input("Enter marks in physics: "))
chemistry = float(input("Enter marks in chemistry: "))
biology = float(input("Enter marks in biology: "))
mathematics = float(input("Enter marks in mathematics: "))
computer = float(input("Enter marks in computer: "))

total = physics + chemistry + biology + mathematics + computer
percentage = total/5 
grade = "F"     #initilization

if percentage >= 90:
    grade = "A"
elif percentage >=80:
    grade = "B"   
elif percentage >=70:
    grade = "C"
elif percentage >=60:
    grade = "D"  
elif percentage >=40:
    grade = "E" 
else:
    grade = "F" 

print("Total Marks out of 500 = ", total)
print("Percentage = ", percentage)
print("Grade = " + grade)