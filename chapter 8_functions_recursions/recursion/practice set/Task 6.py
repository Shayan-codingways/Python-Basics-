'''inches to centimeters'''

def inc_to_cm(inch=0):
   cm = inch*2.54
   return cm
    
    
    
inch=int(input('Enter measurement in inches '))

print('Farenheit Temperature is:'+ str(inc_to_cm(inch)))
print(inc_to_cm()) # at c=0, f=32