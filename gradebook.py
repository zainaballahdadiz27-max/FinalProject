# Creates a new Gradebook object.
# Initializes dictionaries for students, courses, and grades, and sets the passing grade.
class Gradebook:
    def __init__(self):
        self.students = {}        # Key: student_id, Value: Student object
        self.courses = {}         # Key: course_code, Value: Course object
        self.grades = {}          # Stores students' grades
        self.passing_grade = 55

    # Adds a Student object to the student's dictionary.
    def add_student(self, student):
        self.students[student.student_id] = student

    # Adds a Course object to the course's dictionary.
    def add_course(self, course):
        self.courses[course.course_code] = course


    # Enrolls a student in a course if both exist.
    def enroll_student(self, student_id, course_code):

        if student_id in self.students and course_code in self.courses:

            student = self.students[student_id]
            course = self.courses[course_code]

            student.enroll_course(course_code)
            course.add_student(student)

            if student_id not in self.grades:
                self.grades[student_id] = {}

            self.grades[student_id][course_code] = {}

            print("Student enrolled successfully.")

        else:
            print("Student or course not found.")

    # Adds an assessment (Quiz, Exam, or Project) to a course.
    def add_assessment(self, course_code, assessment):
        if course_code in self.courses:
            self.courses[course_code].add_assessment(assessment)
            print("Assessment added successfully.")
        else:
            print("Course not found.")

    # Records a student's score for an assessment.
    def record_grade(self, student_id, course_code, assessment_title, score):

        if student_id not in self.students:
            print("Student not found.")
            return

        if course_code not in self.courses:
            print("Course not found.")
            return

        assessment = self.courses[course_code].find_assessment(assessment_title)

        if assessment is None:
            print("Assessment not found.")
            return

        if student_id not in self.grades:
            self.grades[student_id] = {}

        if course_code not in self.grades[student_id]:
            self.grades[student_id][course_code] = {}

        self.grades[student_id][course_code][assessment_title] = (assessment, score)

        print("Grade recorded successfully.")

    # Calculates the average grade for one student in one course.
    def calculate_average(self, student_id, course_code):

        if student_id not in self.grades:
            return None

        if course_code not in self.grades[student_id]:
            return None

        scores = list(self.grades[student_id][course_code].values())

        if not scores:
            return 0
        return sum(scores) / len(scores)

    # Shows a complete report for one student.
    # The report includes student information, enrolled courses, grades, average score, letter grade, and pass/fail result.
    def show_report(self, student_id):

        if student_id not in self.students:
            print("Student not found.")
            return

        student = self.students[student_id]

        print("\n========== STUDENT REPORT ==========")
        print(f"Student ID : {student.student_id}")
        print(f"Name       : {student.name}")
        print(f"Email      : {student.email}")

        if student_id not in self.grades:
            print("\nNo grades found.")
            return

        # Loop through every course
        for course_code, assessments in self.grades[student_id].items():

            course = self.courses[course_code]

            print(f"\nCourse : {course.course_name}")
            print("-" * 45)

            total_percentage = 0
            count = 0

            # Loop through every assessment
            for title, data in assessments.items():
                assessment = data[0]
                score = data[1]

                percentage = assessment.calculate_percentage(score)

                print(f"{title}")
                print(f"Score      : {score}/{assessment.max_score}")
                print(f"Percentage : {percentage:.2f}%")

                print(f"Feedback   : {assessment.grade_message(score)}")
                print()

                total_percentage += percentage
                count += 1

            average = total_percentage / count

            # Letter Grade
            if average >= 90:
                letter = "A"
            elif average >= 80:
                letter = "B"
            elif average >= 70:
                letter = "C"
            elif average >= 60:
                letter = "D"
            else:
                letter = "F"

            # Pass/Fail
            if average >= self.passing_grade:
                result = "Passed"
            else:
                result = "Failed"

            print(f"Average      : {average:.2f}%")
            print(f"Letter Grade : {letter}")
            print(f"Result       : {result}")

        print("=" * 45)
