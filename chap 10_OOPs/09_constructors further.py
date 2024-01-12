'''Constructor'''
# form
class Employee:
    # class attribute
    company='google'

    # constructor dunder method
    def __init__(self,name,salary,subunit):
        # defining attrbutes within constructor this time.
        self.name=name
        self.salary=salary
        self.subunit=subunit

        print('Employee is created')
    
    # function for get salary
    def getDetails(self):
        print(f"The name of the employee working in /'{self.company} is /'{self.name} has salary /'{self.salary} and subunits /'{self.subunit}")

# object instantiation and calling of constructor
Harry = Employee('harry',100,'printer') # runs itself

Harry.getDetails() 