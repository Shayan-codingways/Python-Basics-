class Employee:
    '''class attribute'''
    company='Google'  # hardcore(specific to each class)
    salary= 100

# object instantiation
harry=Employee()
rajni=Employee()

harry.salary=300
rajni.salary=400

print(harry.salary)
print(rajni.salary)