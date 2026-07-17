def show_report(self, student_id, course_code):

    if student_id not in self.students:
        print("Student not found.")
        return

    if course_code not in self.courses:
        print("Course not found.")
        return

    student = self.students[student_id]
    course = self.courses[course_code]

    print("\n========== REPORT ==========")
    print(f"Student : {student.name}")
    print(f"ID      : {student.student_id}")
    print(f"Course  : {course.course_name}")
    print("----------------------------")

    total = 0
    count = 0

    for title, score in self.grades[student_id][course_code].items():
        print(f"{title}: {score}")
        total += score
        count += 1

    average = total / count if count else 0

    print("----------------------------")
    print(f"Average: {average:.2f}")

    if average >= self.passing_grade:
        print("Status : PASS")
    else:
        print("Status : FAIL")