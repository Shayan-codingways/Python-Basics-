
f=open('task5.txt')
content=f.read()

content=content.replace('D','d')
content=content.replace('O','o')
content=content.replace('N','n')
content=content.replace('K','k')
content=content.replace('E','e')
content=content.replace('Y','y')

if 'donkey' in content:
    content=content.replace('donkey','######')

f.close()

f=open('task5.txt','w')
f.write(content)