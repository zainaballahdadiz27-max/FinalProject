from Gradebook import Gradebook
from Assessment import Assessment
from Course import Course
from Student import Student
from Report import show_report

course = Course("PY101", "Python Programming")

quiz = Quiz("Quiz 1", 10)
exam = Exam("Midterm Exam", 100)
project = Project("Final Project", 100)

gradebook.add_course(course)

gradebook.add_assessment("PY101", quiz)
gradebook.add_assessment("PY101", exam)
gradebook.add_assessment("PY101", project)

gradebook.record_grade("S001", "PY101", "Quiz 1", 8)
gradebook.record_grade("S001", "PY101", "Midterm Exam", 78)
gradebook.record_grade("S001", "PY101", "Final Project", 90)

print("Average:", gradebook.calculate_average("S001", "PY101"))

gradebook.show_report("S001", "PY101")