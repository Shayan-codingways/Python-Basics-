'''Constructor'''

class Employee:
    company='google'

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit

        print('Employee is created')

    def getDetails(self):
        print(f"The name of the employee is {self.name} has salary {self.salary} and subunits {self.subunit}")


Harry = Employee('harry',100,'printer') # runs itself (passed arguments in class)
Harry.getDetails() # Employee.getDetails(harry)