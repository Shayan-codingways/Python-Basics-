
'''Dictionary methods/functions'''

myDict={
    "Fast":  "In a quick manner", # fast is key and def is value.
    "Harry": "A Coder",
    "Marks": [1,2,4],
    
    # "nested dictionary with colon"
    "another_dict":{
        'harry': 'Player'
    },
    
    1:2
}

print(type(myDict)) # type is dict

# 1. dictionary.keys(no arg) --> display just all 'keys' in a dict keys form 
print(myDict.keys())

print(type(myDict.keys())) # it is dict keys but we can convert it into to list type
print(list(myDict.keys())) # converted to list type

print("\n")


# 2. dictionary.values --> display just all 'values' in a list form 
print(myDict.values())

print(type(myDict.values())) # it is dict keys but we can convert it into to list type
print(list(myDict.values())) # converted to list type
print(type(list(myDict.values()))) # type is list

print("\n")


# 3. dictionary.items --> return key-value pair in tuple form
print(myDict.items())


# 4. dictionary.update --> updates original dict

'''Original dict'''
print(myDict)


'''new dict'''
updateDict={
   'lovish': 'Friends',
   'Harry': 'dancer' # overwrite previous Harry
}


'''updating in original dict by adding key/value pairs from new dictionary'''
myDict.update(updateDict) 
print(myDict)


# 5. dictionary.get(key)--> return key-value pair in tuple form
print(myDict.get("Harry")) 
print(myDict["Harry"])

'''differnec in these two'''
print(myDict.get("Harry2")) # outputs none 
print(myDict["Harry2"]) # throws error