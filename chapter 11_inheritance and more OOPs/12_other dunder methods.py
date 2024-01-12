'''magical str dunder method --> directly printing objects '''

class Number:
    def __init__(self,num):
        self.num=num

    '''these aren't functions'''
    # add method (set method)
    def __str__(self) :
        return f"Decimal number : {self.num}"  # (returned fstring)
    
    def __len__(self):
       return 1

n=Number(9)

print(n) # number object at memory location(000x0003993443>) (if def str method not applied)
print(len(n)) # len function 