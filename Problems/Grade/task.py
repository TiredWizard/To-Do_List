grade = int(input())
max_grade = int(input())

grade_percentage = (grade / max_grade) * 100


if grade_percentage < 60:
    print("F")
elif 60 <= grade_percentage < 70:
    print("D")
elif 70 <= grade_percentage < 80:
    print("C")
elif 80 <= grade_percentage < 90:
    print("B")
elif 90 <= grade_percentage <= 100:
    print("A")
