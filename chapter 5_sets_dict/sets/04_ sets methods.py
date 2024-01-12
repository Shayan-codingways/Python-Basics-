'''methods'''

b=set()

b.add(4)
b.add(5)
b.add((4,5,6)) # can add tuple only
print(b)

# 1. len(set)
print(len(b)) 

# 2. set.remove(element)
print(b)

b.remove(5) # print(b.remove(5)) --> not right ...
print(b)

# 3. set.pop(no argument) --> removes any random element/tuple.
b.pop()
print(b)

b.pop()
print(b)

# 4. s.clear() --> empties set
b=set()

b.add(4)
b.add(5)
b.add((4,5,6)) # can add tuple
print(b)

b.clear()
print(b)


print("\n\n")
# 5. s.union and intersection

set1={1,2,3,5,7}
set2={2,5,6,7,4}

set3=set1.union(set2)
print(set3)
print(set1 | set2)

set3=set1.intersection(set2)
print(set3)
print(set1 & set2)

# differnce
print(set1 - set2)
print(set2 - set1)

# symmetric differnce
print(set1 ^ set2)

