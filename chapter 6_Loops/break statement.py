'''break exit the loop!'''

for i in range (10):
   print(i)

   if i==5:
       break
# else won't execute as loop has terminated.  else only works when loop completely terminates succesfully   
else:
    print("Done")