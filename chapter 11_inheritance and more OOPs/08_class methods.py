'''class methods(we want to change class attribute)'''
# class method is bound to the class and to the object of a class.

# 1 ---> changing instance attribute here
# class
class Employee:
    company="dox"
    salary=100
    location="Karachi"

    def changeSalary(self,sal):
        self.salary=sal

# object instantiate
e=Employee()

# method run
print(e.salary)
print(Employee.salary)

print("\n")
e.changeSalary(400)

print(e.salary) # this changes(nstance attribute changes to 400
print(Employee.salary) # class attribute remain same 100


print("\nchanging class attribute now method 1")


# 2 ---> changing instance and class attribute both here method 1
# class
class Employee:
    company="dox"
    salary=100
    location="Karachi"
    
    #********way of changing class attribute (.__class__. ) **********#
    def changeSalary(self,sal):
        self.__class__.salary=sal 

# object instantiate
e=Employee()

# method run
print(e.salary)
print(Employee.salary)

print("\n")
e.changeSalary(400)

print(e.salary) # this changes(nstance attribute changes to 400
print(Employee.salary) # class attribute remain same 100


print("\nchanging class attribute now method 2")



# 2 ---> changing instance and class attribute both here method 2
# class
class Employee:
    company="dox"
    salary=100
    location="Karachi"
    
    #********way of changing class attribute {cls.salary while passing cls insted of self in function} **********#
    @classmethod #decorator
    def changeSalary(self,sal):
        self.salary=sal 

# object instantiate
e=Employee()

# method run
print(e.salary)
print(Employee.salary)

print("\n")
e.changeSalary(400)

print(e.salary) # this changes(nstance attribute changes to 400
print(Employee.salary) # class attribute remain same 100
