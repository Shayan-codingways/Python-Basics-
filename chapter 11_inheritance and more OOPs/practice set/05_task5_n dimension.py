"n dimensional vector"

class vector:
    
    '''n-dimensional vector made - just taken a vector we can take list now'''
    def __init__(self,vec):
        self.vec=vec
    
    '''displaying vectors'''
    def __str__(self):
        
        '''initially string empty, and then displayed'''
        str1="" # initially string is empty
        indexofvector=0

        for i in self.vec:
            str1 += f" {i}a{indexofvector} +" # adding in string
            indexofvector +=1

        return str1[:-1] # won't return last (+) sign as slicing is till n-1
   

    '''OPERATOR OVERLOADING'''   
    def __add__(self,slf):

        # we can't add 2 lists bcz it only appends
        " [1,2] + [1,4] = [1,2,1,4] "
        
        new_added_vector=[]
        index=0
        for index in range(len(self.vec)):
            new_added_vector.append(self.vec[index]+slf.vec[index])
            index +=1
        
        return vector(new_added_vector)  # calling under vector(automatically prints) 
                                         #  with str     
        
    
    def __mul__(self,slf):

        "dot product"
        sum=0
        for i in range(len(self.vec)):
            res=self.vec[i]*slf.vec[i]
            sum+=res
        return sum


v1=vector([1,4])
print(v1)
    
'''overloading part'''
v2=vector([1,6])
print(v1+v2)
print(v1*v2)