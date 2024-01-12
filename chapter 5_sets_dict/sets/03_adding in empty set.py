'''adding in empty set'''

# empty set
b=set()
print(type(b)) # --> empty set
print(b)

# adding elements in empty set
b.add(4)
b.add(5)
b.add(5) # won't add 5 again as unique values only.

# b.add([4,5,6]) won't add list in set
b.add((4,5,6)) # can add tuple
b.add((4,))
# b.add({4:5}) can't add dictionary as well 
'''only tuple cant change is hashable thus can't be added in sets'''

print(b)


'''properties of sets'''
# 1. sets are unordered
# 2. sets are unindexed
# 3. unchangeable
# 4. has no duplicate values