class Number:     
    def __init__(self,x,y):
        self.num1=x
        self.num2=y
    
    def sum(self):              # function
        return self.num1+ self.num2   # has variables a and b
    
# form filling -->object making    
num=Number(6,7) # object instantiation

s=num.sum()
print(s)