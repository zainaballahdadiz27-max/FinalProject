class Course:
    # Creates a Course object with its code, name, list of enrolled students, and assessments.
    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name
        self.students = {}
        self.assessments = []

    # Enrolls a student by adding their student ID to the students list.
    def add_student(self, student):
        self.students[student.student_id] = student

    # Adds a Quiz, Exam, or Project object to the assessments list.
    def add_assessment(self, assessment):
        self.assessments.append(assessment)

    # Searches for an assessment by its title.
    # Returns the assessment object if found,
    # otherwise returns None.
    def find_assessment(self, title):
        for assessment in self.assessments:
            if assessment.title == title:
                return assessment
        return None

    # Displays the course details, including
    # course code, course name, enrolled students,
    # and assessments.
    def display_info(self):
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Enrolled Students: {len(self.students)}")

        print("Assessments:")
        for assessment in self.assessments:
            print(f"- {assessment.title} / Max Score: {assessment.max_score}")

# course = Course("PY101", "Python Programming")
#
# course.add_student("S001")
# course.add_student("S002")
#
# quiz = Quiz("Quiz 1", 10)
# exam = Exam("Midterm Exam", 100)
# project = Project("Final Project", 100)
#
# course.add_assessment(quiz)
# course.add_assessment(exam)
# course.add_assessment(project)
#
# course.display_info()