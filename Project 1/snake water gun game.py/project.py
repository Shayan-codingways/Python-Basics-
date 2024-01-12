'''Game Project!'''


# function for game....
def gameWin(a,b):

    # tie case
    if a==b:
        return None
    
    # case 1
    if a =='s':
        if b == 'w':
            return False
        elif b=='g':
            return True
        
    elif a =='w':
        if b == 's':
            return True
        elif b=='g':
            return False
    
    elif a =='g':
        if b == 's':
            return False
        elif b=='w':
            return True
    



# Computer choice
print("computer Turn: snake(s) water(w) or gun(g)")

import random
randno=random.randint(1,3)
print(randno)

if(randno==1):
    a = 's'
elif(randno==2):
    a = 'w'
else:
    a = 'g'

# user turn
b=input("Your Turn: snake(s) water(w) or gun(g): ")

# choice display
print(f"Computer chose {a}")
print(f"You chose {b}")

# function call
res=gameWin(a,b)

# result
if(res==None):
    print("Tie")
elif res:
    print("you win")
else:
    print("You Lose")