
'''Parent class'''
class Employee:

    '''Class attribute'''
    company="google"
    
    '''Class method'''
    def showDetails(self):
        print("This is an employee.")


''' derived/child class'''
class Programmer(Employee):

    language='Python'
    
    def getLanguage(self):
        print(f"The language is {self.language}")  


e=Employee()
e.showDetails()  # equivalent to -->
Employee.showDetails(e)

print('\n')

''' child class has access(inherited) to all parent methods and attributes '''
p=Programmer()
p.showDetails() 
print(p.company)


