'''setters function'''
class Employee:
    company="Engro"
    salary=3000
    salaryBonus=500
    # totalSalary=3330+444 (how to avoid hardcore by property decorator)
    
    def totalsalary(self):
        a=self.salary+self.salaryBonus
        return a
    

    def totalsalariii(self,sal):
       self.salaryBonus=sal-self.salary

e=Employee()

a=e.totalsalary() 
print(a)

print("\n")

# can't do for functions
# ** e.totalsalary()=5000 {error}
e.totalsalariii(5000)
print(e.salary)
print(e.salaryBonus)
