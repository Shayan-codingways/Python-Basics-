class Number:     
    def __init__(self1,x):
        self1.num=x
    
    def __add__(self1,self2):
        return self1.num + self2.num
    
    
# form filling -->object making    
n1=Number(6) # object instantiation
n2=Number(5)

print(n1+n2)

'''
initially, self1.num --> n1.num has 6
then       self1.num --> n2.num has 5

self1=n1 , self2=n2
add dunder called --> __add__(n1,n2)

return self1.num + self2.num
          n1.num + n2.num 
           6     +     5 


'''