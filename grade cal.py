# Student Grade Calculator

print("===== Student Grade Calculator =====")

name = input("Enter student name: ")

math = float(input("Enter Mathematics marks: "))
physics = float(input("Enter Physics marks: "))
chemistry = float(input("Enter Chemistry marks: "))
english = float(input("Enter English marks: "))
computer = float(input("Enter Computer marks: "))

total = math + physics + chemistry + english + computer
percentage = total / 500 * 100

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n===== Result =====")
print("Student:", name)
print("Total Marks:", total, "/ 500")
print("Percentage:", round(percentage, 2), "%")
print("Grade:", grade)