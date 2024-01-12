# if any operator performs additional actions other than what is meant for, 
# it is called operator overloading. 

print(10+20)
# back process(magic methods)
'__add__(self,x)'
print(int.__add__(10,20))
print(int.__sub__(10,20))
print(int.__mul__(10,20))
print(int.__truediv__(10,20))

print("sha"+"yan")
print(str.__add__("sha","yan"))


'''overload (operation on objects)'''
class A:
    def __init__(self,x):
        self.x=x

    def __add__(self,other): #-->A.__add__(10,20)
        sum=self.x + other.x
        return sum
 
a=A(100)
b=A(200)

sum=a+b  # A.__add__(self,other) -- > "+" calls thiss add method A (other is b) --> A.__add__(a,b)
print(sum) # (sums a+b)