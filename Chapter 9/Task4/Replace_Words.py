# A file contain a word "Donkey" multiple times. 
# you need to write a program which 
# replace this words with ###### by updating the same file

with open("D:\AI Engineering\Txt Files For Chapter 9\File.txt" , 'r') as f:
    text = f.read()

if "donkey" in text.lower():
    new_text = text.replace("Donkey", "########") \
                    .replace("donkey", "########")\
                    .replace("DONKEY", "########")


    with open("D:\AI Engineering\Txt Files For Chapter 9\File.txt" , 'w') as f:
        f.write(new_text)
    print("Word is updated")
else:
    print("Word not found")













# Score = 99

# f = open("D:\AI Engineering\Txt Files For Chapter 9\Score.txt","r")
# text = f.read()
# f.close()

# old = int(text)

# if Score > old:
#     f = open("D:\AI Engineering\Txt Files For Chapter 9\Score.txt","w")
#     text = f.write(str(Score))
#     f.close()    
#     print("High Score Updated:", Score)
# else:
#     print("Score Not Breaked: " ,old)