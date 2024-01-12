
# class formed (form formed for railway reservation)
class RailwayForm:
    formType="RailwayForm"

    def printData(self):
        print(f"name is {self.name}")
        print(f"name is {self.train}")

# making object (new application formed, data filled, print)

'''new application'''
harrysApplication=RailwayForm()  # harry initialing empty form 

'''data filling'''
harrysApplication.name="Harry"
harrysApplication.train='Shalimar express'

'''print'''
harrysApplication.printData()



# Why OOPS?
'''
maintaing application
real world modelling
'''