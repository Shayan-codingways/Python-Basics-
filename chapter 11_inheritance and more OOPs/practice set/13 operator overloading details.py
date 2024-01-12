# if any operator performs additional actions other than what is meant for, 
# it is called operator overloading. 

print(10+20)
# back process(magic methods)
'__add__(self,x)'
print(int.__add__(10,20))
print(int.__sub__(10,20))
print(int.__mul__(10,20))
print(int.__truediv__(10,20))

print("sha"+"yan") #(calls for str)
print(str.__add__("sha","yan"))
