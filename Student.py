
class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = []

    # Returns the student's ID
    def get_id(self):
        return self.student_id

    # Returns the student's name
    def get_name(self):
        return self.name

    # Updates the student's email
    def set_email(self, email):
        if "@" in email and "." in email:
            self.email = email
            print("Email updated successfully.")
        else:
            print("Invalid email address.")

    # Adds a course to the student's course list
    def enroll_course(self, course_code):
        self.courses.append(course_code)
        print(f"{course_code} has been added.")

    # Displays the student's information
    def display_info(self):
        print("Student Information")
        print("-------------------")
        print(f"Student ID : {self.student_id}")
        print(f"Name       : {self.name}")
        print(f"Email      : {self.email}")
        print(f"Courses    : {', '.join(self.courses) if self.courses else 'No courses enrolled'}")


# Example Usage
# student1 = Student("S001", "Ahmad Noori", "ahmad@example.com")
#
# print(student1.get_id())
# print(student1.get_name())
#
# student1.set_email("rahimi@gmail.com")
#
# student1.enroll_course("PY101")
# student1.enroll_course("MATH101")
#
# student1.display_info()