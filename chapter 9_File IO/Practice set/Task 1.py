
f=open('poem.txt','r')

a = f.read()
print(a)

a=a.replace('T','t')
a=a.replace('W','w')
a=a.replace('I','i')
a=a.replace('N','n')
a=a.replace('K','k')
a=a.replace('L','l')
a=a.replace('E','e')

print(a)


if 'twinkle' in a:
   print('Twinkle is present')
else:
   print('Twinkle is not present')


f.close()