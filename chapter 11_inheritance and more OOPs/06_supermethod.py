'''super method is used to access the methods of super class in derived class for multi level inheritance'''"mULTI LEVEL INHERITANCE"

# super class is parent class
# a class has its own method but also runs its predecessor's method as well.

# parent class
class Person:
    country="Pakistan"
    city="Karachi"

    def breath(self):
        print("intake oxygen")

# child class of employee
class Employee(Person):
    company="Honda"

    def getsalary(self):
        print(f"Salary is {self.salary}")

    def breath(self):
        super().breath()
        print("i am breathing")


# child's child
class Programmer(Employee):
    company="fiverr"
   
    def getsalary(self):
        print("No salary to programmers")

    #super method
    def breath(self):
        super().breath()
        print("i am breatheeeeeeeeeeeeeeeee")


'''objects'''
p=Person()
e=Employee()
pr=Programmer()


'''methods running'''
e.breath() # runs it's parent's and then it's owns

print("\n")
pr.breath() # moves to parent super(employee)
            # there is also a super so it moves to grandfather (person)
            # prints persons's, then employees, then it's own
