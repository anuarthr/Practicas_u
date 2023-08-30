class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def applyIncrease(self):
        increasedSalary = self.salary * 1.1
        return Employee(self.name, increasedSalary)

    def formatSalary(self):
        return "${:,.0f}".format(self.salary)

class regularEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

class managerEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def applyIncrease(self):
        increasedSalary = (self.salary + self.bonus) * 1.1
        return managerEmployee(self.name, increasedSalary, self.bonus)

    def formatSalary(self):
        totalSalary = self.salary + self.bonus
        return "${:,.0f} (Salary: ${:,.0f}, Bonus: ${:,.0f})".format(totalSalary, self.salary, self.bonus)

def lowSalary(employees, threshold):
    return filter(lambda emp: emp.salary < threshold, employees)

def averageSalary(employees):
    totalSalaries = sum(emp.salary for emp in employees)
    nofEmployees = len(employees)
    return totalSalaries / nofEmployees

def salarySort(employees):
    return sorted(employees, key=lambda emp: emp.salary)

def highestSalary(employees):
    return max(employees, key=lambda emp: emp.salary)

employees = [
    regularEmployee("Omar", 50000),
    regularEmployee("Jhayco", 60000),
    regularEmployee("Feid", 45000),
    regularEmployee("Mora", 55000),
    managerEmployee("Anuel", 70000, 10000),
    managerEmployee("Eladio", 80000, 15000),
]

increasedEmployees = [emp.applyIncrease() for emp in employees]

salaryThreshold = 60000
empBelowThreshold = list(lowSalary(increasedEmployees, salaryThreshold))
empAverageSalary = averageSalary(increasedEmployees)
empSortedSalaries = salarySort(increasedEmployees)
empHighestSalary = highestSalary(increasedEmployees)

print("Original employees:")
for emp in employees:
    print(emp.name, emp.formatSalary())

print("\nEmployees with salary raise:")
for emp in increasedEmployees:
    print(emp.name, emp.formatSalary())

print("\nEmployees sorted by salary:")
for emp in empSortedSalaries:
    print(emp.name, emp.formatSalary())

print("\nEmployee with the highest salary:", empHighestSalary.name, empHighestSalary.formatSalary())
