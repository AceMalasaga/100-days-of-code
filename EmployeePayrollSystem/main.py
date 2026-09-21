from company import Company

is_payroll_active = True
company = Company()

while is_payroll_active:
    print("=== COMPANY PAYROLL SYSTEM ===")
    print("1. View All Employees\n2. Add New Employee\n3. Log Work Hours\n4. Process & Run Payroll\n5. Exit")
    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:
        company.display_all_employees()
    elif user_choice == 2:
        emp_id = input("Enter Employee ID: ").strip().lower()
        emp_name = input("Enter Employee Name: ")
        emp_hr = float(input("Enter Hourly Rate: "))
        company.add_employee(emp_id, emp_name, emp_hr)
    elif user_choice == 3:
        e_id = input("Enter Employee ID: ").strip().lower()
        emp_hours = float(input("Enter Hours Worked: "))
        company.log_employee_hours(e_id, emp_hours)
    elif user_choice == 4:
        company.process_payroll()
    elif user_choice == 5:
        is_payroll_active = False
        print("Exiting...")
    else:
        print("Invalid Input")