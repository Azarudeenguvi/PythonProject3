class Employee:
    def __init__(self,name,salary):
        self.salary=salary
        self.name=name

    def calculate_salary(self):
        print(f"The calculated salary of employee {self.name} and salary is {self.salary}")

class RegularEmployee(Employee):
    def calculate_salary(self):
        print(f"The calculated salary of regular employee {self.name} and salary is {self.salary}")

class ContractEmployee(Employee):
    def calculate_salary(self):
        print(f"The calculated salary of contract employee {self.name} and salary is {self.salary}")

class Manager(Employee):
    def calculate_salary(self):
        print(f"The calculated salary of manager {self.name} and salary is {self.salary}")


m1=Manager('praveen',50000)
m1.calculate_salary()
c1=ContractEmployee('john',12000)
c1.calculate_salary()
r1=RegularEmployee('peter',30000)
r1.calculate_salary()


#************** or ********************
# m=[Manager('praveen',50000),ContractEmployee('john',12000),RegularEmployee('peter',30000)]
# for i in m:
#     i.calculate_salary()

