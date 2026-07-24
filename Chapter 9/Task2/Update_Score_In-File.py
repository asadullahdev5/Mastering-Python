# The game function in a program lets a 
# user play a game and return the score as an 
# intger. you need to read a file 'Hi_Score.txt' 
# which is either is blank contain the previsous hi 
# score yoou need to write a program to update the 
# high score whenever the game breaks the high score
Score = 99

f = open("D:\AI Engineering\Txt Files For Chapter 9\Score.txt","r")
text = f.read()
f.close()

old = int(text)

if Score > old:
    f = open("D:\AI Engineering\Txt Files For Chapter 9\Score.txt","w")
    text = f.write(str(Score))
    f.close()    
    print("High Score Updated:", Score)
else:
    print("Score Not Breaked: " ,old)