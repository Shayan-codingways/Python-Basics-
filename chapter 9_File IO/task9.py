
file1="copy.txt"
file2="this.txt"

f=open(file1)
content1=f.read()
f.close()

f=open(file2)
content2=f.read()
f.close()


if(content1==content2):
    print("identical")
else:
    print("not identical")