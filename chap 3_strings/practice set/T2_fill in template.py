'''TAsk 2'''

letter='Dear <|name|>\n\t\tYou are selected!\n\t\t\t <|date|> '

name=input('Enter name: ')
date=input('Enter date: ')


'''won't work'''
# letter.replace('<|name|>',name)
# letter.replace('<|date|>',date)

'''work!'''
letter=letter.replace('|name|',name)
letter=letter.replace('|date|',date)

print(letter)