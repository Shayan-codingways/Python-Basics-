'''              slicing with skip value                    '''

name='shayan'
d=name[1:4:1] # skip value 1 but it won't skip as 1 value will print
c=name[1:4:2] # skip value 2

print(d)
print(c)


e=name[0::2]
print(e) # skips alterantely 2nd value !!! ans is ''saa'' !!!




'''example'''

story="Once upon a time there was a youtuber named harry who uploaded python course with notes."

print(story[0])
print(story[0:5])
print(story[0:])
print(story[:5])
print(story[:-1])
print(story[0::3])
print(story[0::1])
