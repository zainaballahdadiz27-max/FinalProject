# from Student import Student
# from Course import Course
# from Assessment import Quiz, Exam, Project
# from gradebook import gradebook
#
# # Create gradebook object
# gradebook = gradebook()
#
#
#
#
# while True:
#     print("=" * 50)
#     print("      STUDENT GRADE MANAGEMENT SYSTEM")
#     print("=" * 50)
#
#     options = ["1." "Add Student",
#                "2." "Add Course",
#                "3." "Enroll Student",
#                "4." "Add Assessments",
#                "5." "Record Grades",
#                "6." "Calculate Average",
#                "7." "Show Report\n", ]
#     for option in options:
#         print(option)
#
#     user_choice = input("Choose an option: ")
#     print(user_choice)
#
#     # Step 1. Add Student
#     if user_choice == "1":
#
#         print("\nStep 1: Add Student")
#
#         student = Student("S001", "Ahmad Rahimi", "ahmad@example.com")
#
#         print("Student added successfully.\n")
#         student.display_info()
#
#     elif user_choice == "2":
#         # Step 2. Add Course
#         print("\n" + "-" * 50)
#         print("Step 2: Add Course")
#
#         course = Course("PY101", "Python Programming")
#
#         print("Course added successfully.\n")
#         course.display_info()
#
#     elif user_choice == "3":
#         # Step 3. Enroll student
#         print("\n" + "-" * 50)
#         print("Step 3: Enroll Student")
#
#         gradebook = gradebook()
#
#         gradebook.add_student(student)
#         gradebook.add_course(course)
#
#         gradebook.enroll_student(student.student_id, course.course_code)
#
#         print("\nStudent", student.student_id,
#               "is now enrolled in", course.course_code)
#
#     elif user_choice == "4":
#         # Step 4. Add Assessments
#         print("\n" + "-" * 50)
#         print("Step 4: Add Assessments")
#
#         quiz = Quiz("Quiz 1", 10)
#         exam = Exam("Midterm Exam", 100)
#         project = Project("Final Project", 100)
#
#         gradebook.add_assessment(course.course_code, quiz)
#         gradebook.add_assessment(course.course_code, exam)
#         gradebook.add_assessment(course.course_code, project)
#
#         print()
#
#         for assessment in course.assessments:
#             print(assessment.display_info())
#
#     elif user_choice == "5":
#         # Step 5. Record Grades
#         print("\n" + "-" * 50)
#         print("Step 5: Record Grades")
#
#         gradebook.record_grade("S001", "PY101", "Quiz 1", 8)
#         gradebook.record_grade("S001", "PY101", "Midterm Exam", 75)
#         gradebook.record_grade("S001", "PY101", "Final Project", 90)
#
#         print("\nGrades Recorded")
#
#         print("Quiz 1        : 8 out of 10")
#         print("Midterm Exam  : 75 out of 100")
#         print("Final Project : 90 out of 100")
#
#     elif user_choice == "6":
#         # Step 6. Calculate Average
#         print("\n" + "-" * 50)
#         print("Step 6: Calculate Average")
#
#         quiz_percent = quiz.calculate_percentage(8)
#         exam_percent = exam.calculate_percentage(75)
#         project_percent = project.calculate_percentage(90)
#
#         average = (quiz_percent + exam_percent + project_percent) / 3
#
#         print(f"Quiz 1        : {quiz_percent:.0f}%")
#         print(f"Midterm Exam  : {exam_percent:.0f}%")
#         print(f"Final Project : {project_percent:.0f}%")
#
#         print(f"\nAverage = ({quiz_percent:.0f} + {exam_percent:.0f} + {project_percent:.0f}) / 3")
#
#         print(f"Average = {average:.2f}%")
#
#     elif user_choice == "7":
#         # Step 7. Show Report
#         print("\n" + "-" * 50)
#         print("Step 7: Show Report")
#
#         print("\n========== STUDENT REPORT ==========")
#
#         print(f"\nStudent ID : {student.student_id}")
#         print(f"Name       : {student.name}")
#         print(f"Email      : {student.email}")
#
#         print(f"\nCourse : {course.course_code} - {course.course_name}")
#
#         print("\nGrades")
#
#         print(f"Quiz 1        : 8/10   = {quiz_percent:.0f}%")
#         print(f"Feedback      : {quiz.grade_message(8)}")
#
#         print()
#
#         print(f"Midterm Exam  : 75/100 = {exam_percent:.0f}%")
#         print(f"Feedback      : {exam.grade_message(75)}")
#
#         print()
#
#         print(f"Final Project : 90/100 = {project_percent:.0f}%")
#         print(f"Feedback      : {project.grade_message(90)}")
#
#         print("\nAverage :", format(average, ".2f"), "%")
#
#         if average >= gradebook.passing_grade:
#             print("Result  : PASSED")
#         else:
#             print("Result  : FAILED")
#
#         print("\n" + "=" * 50)
#         print("End of Program")
#         print("=" * 50)
#
#     else:
#         print("Invalid Choice!")
#         break


from Student import Student
from Course import Course
from Assessment import Quiz, Exam, Project
from gradebook import Gradebook


