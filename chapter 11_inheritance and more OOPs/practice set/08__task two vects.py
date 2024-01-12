class vector:
    
    # 3 dimensional vector initialized vector(self.i,self.j,self.k)
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __add__(self,slf):
        i=self.i+slf.i
        j=self.j+slf.j
        k=self.k+slf.k

        return f"{i}i + {j}j + {k}k"
    
        #return vector(i,j,k)
'''
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
   ''' 
v1=vector(1,2,3)
v2=vector(5,6,7)
print(v1+v2)


'''Method 2'''


class vector:
    
    # 3 dimensional vector initialized vector(self.i,self.j,self.k)
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __add__(self,slf):
        i=self.i+slf.i
        j=self.j+slf.j
        k=self.k+slf.k

        return vector(i,j,k) # returned as a new vector
    
    # dispalyaing a new vector defined as follows vector(self.i, self.j, self.k)
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    

v1=vector(1,2,3)
v2=vector(5,6,7)
print(v1+v2)





