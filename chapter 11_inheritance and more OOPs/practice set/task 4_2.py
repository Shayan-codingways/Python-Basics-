class complex:

    # initialize complex num (has 2 parameters) 
    # now complex is like complex(self.real , self.imag)
    def __init__(self, r,i):
        self.real=r
        self.imaginary=i

    def __add__(self,slf):
        real = self.real + slf.real 
        imag = self.imaginary + slf.imaginary
        
        # returned as a complex num
        return complex(real, imag)

    # (a+bi)(c+di)=(ac-bd)+(ad+bc) 
    def __mul__(self,slf):
        mulReal=self.real*slf.real - self.imaginary*slf.imaginary
        mulimag=self.real*slf.imaginary + self.imaginary*slf.real

        return complex(mulReal,mulimag) # returned as a new complex num
    
    def __str__(self):

        if self.imaginary<0:  #(self.imag = mulimag)
            self.imaginary = -1*self.imaginary  # removes extra negative sign with imag
            return f"{self.real} - {self.imaginary}i"
        
        else:
            return f"{self.real} + {self.imaginary}i"
    
    
c1=complex(1,4)
c2=complex(8,-2)

print(c1+c2)
print(c1*c2)