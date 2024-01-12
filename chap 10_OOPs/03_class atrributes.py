'''class attributess --> are changeable''' 


'''Form'''
class Employee:
    '''class attribute'''
    company='Google'  # hardcore(specific to each class)

# object instantiation
harry=Employee()
rajni=Employee()

print(harry.company)
print(rajni.company)

# changing class's company
Employee.company="youtube"

print(harry.company)
print(rajni.company)