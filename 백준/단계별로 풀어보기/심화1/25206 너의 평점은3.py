summation_grade = 0
summation_credit = 0
for _ in range(20):
    subject, credit, grade = input().split()
    if grade == 'P':
        continue
    if grade == 'F':
        summation_credit += float(credit)
    else:
        grade_in_number = 4.5 - (ord(grade[0]) - ord('A'))
        if grade[1] == '0':
            grade_in_number -= 0.5
        summation_grade += float(credit) * grade_in_number
        summation_credit += float(credit)

GPA = summation_grade/summation_credit

print(GPA)
