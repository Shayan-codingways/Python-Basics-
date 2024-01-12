'''printing pattern'''

def print_pattern(n):

    i=n
    while(i!=0):
        print("*" * i)
        i-=1
    
    
    print('\n')
    i=0
    for i in range(n,0,-1):
        print("*" * i)



x=int(input('Enter num for pattern: '))
#print_pattern(x)