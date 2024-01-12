
'''Method 1'''

class vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1=vector([1,2,3]) # whole vector taken as list
print(v1)

'''Method 2'''

print("\n Method 2")
#### not taken as list
class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
v1=vector(1,2,3)
print(v1)

'''Method 3'''

print("\n Method 3")
#### no str
class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

        print(f"{self.i}i + {self.j}j + {self.k}k")
    
v1=vector(1,2,3)
