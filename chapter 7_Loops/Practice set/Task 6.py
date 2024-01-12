''' Factorial of a given number'''

n=int(input("Factorial number: "))

fact=1
for i in range(1,n+1):
    fact=i*fact

print(f"The factorial of {n} is {fact}")


