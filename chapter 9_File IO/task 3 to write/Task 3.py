# printing 2-20 tables in file
# files for write generates itself

for j in range(2,21): 
    
    # file name given and content written 
    with open(f'multipicationtable table of {j}.txt','w') as file:
 
        for i in range(1,11):
            file.write(f"{j}*{i}={i*j} \n")
    
        print("\n")
    
  


  