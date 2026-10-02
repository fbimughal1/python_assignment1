# [grade_calculator.py]
# Author: [Obaid ur Rahman]
# Date: [29/09/2026]
# Description: [The script will take a score from user as input and display the corresponding grade.]

score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
