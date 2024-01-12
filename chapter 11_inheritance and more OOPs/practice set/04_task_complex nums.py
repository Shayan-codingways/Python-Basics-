# real+imaginary i
# 1+2i

class complex:

    # initialize complex num (has 2 parameters)
    def __init__(self, r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,slf):

        real= self.real + slf.real 
        imag=self.imaginary + slf.imaginary
          
          
        if imag<0:
            imag = -1*imag  # removes extra negative sign with imag
            return f"{real} - {imag}i"
        else:
            return f"{real} + {imag}i"
    
    # (a+bi)(c+di)=(ac-bd)+(ad+bc) 
    def __mul__(self,slf):

        mulReal=self.real*slf.real - self.imaginary*slf.imaginary
        mulimag=self.real*slf.imaginary+self.imaginary*slf.real
        

        if mulimag<0:
            mulimag = -1*mulimag  # removes extra negative sign with imag
            return f"{mulReal} - {mulimag}i"
        else:
            return f"{mulReal} + {mulimag}i"
    
    
c1=complex(1,1)
c2=complex(1,-2)

print(c1+c2)
print(c1*c2)