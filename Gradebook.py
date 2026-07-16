from Student import Student
class Gradebook:
    # Creates a new Gradebook object.
    # Initializes dictionaries for students, courses, and grades,
    # and sets the passing grade.
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

        if student_id not in self.grades:
            print("Student not found.")
            return

        if course_code not in self.grades[student_id]:
            print("Student not enrolled.")
            return

        course = self.courses[course_code]

        assessment = course.find_assessment(assessment_title)

        if assessment is None:
            print("Assessment not found.")
            return

        self.grades[student_id][course_code][assessment_title] = score

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

















