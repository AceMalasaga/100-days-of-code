class EmployeePayroll:

    def __init__(self, employee_id, employee_name, hourly_rate, hours_worked=0.0):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.hourly_rate = float(hourly_rate)
        self.hours_worked = float(hours_worked)

    def display_info(self):
        """Print employee info"""
        print(f"[{self.employee_id}] {self.employee_name} - Rate: ₱{self.hourly_rate}/hr - Hours Logged: {self.hours_worked} hrs.")

    def log_hours(self, add_hours):
        """Log hours worked by employee"""
        self.hours_worked += add_hours
        print(f"Logged {add_hours} hours for {self.employee_name}. Total hours: {self.hours_worked}")

    def calculate_payroll(self):
        """"Return gross pay for the current pay period"""
        return self.hourly_rate * self.hours_worked

    def reset_payroll(self):
        """Reset hours worked back to 0.0 for the next pay cycle"""
        self.hours_worked = 0.0

# employee_payroll = EmployeePayroll("E101", "Ace Malasaga", 250, 200)
# employee_payroll.display_info()
# employee_payroll.log_hours(8)
# # employee_payroll.calculate_payroll()
# employee_payroll.reset_payroll()
# print(employee_payroll.hours_worked)