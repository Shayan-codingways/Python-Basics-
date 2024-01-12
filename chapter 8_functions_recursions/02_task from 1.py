'''       Function making!        '''
# function
def percent(marks):
   
    sum=0
    for i in marks:
        sum=sum+i

   
    percentage=(sum/400)*100

    return percentage

# marks1 called
marks1=[45,78,86,77]
a=percent(marks1)
percentage1=a

# marks 2 called
marks2=[44,34,45,73]
b=percent(marks2)
percentage2=b

# display
print(percentage1,percentage2)
