class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

def applyIncrease(employee):
    increasedSalary = employee.salary * 1.1
    return Employee(employee.name, increasedSalary)

def lowSalary(employees, threshold):
    return filter(lambda emp: emp.salary < threshold, employees)

def averageSalary(employees):
    employeeList = list(employees) 
    salaries = map(lambda emp: emp.salary, employeeList)
    totalSalaries = sum(salaries)
    nofEmployees = len(employeeList) 
    return totalSalaries / nofEmployees

def salarySort(employees):
    return sorted(employees, key=lambda emp: emp.salary)

def highestSalary(employees):
    return max(employees, key=lambda emp: emp.salary)

def formatSalary(salary):
    return "${:,.0f}".format(salary)

employees = [
    Employee("Omar", 50000),
    Employee("Jhayco", 60000),
    Employee("Feid", 45000),
    Employee("Mora", 55000),
    Employee("Anuel", 70000),
    Employee("Eladio", 80000),
]

increasedEmployees = list(map(applyIncrease, employees))

salaryThreshold = 60000
empBelowThreshold = lowSalary(increasedEmployees, salaryThreshold)
empAverageSalary = averageSalary(increasedEmployees)
empSortedSalaries = salarySort(increasedEmployees)
empHighestSalary = highestSalary(increasedEmployees)

print("Original employees:")
for emp in employees:
    print(f"{emp.name}: {formatSalary(emp.salary)}")

print("\nEmployees with salary raise:")
for emp in increasedEmployees:
    print(f"{emp.name}: {formatSalary(emp.salary)}")

print("\nEmployees with low salary:", [emp.name for emp in empBelowThreshold])
print("Average salary of employees with raise: ${:.2f}".format(empAverageSalary))

print("\nEmployees sorted by salary:")
for emp in empSortedSalaries:
    print(f"{emp.name}: {formatSalary(emp.salary)}")

print("\nEmployee with the highest salary:", empHighestSalary.name)
