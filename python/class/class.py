class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary 
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount
    
    def displayEmployee(self):
        print "Name :", self.name, ", Salary: ", self.salary

emp1 = Employee("Zara", 2000)
emp2 = Employee("Kyle", 3000)

emp1.displayEmployee()
emp2.displayEmployee()

print "Total Employee is %d" % Employee.empCount

emp1.salary = 1000

Employee_list = []

for i in range(5):
    name = "kyle"
    salary = 1000 + i*1000
#    emp = Employee(name, salary)
#    Employee_list.append(emp)
    Employee_list.append(Employee(name, salary))

for i in range(5):
    Employee_list[i].displayEmployee()



