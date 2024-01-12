'''factorial by function'''
# n!= 1*2*3*4*....*n

def factorial(n):
  pro=1
  for i in range(1,n+1):
    pro=pro*i

  return(pro)


num=int(input('number please: '))
ans=factorial(num)
print(ans)


def factorial(n):
  pro=1
  for i in range(n,1,-1):
    print(i)
    pro=pro*i
    

  return(pro)

num=int(input('number please: '))
ans=factorial(num)
print(ans)
