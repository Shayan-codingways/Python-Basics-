'''recursion to sum n natural nos.'''

# Sn = 1+2+3+4+5+6+....+ n-1 +n
# Sn = S(n-1) + n

def recursion_sum(n=0):
    if (n==0):
        return 0
    else:
        sum=n+recursion_sum(n-1)

    return sum


x=int(input('Enter num upto sum: '))

print(f"Sum of {x} numbers is {recursion_sum(x)}\n")
print(f"Sum of {x} numbers is {recursion_sum()}")