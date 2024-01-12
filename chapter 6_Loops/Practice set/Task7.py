'''        star printing        '''

n=4
for i in range(4):
    print("*" * (i+1))





print("\n")
n=3
for i in range(3):
    print(" " * (n-1-i), end='')
    print("*" * (2*i+1),  end = "")  # end function eliminates default line break  
    print(" " * (n-1-i))