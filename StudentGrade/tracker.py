from student import Student
class Tracker:

    def __init__(self):
        self.student = {}

    def add_student(self, student_id, name, grade=0.0):
        """Add a student records to the tracker"""
        if student_id in self.student:
            print(f"Student ID '{student_id}' already exists")
            return False
        else:
            self.student[student_id] = Student(student_id, name, grade)
            return True

    def display_students(self):
        """Display all student records"""
        if not self.student:
            print("No students currently registered.")
        else:
            print("\n=== ALL STUDENTS ===")
            for student in self.student.values():
                student.update_grade(student.grade)
                student.student_info()
            print("----------------------------------------------\n")

    def update_student_grade(self, student_id, new_grade):
        """Update student grade"""
        if student_id in self.student:
            self.student[student_id].update_grade(new_grade)
            status = "PASSED" if self.student[student_id].grade >= 75 else "FAILED"
            print(f"Updated {self.student[student_id].name}'s grade to {new_grade} ([{status}])")
        else:
            print(f"Student ID '{student_id}' does not exist")

# track = Tracker()
# track.add_student("S123", "Ace Malasaga",74.90)
# track.add_student("S121", "Ace Bernard Malasaga",95.0)
# track.update_student_grade("S121", 85.0)
# track.display_students()
