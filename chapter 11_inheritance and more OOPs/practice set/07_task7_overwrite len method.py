"n dimensional vector"

class vector:
    def __init__(self,vec):
        self.vec=vec

    def __str__(self):

        str1="" # initially string is empty
        index=0

        for i in self.vec:
            str1 += f" {i}a{index} +" # adding in string
            index +=1

        return str1[:-1] # won't return last (+) sign as slicing is till n-1
   
   
    def __len__(self):
        return len(self.vec)


v1=vector([1,4,4,5,5,6,8])
print(v1)
    
'''overloading part'''
v2=vector([1,6,4,5,5,8])
print(v2)

'''task 7'''

print(len(v1))
print(len(v2))
