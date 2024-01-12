#wipe out contents of a file

#the write function with no input wipes out content
file='task10.txt'
f=open(file,'w')
f.write("")
f.close()
