class Employee:
    def __init__(self, name, ID_number, department, job_title):
        self.name = name
        self.ID_number = ID_number
        self.department = department
        self.job_title = job_title

    def get_info(self):
        return self.name, self.ID_number, self.department, self.job_title

worker1 = Employee("Susan Meyers", "47899", "Accounting", "Vice President")
worker2 = Employee("Mark Jones", "39119", "IT", "Programmer")
worker3 = Employee("Joy Rogers", "81774", "Manufacturing", "Engineer")

print("Name,", "ID Number,", "Department,", "Job Title")
info1 = worker1.get_info()
print(info1)
info2 = worker2.get_info()
print(info2)
info3 = worker3.get_info()
print(info3)

# Program #4, Donovan Thompson 4/4/2025
