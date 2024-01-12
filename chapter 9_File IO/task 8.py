# making a copy of this .txt

f = open("this.txt") 
content=f.read()
f.close()
print(content)

#write function itself creates a file 
with open("copy.txt",'w') as f:
    f.write(content)