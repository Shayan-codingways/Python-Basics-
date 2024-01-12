"MULTIPLE INHERITANCE --> 2 parents 1 child"

# parent(base classes)
class Employee:
    company="VIsa"
    ecode=120

class Freelancer:
    company="Fiverr"
    level=0

    def upgradeLevel(self):
        self.level=self.level+1

# chile(derivfed classes)
class Programmer(Employee,Freelancer):
    name="Rohit"


p=Programmer()
print(p.level)

p.upgradeLevel()
print(p.level)


# ****important**** #
'''prints visa {class Programmer(Employee,Freelancer)} employee written 1st'''
print(p.company)