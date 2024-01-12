'''self'''

''' class made ''' 
class Employee:
    company='google'

    def getsalary(self):
        print('salary is 100k')

'''object formed'''
harry=Employee()


'''calling methods of class'''
harry.getsalary()
Employee.getsalary(harry)

'''both 
harry.getsalary() 
Employee.getsalary(harry)  
are equivalent.

when we say upper one we have it convert it to lower one behind scenes. argument given
is harry which corresponds to the self we take for a function

if we dont't take self then ide will show error "no positional argument for Employee.get salary
while it takes one on call"

'''