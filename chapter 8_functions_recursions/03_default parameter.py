def greet(name='Stranger'):
    print("Good Day!" + " " , name)


user=input("Enter user name: ")
greet(user)

'''
greet() # no argument passed won't work.'''

# but if we give default value to argument name='stranger'
# then greet() will display stranger

greet()