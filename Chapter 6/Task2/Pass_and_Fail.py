# Write a Program to find out whether a Student it pass or 
# fail require 40% and each subject in 33% to pass

Sub1 = int(input("Enter phy marks: "))
Sub2 = int(input("Enter Math marks: "))
Sub3 = int(input("Enter Eng marks: "))

Total = 300
Obtained = Sub1 + Sub2 + Sub3

if (Sub1 >= 33 and Sub2 >= 33 and Sub3 >= 33) and (Obtained >= Total * 0.4):
    print("You Passed")
else:
    print("You Failed")

