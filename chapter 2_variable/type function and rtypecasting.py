
'''Typecasting converts one datatype to another'''

a="3534"  # now this isn't integer, it is a string in double quote
print("Type of a",type(a))

## print(a+5) won't print 3539 as we can't add integer to string.
print(a+"5") # string joined with string now correct as ans is 35345

'''but still 5 is not added to the number, it is just concatenated'''



'''so now we can do typecasting(change string to integer)'''
a='3534'
a=int(a) ##### int function tries converting string to an integer value #####  
         ##### in this case it'll become 3534 ######
         ##### but as an eg it wouldn't have been able to convert a name eg shayan into intger #####
print(a+5) ##### now ans is 3539 #####



a='344jhgfh5' 
# a=int(a)        # won't work as invalid string.


'''int to string conversion'''
a=31
a=str(a)
print(a)

'''int to float'''
a=222
print(float(a))

b=4
c=7
print(b+c)