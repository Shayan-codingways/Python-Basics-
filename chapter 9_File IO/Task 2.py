# function for game score
def game():
    return 64


# storing cuurent score value through game functionm 
score=game()
print(score)

# reading score from file
with open('hiscore.txt') as f:  # file read string so we converted to int for comparison 
    hiscorestr=(f.read())    

# comparing scores and writing if condition is true
if score>int(hiscorestr) or hiscorestr=="":       
   with open('hiscore.txt','w') as f:
       f.write(str(score))   # file takes string input
    