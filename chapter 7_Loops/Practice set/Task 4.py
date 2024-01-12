'''prime number'''

num=int(input("Enter number: "))

Prime=True
for i in range(2,num):
    if(num%i==0):
        Prime=False
        break



if(Prime):
   print("This number is prime")
else:
   print("Number is not prime") 
    