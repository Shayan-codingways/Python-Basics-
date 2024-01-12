'''greatest of 3 numbers'''

def greatof3(x,y,z):
    if(x>=y):
        if(x>=z):
            great=x
        elif(z>=x):
            great=z

    elif(y>=x):
        if(y>=z):
            great=y
        elif(z>=x):
            great=z

    return great


x=int(input('Enter num 1: '))
y=int(input('Enter num 2: '))
z=int(input('Enter num 3: '))

ans=greatof3(x,y,z)
print(f"the greatest of these numbers is {ans}")