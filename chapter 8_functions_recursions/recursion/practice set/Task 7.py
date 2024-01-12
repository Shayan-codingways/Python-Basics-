'''strip a string'''

def remove_strip(string , word):

   new=string.replace(word,"") # removes word
   
   return new.strip() # removes frwd backward spaces


l1 = "     Harry is a good     "
print(l1)

n=remove_strip(l1,'Harry')
print(n)