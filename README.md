# Student Gradebook & Course Manager
## Full Name
**Zainab Allahdadi**

## Project Title
**Student Gradebook and Course Manager**

## Project Description
The Student Grade Management System is a Python application developed using Object-Oriented Programming (OOP). It helps teachers manage students, courses, assessments, and grades in one place. The system allows users to enroll students in courses, record grades for quizzes, exams, and projects, calculate averages, generate student reports, and display overall statistics through a dashboard.

## How to Run the Project

1. Make sure Python or VS code is installed on your computer.
2. Download or clone the project files.
3. Open the project folder in your preferred IDE (such as PyCharm or VS Code).
4. Run the `main.py` file.
5. Use the menu to interact with the system.

## Classes Created

The project contains the following classes:

- **Student**
- **Course**
- **Assessment**
- **Quiz**
- **Exam**
- **Project**
- **Gradebook**

## Object-Oriented Programming Concepts

### Encapsulation
Encapsulation is used by organizing data and related methods inside classes.

Examples:
- `Student` stores student information and enrollment methods.
- `Course` stores course information, enrolled students, and assessments.
- `Gradebook` manages students, courses, grades, and reports.

### Inheritance
The project uses inheritance by creating specialized assessment classes from the `Assessment` class.

- `Quiz` inherits from `Assessment`
- `Exam` inherits from `Assessment`
- `Project` inherits from `Assessment`

This reduces code duplication and promotes code reuse.

### Method Overriding
Method overriding is used in the assessment subclasses.

Each subclass (`Quiz`, `Exam`, and `Project`) overrides the `grade_message()` method to provide feedback specific to that assessment type.

Example:
- Quiz  "Excellent quiz performance!"
- Exam  "Passed the exam."
- Project  "Excellent project work."

## Custom Features

### 1. Dashboard
The Dashboard displays useful information about the system, including:
- Total number of students
- Total number of courses
- Total number of assessments

### 2. Teacher Comments
Teachers can add personalized comments to a student's report. The comments are saved with the student's information and displayed whenever the student's report is generated.

## Main Features

- Add students
- Add courses
- Enroll students in courses
- Add quizzes, exams, and projects
- Record student grades
- Calculate average grades
- Generate detailed student reports
- Display letter grades
- Determine pass/fail results
- Search for students
- Delete students
- Add teacher comments
- Display a dashboard

## Author

**Zainab Allahdadi**
