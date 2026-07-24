# A file contain a censor words multiple times. 
# you need to write a program which 
# replace this words with ###### by updating the same file

bad_words = ["idiot","shit", "fuck", "fucking", "lucifer", "bastard"]

with open("D:\AI Engineering\Txt Files For Chapter 9\Paragraph.txt", 'r') as f:
    text = f.read()


for word in bad_words:
    text = text.replace(word, "#########")


    with open("D:\AI Engineering\Txt Files For Chapter 9\File.txt" , 'w') as f:
        f.write(text)
    print("Word is updated")

