'''2d / 3d vec'''
# single inheritance

'''2d vec class formed'''
class C2dVec:

    def __init__(self,i,j):
        self.i=i
        self.j=j

    # dunder method for printing a vector
    def __str__(self):
        return f"{self.i}i+{self.j}j"
    
class C3dVec(C2dVec):

    def __init__(self,i,j,k):
        super().__init__(i,j)  # to run c2v2
        self.k=k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"


v2d=C2dVec(1,3)
v3d=C3dVec(1,9,7)

# dunder methods are printed with help of an object
# dunder methods are for objects itself so we don't nhed to call it like functions
print(v2d) 
print(v3d)