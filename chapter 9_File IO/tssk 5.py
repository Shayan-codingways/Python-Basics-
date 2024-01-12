with open('t1.txt') as f:
    co=f.read()
    
    co=co.replace("donkey","#$#$$")
    
with open('t1.txt','w') as f:
    f.write(co)