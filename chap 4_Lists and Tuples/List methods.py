'''Lsit methods'''

# ..1 (list.sort) --> ascending order

l1=[1,8,7,2,21,15] 
# l1=l1.sort()  not a correct way to do.

l1.sort()
print(l1)


# ..2 (list.reverse) --> reverse order

l1=[1,8,7,2,21,15] 

l1.reverse()
print(l1)


# ..3 (list.append(object to append)) --> adds to the end

l1=[1,8,7,2,21,15] 

l1.append('***')  # add to the end of document
print(l1)

l1.append(56) 
print(l1)


# ..4 (list.insert(index,value)) --> inserts obeject at particular index

l1=[1,8,7,2,21,15] 

l1.insert(0,544)  # adds 544 to index 0
l1.insert(2,'544')  # adds 544 to index 2
print(l1)


# ..5 (list.pop(index no)) --> remove obeject from particular index as input

l1=[1,8,7,2,21,15] 

l1.pop(2)  # remover object of at index 2 (removes 7)
print(l1)


# ..6 (list.remove) --> removes obeject by having object as input

l1=[1,8,7,2,21,15] 

l1.remove(21)  # removes a number/object from list
print(l1)


# ..7 (list.count) --> counts a particular element

l1=[1,8,7,2,21,34,34,21,23,21,15] 

a=l1.count(21)  # counts
print(a)
