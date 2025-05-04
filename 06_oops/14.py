class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def get_info(self):
        return f"Employee: {self.name} (ID: {self.employee_id})"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # List to store Employee objects
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def list_employees(self):
        print(f"Department: {self.name}")
        for employee in self.employees:
            print(f"- {employee.get_info()}")

# Example usage
if __name__ == "__main__":
    # Create employees
    emp1 = Employee("John Doe", "E001")
    emp2 = Employee("Jane Smith", "E002")
    
    # Create department
    dept = Department("IT")
    
    # Add employees to department
    dept.add_employee(emp1)
    dept.add_employee(emp2)
    
    # List employees in department
    dept.list_employees() 