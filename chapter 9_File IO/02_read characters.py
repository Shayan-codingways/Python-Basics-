
# file opened (by default mode is read (r))
f=open('sample.txt')


print(f.read())
print('\n')
# reading 5 characters in file
data=f.read(5)
print(data)



# closing file
f.close()