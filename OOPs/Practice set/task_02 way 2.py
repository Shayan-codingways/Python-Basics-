class Calculator: 
    def __init__(self,num):
        self.num=num
    
    def square(self):
        print(f"the value of {self.num} square is {self.num **2}")

    def cube(self):
        print(f"the value of {self.num} square is {self.num **3}")

    def squareroot(self):
        print(f"the value of {self.num} square is {self.num **0.5}")
    
    @staticmethod # task 04
    def greet():
        print("***** Hello! Here's your Calculator ******")


a=Calculator(9)

a.greet() #--->  Calculator.greet()
a.square()
a.cube()
a.squareroot()