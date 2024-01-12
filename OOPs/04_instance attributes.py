'''instance attributes(specific to an object and not for class. )'''

class Employee:
    company='Google'  # hardcore(specific to each class) (set for each object)

# object instantiation
harry=Employee()
rajni=Employee()

# class attributes(same for both)
print(harry.company) 
print(rajni.company)

# instance attributes(both objects have different attributes)
harry.salary=300
rajni.salary=400

print(harry.salary)
print(rajni.salary)


