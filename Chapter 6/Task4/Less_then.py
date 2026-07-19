# find whether a given username contain less then 10 
# character or not

Username = input("Enter User Name Here: ")

if len(Username) < 10:
    print("Contain less then 10 charcter")
else:
    print("Contain more then 10 character")