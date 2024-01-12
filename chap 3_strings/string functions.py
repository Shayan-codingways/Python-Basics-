'''      String functions      '''

story="once upon a time there was a youtuber named harry. who uploaded python course with notes"

# function 1  len(var)
print(len(story))


# function 2  var.endswith(.....) 
print(story.endswith('sghdhd'))  # false
print(story.endswith('notes'))   # true


# function 2  var.count(alphabet/word)
print(story.count('s'))
print(story.count('notes'))
print(story.count('es'))


# function 2  var.capitalize()
print(story.capitalize())  # capitalizes o starting letter
                           # takes no argument just for 1st alphabet


# function 3  string.find(word)   ****just for 1st occurence****
print(story.find('harry')) 
print(story.find('s')) 
print(story.find('ce')) 
print(story.find('Harry')) # not in string outputs -1
print(story.find('once')) 


# function 3  string.replace(word to replace, with what)
print(story.replace('harry','shayan')) 
print(story.replace('a','T'))  # replaces all alphabets words




