class Calculator: 
    def square(self):
        return self.num*self.num
     
    def cube(self):
        return self.num*self.num*self.num

    def squareroot(self):
       return self.num **0.5

number=Calculator()
number.num=int(input("Enter a number for square and cube: "))

#a=number.square() 
a=Calculator.square(number)
print(f"Square of {number.num} is {a}")

b=number.cube()
print(f"Square of {number.num} is {b}")

c=number.squareroot()
print(f"Square root of {number.num} is {c}")



