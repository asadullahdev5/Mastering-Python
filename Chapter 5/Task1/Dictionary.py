# Write a program to create dictionary of urdu words with values as 
# their english translation provide user an optionn to look

Words = {"Shakhs" : "People",
        "Orat" :"Women",
        "Larka" :"Boy",
        "Larki" :"Girl",
        "Bacha" :"Kid",
        "Ami" :"Mother",
        "Abu" :"Father",
        "Bhai" :"Brother",
        "Behn" :"Sister",
        "Chachu" :"Uncle" }

User = input("Enter Your Optio Here Y/N: ")

if(User == "y" or User == "Y"):
    print(Words)
elif (User == "n"or User == "N"):
    print("You Close the Program")
else :
    print("Choose Only y and n")