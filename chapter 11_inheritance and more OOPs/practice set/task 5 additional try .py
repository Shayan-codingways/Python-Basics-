
class N_dimensional_vec:
    # vec initialized
    def __init__(self,vec):
        self.vec=vec

    # display string 
    def __str__(self):

        vec_str=""
        index=97 

        for item in self.vec:
           
           string_to_add = f"{item}{chr(index)} +"
           vec_str += string_to_add
           index += 1
        
        vec_str=vec_str[:-1]
        return vec_str  # now prints on called print function on object
    
    
        # initially string empty 
        # index for ascii characters 
        # adding string in vec andchr(index) converts to ascii
        # vec sliced to remove last + sign
        # returned as print(vec1) is called


    '''adding'''
    def __add__(self,seelf):
       
        added_vector=[]
        for item in range(0 , len(self.vec)):
            result=self.vec[item]+vec2.vec[item]

            added_vector.append(result)
            item+=1

        return N_dimensional_vec(added_vector)   # print also called with v1+v2 so moves to str
    
    # here we are creating a new list of vectors so initialize list
    # then a loop from index 0 to len for summing every outcome
    # appends every value to list unlike string as string adds but not list
    # index increased by 1 everytime for loop
    # returned as a function/class with print(vec1+vec2) leading to str called.
    
    '''dot prduct'''
    def __mul__(self,seelf):
       
        dot_product=0
        for item in range(0 , len(self.vec)):
            result=self.vec[item]*vec2.vec[item]
            dot_product+=result

        return dot_product
    
    def modulusofvectors(self):
        sum=0
        for item in range(len(self.vec)):
            res_initial=self.vec[item] * self.vec[item]
            sum+=res_initial

        res_final=sum **0.5
        
        return res_final


vec1 = N_dimensional_vec([1,2,3,4,5,6,7])
print(vec1)

vec2 = N_dimensional_vec([-1,-2,3,-4,5,6,-7])

vec3=vec1+vec2 # vec 3 is added vector [we move to return N_dimensional_vec(added_vector)]
               # this list [2,4,6,8,10,12,14] is recorded in the class cobnstruct
print(vec3) # on this, the upper list is displayed


dot_product=vec1*vec2
print(dot_product)

if dot_product==0:
    print("two vectors are perpendicular")
else:
    print("Not perpendicular")

print(vec1.modulusofvectors())
print(vec1.modulusofvectors())

print("Value of cosQ is: ",dot_product/(vec1.modulusofvectors()*vec2.modulusofvectors()))