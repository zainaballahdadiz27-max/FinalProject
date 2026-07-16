# Parent class for graded work. Quiz, Exam, and Project which inherit from this class.

# Parent/Superclass
class Assessment:
    def __init__(self, title, max_score=0):
        self.title = title  # The title of the assessment.
        self.max_score = max_score

    # Converts the student's score into a percentage.
    def calculate_percentage(self, score):
        percentage =  (score / self.max_score) * 100
        return percentage

    # Return feedback for the score
    @staticmethod
    def grade_message(score):
        message = f"Your score is {score}, well done! Keep practicing to improve."
        return message
    # Display the title and the max score

    def display_info(self):
        return f"{self.title} - Max Score: {self.max_score}"

# Child/Subclass
class Quiz(Assessment):
    def display_info(self=None):
        return f"Quiz: {self.title} - Max Score: {self.max_score}"

    # Returns feedback based on the quiz score.
    def grade_message(self, score):
        if score == 10:
            return "Perfect score! Outstanding work!"
        elif score == 9:
            return "Great quiz result! You almost got a perfect score."
        elif score == 8:
            return "Very good job! You have a strong understanding."
        elif score == 7:
            return "Good work! Keep practicing to reach an even higher score."
        elif score == 6:
            return "Nice effort! You're making good progress."
        elif score == 5:
            return "Average result. A little more practice will help."
        elif score == 4:
            return "You're improving, but more study is needed."
        elif score == 3:
            return "Needs more practice. Review the lesson and try again."
        elif score == 2:
            return "Keep trying. Spend more time reviewing the material."
        elif score == 1:
            return "Don't give up. Practice regularly and you'll improve."
        elif score == 0:
            return "No correct answers this time. Review the lesson and try again."
        else:
            return "Invalid score. Please enter a score between 0 and 10."

class Exam(Assessment):
    # Displays the exam name and its maximum score.
    def display_info(self=None):
        return f"Exam: {self.title} - Max Score: {self.max_score}"

    # Returns pass or fail feedback based on the exam score.
    def grade_message(self, score):
        percentage = (score / self.max_score) * 100

        if percentage >= 55:
            return "Passed exam."
        else:
            return "Failed exam."

class Project(Assessment):
    # Displays the project name and its maximum score.
    def display_info(self=None):
        return f"Project: {self.title} - Max Score: {self.max_score}"

    # Returns feedback based on the project score.
    def grade_message(self, score):
        percentage = (score / self.max_score) * 100

        if percentage >= 90:
            return "Excellent project!"
        elif percentage >= 55:
            return "Project submitted."
        else:
            return "Project needs improvement."





exam = Exam("Midterm", 100)
print(exam.grade_message(80))

project = Project("Midterm", 100)
print(project.display_info())
print(project.grade_message(80))

assessment = Assessment("Assessment", 0)
print(assessment.calculate_percentage(8))