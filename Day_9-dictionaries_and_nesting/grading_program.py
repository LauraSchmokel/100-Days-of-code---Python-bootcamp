# Day 9 - Dictionaries and Nesting (Exercise: Grading Program)
# Topics: dictionaries, for loops through key-value pairs, nested conditionals
# What I learned: how to loop through a dictionary and build a new one with transformed data

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if student_scores[key] > 90 and student_scores[key] <= 100:
        student_grades[key] = "Outstanding"

    elif student_scores[key] > 80 and student_scores[key] <= 90:
         student_grades[key] = "Exceeds Expectations"

    elif student_scores[key] > 70 and student_scores[key] <= 80:
         student_grades[key] = "Acceptable"

    elif student_scores[key] <= 70:
         student_grades[key] = "Fail"

print(student_grades)