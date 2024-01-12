'''understanding class attributes (attributes asscociated with class)'''

class Employee:
    company='Google'  # hardcore(specific to each class) (set for each object)

# object instantiation
harry=Employee()
rajni=Employee()

print(harry.company) # same for both
print(rajni.company)

# changing class's company
Employee.company="youtube"

print(harry.company)
print(rajni.company)