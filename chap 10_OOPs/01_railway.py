
# class formed (form formed for railway reservation)
'''Application form'''
class RailwayForm:
    
    # class attribute
    formType="RailwayForm"
    
    # method
    def printData(self):
        print(f"name is {self.name}")
        print(f"name is {self.train}")

# making object
harrysApplication=RailwayForm()  # harry initialing empty form
# --> harrysapplication will go to self *self = harrysapplication*

'''data filling'''
# self.name, self.train 
harrysApplication.name="Harry"
harrysApplication.train='Shalimar express'

# method called
harrysApplication.printData()  # ==  RailwayForm.printData(harrysApplication)
RailwayForm.printData(harrysApplication) 
