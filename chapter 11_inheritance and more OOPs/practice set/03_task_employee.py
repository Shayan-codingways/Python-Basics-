# employee class made
class Employee:
    salary=1000
    increment=1.5
    
    # propertu created so that we can know both sal and increment
    @property
    def salaryAfterIncrement(self):
        res = self.salary * self.increment
        return res
    
    # setter created with additional parameter
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sal):
        self.increment=sal/self.salary

e=Employee()
print(e.salaryAfterIncrement)

print(e.increment)  # 1.5
e.salaryAfterIncrement=2000 # salary after is passed to sal
print(e.increment)  # 2