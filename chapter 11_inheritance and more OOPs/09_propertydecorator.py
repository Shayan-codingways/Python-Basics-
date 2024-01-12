'''property/getter introduction'''

class Employee:
    company="Engro"
    salary=3000
    salaryBonus=444
    # totalSalary=3330+444 (how to avoid hardcore by property decorator)
    
    '''below function acts a property not function'''
    @property
    def totalsalary(self):
        a=self.salary+self.salaryBonus
        return a

    
e=Employee()

a=e.totalsalary #(it's a property now so we cant write function() instead we'll write (e.totalsalary)
print(a)
