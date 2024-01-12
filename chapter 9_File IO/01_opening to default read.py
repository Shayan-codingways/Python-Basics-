'''Opening file to read'''

# file opened (by default mode is read (r))
f=open('sample.txt','r')

#reading whole data in file
data=f.read()
print(data)

# closing file
f.close()