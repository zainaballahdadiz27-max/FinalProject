from Student import Student
from Course import Course
from Assessment import Quiz, Exam, Project
from Gradebook import Gradebook

print("=" * 50)
print("      STUDENT GRADE MANAGEMENT SYSTEM")
print("=" * 50)

options = ["1." "Add Student",
           "2." "Add Course",
           "3." "Enroll Student",
           "4." "Add Assessments",
           "5." "Record Grades",
           "6." "Calculate Average",
           "7." "Show Report\n", ]
for option in options:
    print(option)

user_choice = input("Choose an option: ")
print(user_choice)

# Step 1. Add Student
print("\nStep 1: Add Student")

student = Student("S001", "Ahmad Rahimi", "ahmad@example.com")

print("Student added successfully.\n")
student.display_info()

# Step 2. Add Course
print("\n" + "-" * 50)
print("Step 2: Add Course")

course = Course("PY101", "Python Programming")

print("Course added successfully.\n")
course.display_info()

# Step 3. Enroll student
print("\n" + "-" * 50)
print("Step 3: Enroll Student")

gradebook = Gradebook()

gradebook.add_student(student)
gradebook.add_course(course)

gradebook.enroll_student(student.student_id, course.course_code)

print("\nStudent", student.student_id,
      "is now enrolled in", course.course_code)

# Step 4. Add Assessments
print("\n" + "-" * 50)
print("Step 4: Add Assessments")

quiz = Quiz("Quiz 1", 10)
exam = Exam("Midterm Exam", 100)
project = Project("Final Project", 100)

gradebook.add_assessment(course.course_code, quiz)
gradebook.add_assessment(course.course_code, exam)
gradebook.add_assessment(course.course_code, project)

print()

for assessment in course.assessments:
    print(assessment.display_info())

# Step 5. Record Grades
print("\n" + "-" * 50)
print("Step 5: Record Grades")

gradebook.record_grade("S001", "PY101", "Quiz 1", 8)
gradebook.record_grade("S001", "PY101", "Midterm Exam", 75)
gradebook.record_grade("S001", "PY101", "Final Project", 90)

print("\nGrades Recorded")

print("Quiz 1        : 8 out of 10")
print("Midterm Exam  : 75 out of 100")
print("Final Project : 90 out of 100")

# Step 6. Calculate Average
print("\n" + "-" * 50)
print("Step 6: Calculate Average")

quiz_percent = quiz.calculate_percentage(8)
exam_percent = exam.calculate_percentage(75)
project_percent = project.calculate_percentage(90)

average = (quiz_percent + exam_percent + project_percent) / 3

print(f"Quiz 1        : {quiz_percent:.0f}%")
print(f"Midterm Exam  : {exam_percent:.0f}%")
print(f"Final Project : {project_percent:.0f}%")

print(f"\nAverage = ({quiz_percent:.0f} + {exam_percent:.0f} + {project_percent:.0f}) / 3")

print(f"Average = {average:.2f}%")

# Step 7. Show Report
print("\n" + "-" * 50)
print("Step 7: Show Report")

print("\n========== STUDENT REPORT ==========")

print(f"\nStudent ID : {student.student_id}")
print(f"Name       : {student.name}")
print(f"Email      : {student.email}")

print(f"\nCourse : {course.course_code} - {course.course_name}")

print("\nGrades")

print(f"Quiz 1        : 8/10   = {quiz_percent:.0f}%")
print(f"Feedback      : {quiz.grade_message(8)}")

print()

print(f"Midterm Exam  : 75/100 = {exam_percent:.0f}%")
print(f"Feedback      : {exam.grade_message(75)}")

print()

print(f"Final Project : 90/100 = {project_percent:.0f}%")
print(f"Feedback      : {project.grade_message(90)}")

print("\nAverage :", format(average, ".2f"), "%")

if average >= gradebook.passing_grade:
    print("Result  : PASSED")
else:
    print("Result  : FAILED")

print("\n" + "=" * 50)
print("End of Program")
print("=" * 50)
