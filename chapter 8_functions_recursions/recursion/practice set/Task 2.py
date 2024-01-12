'''Celsius to fareheit'''

def celsius_to_Fare(celsius=0):
   
   F= 32+(celsius*9/5)
   return F
    
    
    
c=int(input('Enter temp in celsius '))

print('Farenheit Temperature is:'+ str(celsius_to_Fare(c)))
print(celsius_to_Fare()) # at c=0, f=32
