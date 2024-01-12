
'''BEst way of opening and closing file automatically!'''
# no need to close file in with

with open('another.txt','r') as file:
    a=file.read()
    print(a)

with open('another.txt','w') as file:
    a=file.write('me')
    