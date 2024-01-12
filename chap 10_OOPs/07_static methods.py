'''static method'''

class Employee:
    company='google'

    def getsalary(self,signature):
        print(f'salary for this employye working in {self.company} is {self.salary}\n{signature} ')  

    '''static concept(without self)'''
    
    def greet(self):
        print('Good afternoon')

    # here we need no self unlike the upper getsalary function so we can use static method.

    @staticmethod
    def greets():
        print('Good afternoon')
   

   
harry=Employee()


harry.greet() # coverison to Employee.greet(harry)
harry.greets() # coversion to Employee.greets()

harry.salary=10000
harry.getsalary("Thanks")  # == Employee.getsalary(harry,thanks) (harry) pased to function
Employee.getsalary(harry,'Thanks')