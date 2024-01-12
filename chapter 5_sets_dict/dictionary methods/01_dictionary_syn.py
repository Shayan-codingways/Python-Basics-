'''                Dictionary Syntax                      '''


myDict={
    "Fast":  "In a quick manner", # fast is key and def is value.
    "Harry": "A Coder",
    "Marks": [1,2,4],
    
    # "nested dictionary with colon"
    "another_dict":{
        'harry': 'Player'
    }
}

# printing/displaying
print("1.", myDict["Fast"])
print("2.", myDict["Harry"])
print("3.", myDict["Marks"])

print("4.", myDict["another_dict"])
print("5.", myDict["another_dict"]['harry'])



'''properties of dictionary'''
# 1. unordered
# 2. mutable (changeable)

'''eg'''
myDict["Marks"]=[45,78]
print("\n\"changeable\"", myDict["Marks"])

# 3. it is indexed
# 4. no duplicate keys 
