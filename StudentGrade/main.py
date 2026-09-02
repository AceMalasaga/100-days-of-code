from tracker import Tracker

tracker = Tracker()
is_student = True

while is_student:
    print("=== STUDENT GRADE TRACKER ===")
    print("1. View All Students\n2. Add New Student\n3. Update Student Grade\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        tracker.display_students()
    elif choice == 2:
        print("\nNew Student")
        s_id = input("Enter student ID: ").upper().strip()
        s_name = input("Enter student name: ")
        s_grade = float(input("Enter student grade: "))
        tracker.add_student(s_id, s_name, s_grade)
    elif choice == 3:
        print("\nNew Student Grade")
        s_id = input("Enter student ID: ")
        s_grade = float(input("Enter updated student grade: "))
        tracker.update_student_grade(s_id, s_grade)
    else:
        print("Thank you for using this program")
        is_student = False