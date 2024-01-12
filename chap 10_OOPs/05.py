'''same class and instance attribute'''


class Employee:
    company='Google'  # hardcore(specific to each class) (set for each object)
    salary=100        # salary also used as class attribute 

# object instantiation
harry=Employee()
rajni=Employee()

# class attributes(same for both)
print(harry.company) 
print(rajni.company)

# instance attributes(both objects have different attributes)
harry.salary=300 # salary as instance attributes
rajni.salary=400

print(harry.salary)
print(rajni.salary)