#
# while True:
#     print("\n========== STUDENT GRADE MANAGEMENT SYSTEM ==========")
#     print("1. Add Student")
#     print("2. Add Course")
#     print("3. Enroll Student")
#     print("4. Add Assessment")
#     print("5. Record Grade")
#     print("6. Calculate Average")
#     print("7. Show Report")
#     print("8. Exit")
#
#     choice = input("Enter your choice: ")
#
#     # ----------------------------
#     # Step 1 - Add Student
#     # ----------------------------
#     if choice == "1":
#         student_id = input("Student ID: ")
#         name = input("Student Name: ")
#         email = input("Email: ")
#
#         student = Student(student_id, name, email)
#         gradebook.add_student(student)
#
#         print("\nStudent added successfully!")
#
#     # ----------------------------
#     # Step 2 - Add Course
#     # ----------------------------
#     elif choice == "2":
#         course_code = input("Course Code: ")
#         course_name = input("Course Name: ")
#
#         course = Course(course_code, course_name)
#         gradebook.add_course(course)
#
#         print("\nCourse added successfully!")
#
#     # ----------------------------
#     # Step 3 - Enroll Student
#     # ----------------------------
#     elif choice == "3":
#         student_id = input("Student ID: ")
#         course_code = input("Course Code: ")
#
#         gradebook.enroll_student(student_id, course_code)
#
#     # ----------------------------
#     # Step 4 - Add Assessment
#     # ----------------------------
#     elif choice == "4":
#         course_code = input("Course Code: ")
#
#         print("Assessment Types")
#         print("1. Quiz")
#         print("2. Exam")
#         print("3. Project")
#
#         assessment_type = input("Choose assessment: Type 1 for Quiz, Type 2 for Exam, Type 3 for Project: ")
#
#         title = input("Assessment Title: ")
#         max_score = int(input("Maximum Score: "))
#
#         if assessment_type == "1":
#             assessment = Quiz(title, max_score)
#
#         elif assessment_type == "2":
#             assessment = Exam(title, max_score)
#
#         elif assessment_type == "3":
#             assessment = Project(title, max_score)
#
#         else:
#             print("Invalid choice.")
#             continue
#
#         gradebook.add_assessment(course_code, assessment)
#
#     # ----------------------------
#     # Step 5 - Record Grade
#     # ----------------------------
#     elif choice == "5":
#         student_id = input("Student ID: ")
#         course_code = input("Course Code: ")
#         assessment_title = input("Assessment Title: ")
#         score = float(input("Score: "))
#
#         gradebook.record_grade(student_id, course_code, assessment_title, score)
#
#     # ----------------------------
#     # Step 6 - Calculate Average
#     # ----------------------------
#     elif choice == "6":
#         student_id = input("Student ID: ")
#         course_code = input("Course Code: ")
#
#         average = gradebook.calculate_average(student_id, course_code)
#
#         if average is not None:
#             print(f"\nAverage Score = {average:.2f}")
#         else:
#             print("No grades found.")
#
#     # ----------------------------
#     # Step 7 - Show Report
#     # ----------------------------
#     elif choice == "7":
#         student_id = input("Student ID: ")
#         course_code = input("Course Code: ")
#
#         gradebook.show_report(student_id, course_code)
#
#     # ----------------------------
#     # Exit
#     # ----------------------------
#     elif choice == "8":
#         print("Thank you for using the Student Grade Management System.")
#         break
#
#     else:
#         print("Invalid choice. Please try again.")





# Create Student Objects
student1 = Student("S001", "Ahmad Rahmi", "ahmad@gmail.com")
student2 = Student("S002", "Sara Ali", "sara@gmail.com")

# Create Course Objects
course1 = Course("PY101", "Python Programming")
course2 = Course("DB101", "Database Systems")

# Create Assessment Objects
quiz1 = Quiz("Quiz 1", 10)
quiz2 = Quiz("Quiz 2", 10)

exam1 = Exam("Midterm Exam", 100)
exam2 = Exam("Final Exam", 100)

project1 = Project("Final Project", 100)

# Create gradebook Object
gradebook = Gradebook()

# Add the objects to the gradebook
# Add students
gradebook.add_student(student1)
gradebook.add_student(student2)

# Add courses
gradebook.add_course(course1)
gradebook.add_course(course2)

# Add assessments
gradebook.add_assessment("PY101", quiz1)
gradebook.add_assessment("PY101", exam1)
gradebook.add_assessment("PY101", project1)

gradebook.add_assessment("DB101", quiz2)
gradebook.add_assessment("DB101", exam2)

# Enroll Students
gradebook.enroll_student("S001", "PY101")
gradebook.enroll_student("S001", "DB101")

gradebook.enroll_student("S002", "PY101")

# Record Grades
gradebook.record_grade("S001", "PY101", "Quiz 1", 8)
gradebook.record_grade("S001", "PY101", "Midterm Exam", 75)
gradebook.record_grade("S001", "PY101", "Final Project", 90)

gradebook.record_grade("S002", "PY101", "Quiz 1", 7)
gradebook.record_grade("S002", "PY101", "Midterm Exam", 65)
gradebook.record_grade("S002", "PY101", "Final Project", 80)

# Calculate Average
average = gradebook.calculate_average("S001", "PY101")
print(f"Average: {average:.2f}")

# Show Report
gradebook.show_report("S001")

# Search student
# Example Usage
student = gradebook.search_student("S001")

if student:
    student.display_info()
else:
    print("Student not found.")

gradebook.search_student("S001")

# Delete student
gradebook.delete_student("S001")