class Number:
    
    def __init__(self ,x,y):
        self.num1=x
        self.num2=y

    '''method'''
    def sum(self):
        return self.num1 + self.num2

'''made object'''    
num=Number(4,6)

'''called function'''
s=num.sum()
print(s)

class Number:
    
    def __init__(self ,x,y):
        self.num1=x
        self.num2=y

        print(f"the sum is {self.num1} + {self.num2}")

'''made object'''    
num=Number(4,6)

