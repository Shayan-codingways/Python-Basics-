'''Operators'''

#dunder methods are methods that allow instances of a class to interact with the built-in functions 
# and operators of the language.

class Number:
    def __init__(self,num): # num = 4
        self.num=num
        
    '''these aren't functions'''
    # add method (set method)
    def __add__(self,seelf):  # Number.__add__(4,6)  (n1.num,n2.num)
        print(f"lets add {self.num} to {seelf.num}") # n1.num, n2.num
        return self.num+seelf.num
    
    # mul method (set method)
    def __mul__(self,num2):  # Number.__mul__(4,6)
        print(f"lets * {num2.num} to {self.num}")
        return self.num*num2.num

n1=Number(4)  # n1.num=4 
n2=Number(6)  # n2.num=6

# operator overload
sum=n1 + n2 # (calls add method) Number.__add__(n1,n2)
mul=n1 * n2 # (calls mul method) Number.__mul__(n1,n2)
print(sum)
print(mul)


'''
first of all n1 and n2 has 4 and 6 recorded as self.num

on n1+n2, add dunder called
__add__(self,seelf)
__add__(n1,n2)

sum = self.num+seelf.num 
'''