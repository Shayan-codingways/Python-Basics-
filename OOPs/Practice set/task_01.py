class Programmers:
    company="Microsoft"
    
    # constructor
    def __init__(self,name,product):
        self.name=name
        self.product=product

    def getinfo(self):
        print(f"name of programmer at {self.company} is {self.name} annd product is {self.product}")

harry = Programmers("Harry","Skype")
Azka = Programmers("Azka","Git")

harry.getinfo()
Azka.getinfo()