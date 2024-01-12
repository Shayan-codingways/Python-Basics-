'''Recursive'''

# n!= [1*2*3*4*.... * n-1] * n
# n!= (n-1)! * n

def factorial_recursive(n):

    # base case 
    if (n==1 or n==0):
        return 1
    
    # formula case, recursive
    fact = factorial_recursive(n-1) * n
    return fact


num=int(input('number please: '))
ans=factorial_recursive(num)
print(ans)