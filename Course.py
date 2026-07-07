class Course:
    def __init__(self, course_code, course_name, students, assessments):
        self.course_code = course_code
        self.course_name = course_name
        self.students = [students]
        self.assessments = [assessments]

    # Enrolls a student in this course by adding the student’s ID to the course’s students list.
    def add_student(self, student_id):
        if student_id == student_id:
            self.students.append(student_id)