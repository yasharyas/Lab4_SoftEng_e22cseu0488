class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, emp_id, name, age, salary):
        employee = Employee(emp_id, name, age, salary)
        self.employees.append(employee)

    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)

    def display_table(self):
        for emp in self.employees:
            print(f"ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")

if __name__ == "__main__":
    employee_table = EmployeeTable()

    employees_data = [
        ("161E90", "Raman", 41, 56000),
        ("161F91", "Himadri", 38, 67500),
        ("161F99", "Jaya", 51, 82100),
        ("171E20", "Tejas", 30, 55000),
        ("171G30", "Ajay", 45, 44000)
    ]

    for emp_id, name, age, salary in employees_data:
        employee_table.add_employee(emp_id, name, age, salary)

    print("Choose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    choice = input().strip()

    if choice == "1":
        employee_table.sort_by_age()
    elif choice == "2":
        employee_table.sort_by_name()
    elif choice == "3":
        employee_table.sort_by_salary()
    else:
        print("Invalid choice")

    print("\nSorted Employee Table:")
    employee_table.display_table()
