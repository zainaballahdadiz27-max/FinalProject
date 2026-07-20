from Student import Student
from Course import Course
from Assessment import Quiz, Exam, Project
from gradebook import Gradebook

gradebook = Gradebook()
while True:
    print("\n========== STUDENT GRADE MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student")
    print("4. Add Assessment")
    print("5. Record Grade")
    print("6. Calculate Average")
    print("7. Show Report")
    print("8. Delete Student")
    print("9. Teacher Comment")
    print("10. Dashboard")
    print("11. Exit")

    choice = input("Enter your choice: ")

    # ----------------------------
    # Step 1 - Add Student
    # ----------------------------
    if choice == "1":
        student_id = input("Student ID: ")
        name = input("Student Name: ")
        email = input("Email: ")

        student = Student(student_id, name, email)
        gradebook.add_student(student)

        print("\nStudent added successfully!")

    # ----------------------------
    # Step 2 - Add Course
    # ----------------------------
    elif choice == "2":
        course_code = input("Course Code: ")
        course_name = input("Course Name: ")

        course = Course(course_code, course_name)
        gradebook.add_course(course)

        print("\nCourse added successfully!")

    # ----------------------------
    # Step 3 - Enroll Student
    # ----------------------------
    elif choice == "3":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")

        gradebook.enroll_student(student_id, course_code)

    # ----------------------------
    # Step 4 - Add Assessment
    # ----------------------------
    elif choice == "4":
        course_code = input("Course Code: ")

        print("Assessment Types")
        print("1. Quiz")
        print("2. Exam")
        print("3. Project")

        assessment_type = input("Choose assessment: Type 1 for Quiz, Type 2 for Exam, Type 3 for Project: ")

        title = input("Assessment Title: ")
        max_score = int(input("Maximum Score: "))

        if assessment_type == "1":
            assessment = Quiz(title, max_score)

        elif assessment_type == "2":
            assessment = Exam(title, max_score)

        elif assessment_type == "3":
            assessment = Project(title, max_score)

        else:
            print("Invalid choice.")
            continue

        gradebook.add_assessment(course_code, assessment)

    # ----------------------------
    # Step 5 - Record Grade
    # ----------------------------
    elif choice == "5":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")
        assessment_title = input("Assessment Title: ")
        score = float(input("Score: "))

        gradebook.record_grade(student_id, course_code, assessment_title, score)

    # ----------------------------
    # Step 6 - Calculate Average
    # ----------------------------
    elif choice == "6":
        student_id = input("Student ID: ")
        course_code = input("Course Code: ")

        average = gradebook.calculate_average(student_id, course_code)

        if average is not None:
            print(f"\nAverage Score = {average:.2f}")
        else:
            print("No grades found.")

    # ----------------------------
    # Step 7 - Show Report
    # ----------------------------
    elif choice == "7":
        student_id = input("Student ID: ")
        gradebook.show_report(student_id)

    # ----------------------------
    # Step 8 - Delete Student
    # ----------------------------
    elif choice == "8":
        student_id = input("Student ID: ")
        gradebook.delete_student(student_id)

    # ----------------------------
    # Step 9 - Teacher Comment
    # ----------------------------
    elif choice == "9":
        student_id = input("Student ID: ")

        comment = input("Enter teacher comment: ")

        gradebook.teacher_comments(student_id, comment)

    # ----------------------------
    # Step 10 - Dashboard
    # ----------------------------
    elif choice == "10":
        gradebook.dashboard()

    # ----------------------------
    # Exit
    # ----------------------------
    elif choice == "11":

        print("Thank you for using the Student Grade Management System.")
        break

    else:
        print("Invalid choice. Please try again.")



# ****************************
# Create gradebook Object
# ****************************
# gradebook = Gradebook()
#
# # ****************************
# # Create Student Objects
# # ****************************
# student1 = Student("S001", "Ahmad Rahmi", "ahmad@gmail.com")
# student2 = Student("S002", "Sara Noori", "sara@gmail.com")
#
# # **************************
# # Create Course Objects
# # **************************
# course1 = Course("PY101", "Python Programming")
# course2 = Course("DB101", "Database Systems")
#
# # *******************************
# # Create Assessment Objects
# # *******************************
# quiz1 = Quiz("Quiz 1", 10)
# quiz2 = Quiz("Quiz 2", 10)
#
# exam1 = Exam("Midterm Exam", 100)
# exam2 = Exam("Final Exam", 100)
#
# project1 = Project("Final Project", 100)
#
# # *******************************
# # Add students to Gradebook
# # *******************************
# gradebook.add_student(student1)
# gradebook.add_student(student2)
#
# # *******************************
# # Add courses to Gradebook
# # *******************************
# gradebook.add_course(course1)
# gradebook.add_course(course2)
#
# # *******************************
# # Add assessments to courses
# # *******************************
# gradebook.add_assessment("PY101", quiz1)
# gradebook.add_assessment("PY101", exam1)
# gradebook.add_assessment("PY101", project1)
#
# gradebook.add_assessment("DB101", quiz2)
# gradebook.add_assessment("DB101", exam2)
#
# # ****************************
# # Enroll Students
# # ****************************
# gradebook.enroll_student("S001", "PY101")
# gradebook.enroll_student("S001", "DB101")
# gradebook.enroll_student("S002", "PY101")
#
# # **************************
# # Record Grades
# # **************************
# gradebook.record_grade("S001", "PY101", "Quiz 1", 8)
# gradebook.record_grade("S001", "PY101", "Midterm Exam", 75)
# gradebook.record_grade("S001", "PY101", "Final Project", 90)
#
# gradebook.record_grade("S001", "DB101", "Quiz 2", 9)
# gradebook.record_grade("S001", "DB101", "Final Exam", 88)
#
# gradebook.record_grade("S002", "PY101", "Quiz 1", 7)
# gradebook.record_grade("S002", "PY101", "Midterm Exam", 65)
# gradebook.record_grade("S002", "PY101", "Final Project", 80)
#
# # ***************************
# # Add Teacher comments
# # ***************************
# gradebook.teacher_comments(
#     "S001",
#     "Good job! Keep improving your programming skills."
# )
# gradebook.teacher_comments(
#     "S002",
#     "Good effort. Focus on improving your exam performance."
# )
#
# # ***********************
# # Dashboard
# # ***********************
# gradebook.dashboard()
#
# # **************************
# # Calculate Average
# # **************************
# average = gradebook.calculate_average("S001", "PY101")
# print(f"Average: {average:.2f}")
#
# # *************************
# # Show Reports
# # *************************
# gradebook.show_report("S001")
# gradebook.show_report("S002")


