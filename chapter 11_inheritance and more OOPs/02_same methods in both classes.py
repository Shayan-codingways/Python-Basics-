
''' Parent class '''
class Employee:
    company="google"

    def showDetails(self):
        print("This is an employee.")


''' derived/child class'''
class Programmer(Employee):
    language='Python'
    
    def getLanguage(self):
        print(f"The language is {self.language}") 

    ####################################################################

    company='youtube'

    '''same function as above class (overwritten of the parent class)'''
    def showDetails(self):
        print("This is a programmer")


# both classes use their own function now

e=Employee()
e.showDetails()  # equivalent to -->
Employee.showDetails(e)

print('\n')

''' child class has access(inherited) to all parent methods and attributes '''
p=Programmer()
p.showDetails() 

print(p.company) # overwritten from parent class



