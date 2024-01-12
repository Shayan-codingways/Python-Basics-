"mULTI LEVEL INHERITANCE"

# parent class {grandparent}
class Person:
    country="Pakistan"
    city="Karachi"

    def breath(self):
        print("intake oxygen")

# child class of employee [parent]
class Employee(Person):
    company="Honda"

    def getsalary(self):
        print(f"Salary is {self.salary}")

    def breath(self):
        print("i am breathing")


# child's child {son}
class Programmer(Employee):
    company="fiverr"
   
    def getsalary(self):
        print("No salary to programmers")


'''objects'''
p=Person()
e=Employee()
pr=Programmer()


'''methods running'''
p.breath() # uses itselfs
e.breath() # uses itselfs
pr.breath() # inherits from employee (takes nearest parent's methods)

