# A spam comment is defined as a text containsing following keywords 
# "make a lot of money", "buy now" , "subscribe this", "click now" 
# Write a program to detect these spams

# Spam = "make a lot of money" , "buy now" , "subscribe this" ,"click now"

# Without spam words 

Comment = "I started learning Python a few weeks " \
"ago and have been practicing every day. Today I " \
"completed a small program to detect spam comments using conditional statements. " \
"It helped me understand how to build logic and improve my problem-solving skills."
Comment = Comment.lower()

# Conatin Spam words = ["make a lot of money", "buy now", "subscribe this", "click now"]

# Comment = "Congratulations! You can make a lot of money by joining our exclusive program. " \
# "Buy now to get a special discount before the offer expires. " \
# "Don't wait—click now and subscribe this channel to receive more amazing deals and updates."
# Comment = Comment.lower()

if ("make a lot of money" in Comment or "buy now" in Comment or "subscribe this" in Comment or "click now" in Comment):
    print("These Comment Conatin Spam Words")
else:
    print("Nothing have any spam word")