import os

# rename a file 
with open('t11.txt') as f:
    data=f.read()
    
with open('renamed by python.txt','w') as f:
    f.write(data)  # new file formed
    
# now delete old file.
os.remove('t11.txt')