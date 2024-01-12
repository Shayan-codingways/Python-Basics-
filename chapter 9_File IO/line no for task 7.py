# knowing the line for python


with open('logfile.txt') as f:
    
   data=""  # showing content exist at start(initialize)
   i=1
    
    # reading and line untill content lines exist
while data: 
    data=f.readline()
    print(data)
    i+=1
    
    
    if 'python' in data.lower():  #content.lower converts whole content in lower case 
        print("python present at" + i )
    else:
        print("python not present")
