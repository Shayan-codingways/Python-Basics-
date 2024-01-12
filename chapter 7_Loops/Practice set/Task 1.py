'''         number table and f_string!           '''


number= int(input("Enter a number for a table: "))



'''for loop'''
for i in range(0,13):
    a=number*i
    
    # print(str(number) + "*" + str(i) + "=", a) '''printing possibilities'''
    # print(number,"*", i, "=", a)

    print(f"{number} X {i} = {number*i}" )  # f string for display

print("Done")




'''while loop'''
print('\n')
i=1
while (i != 13):
  print(number,"*", i, "=", number*i)
  i+=1