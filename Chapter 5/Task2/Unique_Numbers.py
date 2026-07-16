# input eight numbers from user and display unique numbers


Unique_list = []
for U in range(1,8):
    Number = int(input("Enter Number: "))
    if(Number not in Unique_list):
        Unique_list.append(Number)
Unique_list.sort()
print("Unique Numbers are: ", Unique_list)



