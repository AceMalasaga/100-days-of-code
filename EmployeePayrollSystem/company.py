from employee import EmployeePayroll
class Company:
    def __init__(self):
        self.employees = {}

    def display_all_employees(self):
        if not self.employees:
            print("No employee currently registered in the system.")
        else:
            print("=== ALL MEMBERS ===")
            for worker in self.employees.values():
                worker.display_info()

    def add_employee(self, employee_id, employee_name, hourly_rate):
        if employee_id in self.employees:
            print(f"Employee ID '{employee_id}' already exists in the system.")
        else:
            self.employees[employee_id] = EmployeePayroll(employee_id, employee_name, hourly_rate)

    def log_employee_hours(self, emp_id, hours):
        if emp_id in self.employees:
            self.employees[emp_id].log_hours(hours)
        else:
            print(f"Employee ID '{emp_id}' does not exist in the system.")

    def process_payroll(self):
        total_company_payout = 0.0
        for emp in self.employees.values():
            employee_payout = emp.calculate_payroll()
            total_company_payout += employee_payout
            print(f"[{emp.employee_id}] {emp.employee_name}: {emp.hourly_rate} hrs @ {emp.hours_worked}/hr = {employee_payout}")
            emp.reset_payroll()
        print("--------------------------------------------------")
        print(f"Total company payout: {total_company_payout}\n\n")

# company = Company()
# company.add_employee("E101", 'Ace Malasaga', 595, 32)
# company.log_employee_hours("E101", 32)
# company.process_payroll()
# company.display_all_employees()
#
# print(company.employees)