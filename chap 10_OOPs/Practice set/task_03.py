
'''class'''
class sample:

    '''class attribute a'''
    a="Harry"

# object formed
object=sample()

#creating instance/object attribute 
object.a="vicky"

# won't change class attribute
print(sample.a)
print(object.a)

sample.a='vicky'
print(sample.a)