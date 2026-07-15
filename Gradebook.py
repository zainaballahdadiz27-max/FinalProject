class Gradebook:
    def __init__(self):
        self.students = {""}

    def add_student(self, student):
        self.students[student.student_id] = student

    def get_student(self, student_id):
        return self.students.get(student_id)


manager = Gradebook()


# student1 = Student("S001", "Ali")
# student2 = Student("S002", "Sara")

manager.add_student(student1)
manager.add_student(student2)

print(manager.get_student("S001").name)   # Ali
print(manager.get_student("S002").name)   # Sara






