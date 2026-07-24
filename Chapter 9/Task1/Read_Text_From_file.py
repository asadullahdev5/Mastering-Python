# Read the text from a given file 'poems.txt' and find out whether it contains the word twinkle

f = open("D:\AI Engineering\Twinkle.txt" , "r")
text = f.read()
Appearing_Count = text.count("Twinkle")
print(text)
print("Twinkle Appear in: ", Appearing_Count , "Times")