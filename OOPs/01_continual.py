#object oriented programming
\
''' class is like a form and object is the application(after filling the form)(carries no memory space)

structure --> Class Employee:(Pascal case)
                 # methods/variable
''' 

'''
pascal case:
EmployeeName ---> both capital letters

camel case:
isNumeric, isFloatOrInt ---> first letter small and all others capital letters
'''
 
'''------------------------------------------------------------------------------------------------------'''

# form --> class
class Number:                   # number-named class
    def sum(self):              # function
        return self.a+ self.b   # has variables a and b
    
# form filling -->object making    
num=Number() # object instantiation
num.a=12
num.b=34
s=num.sum()

print(s)
