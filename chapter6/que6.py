Marks = int(input("Enter Marks: "))

if Marks>=90:
    grade = "Ex"
elif Marks>=80:
    grade = "A"
elif Marks>=70:
    grade = "B"
elif Marks>=60:
    grade = "C"
elif Marks>=50:
    grade = "D" 
else:
    grade = "F"

print("Your grade is " + grade)