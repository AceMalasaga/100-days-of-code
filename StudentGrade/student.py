class Student:
    def __init__(self, student_id, name, grade, is_passed=False):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.is_passed = is_passed

    def student_info(self):
        """Display student info with a specific format"""
        status = "PASSED" if self.is_passed else "FAILED"
        print(f"[{self.student_id}] {self.name} - Grade: {self.grade} - [{status}]")

    def update_grade(self, new_grade):
        """Update student grade"""
        self.grade = new_grade
        if new_grade >= 75.0:
            self.is_passed = True
        else:
            self.is_passed = False

# student = Student("141560", "Ace Malasaga", 86.5, True)
# student.student_info()
# student.update_grade(80.5)