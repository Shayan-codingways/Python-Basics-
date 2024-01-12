'''super method is used to access the methods of super class in derived class for multi level inheritance'''"mULTI LEVEL INHERITANCE"


class Person:

    def __init__(self):
        print("initializing person \n")

# child class of employee
class Employee(Person):

    def __init__(self):
        
        super().__init__() # run's person constructor as well
        print("initializing employee \n")


# child's child
class Programmer(Employee):

    def __init__(self):
        super().__init__() # run's person constructor as well
        print("initializing Programmer \n")
   

'''objects'''
p=Person()
print("\n")

print("@@@@@@@@@@@@")
e=Employee() # firstly comes for person and then employee
print("\n")


pr=Programmer()





