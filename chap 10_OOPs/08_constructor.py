'''static Constructor'''

class Employee:
    company='google'

    def __init__(self):
        print('Employee is created')

    def getsalary(self,signature):
        print(f'salary for this employye working in {self.company} is {self.salary}\n{signature} ')  
        
    '''static concept(without self)'''
    
    def greet(self):
        print('Good afternoon')

    # here we need no self unlike the upper getsalary function so we can use static method.

    @staticmethod
    def greets():
        print('Good afternoon')

Harry = Employee()