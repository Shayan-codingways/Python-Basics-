# Normal behaviour

                                 # 1

i=0
while(i<=50):
    print("i = " + str(i))
    i+=1

print('Done')

                                 # 2

i=0
while i<5:
    print("Shayan")
    i+=1

                                 # 3 (shayan  hayan  ayan  yan an n)
string = 'shayan'
i=0
while (i != 6) :
       print(string[i])
       i+=1


                                # 4 (s  sh  sha  shay  shaya  shayan)
print("\n")
string = 'shayan'
i=0
while (i != 6) :
    j=0

    while (j != i+1):
        print(string[j])
        j+=1

    i+=1
    print("\n")
    

                                 # 5 content of list
list=[1,45,67.8,(4,5,6),{4:34}, 'Harry']
len(list)
fruits=['mango','apple','peach']
i=0
while(i < (len(fruits))):
     print(fruits[i])
     i=+1