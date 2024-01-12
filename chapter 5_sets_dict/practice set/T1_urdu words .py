''' Task 1 -- >  urdu to english dictionary '''

myDict={
    "Pankha": "Fan",
    "Dabba" : "Box",
    "Daraz" : "cupboard"
}

print("The options are: ",myDict.keys())

a=input("Enter the Urdu word: ")

# print("The menaing of your word is: ", myDict[a]) --> throw error if input is wrong
print("The menaing of your word is: ", myDict.get(a)) # --> will not throw an error