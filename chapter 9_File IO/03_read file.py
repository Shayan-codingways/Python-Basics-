'''Opening file to read'''

# file opened (by default mode is read (r))
f=open('sample.txt')

# read 1st line in file
data=f.readline()  
print(data)

# read 2nd line's first 2 characters in file
data=f.readline(2)
print(data)

# read 2nd line's remaining characters in file
data=f.readline()
print(data)

# closing file
f.close()