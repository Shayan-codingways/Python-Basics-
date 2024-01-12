class Employee:
    company='google'

    def getsalary(self):
        print(f'salary for this employye working in {self.company} is {self.salary}')  #printin both class/obj attributes

harry=Employee()

harry.salary=10000
harry.getsalary()  # == Employee.getsalary(harry) (harry) pased to function
