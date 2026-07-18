# Write a program to find Greatest of four numbers entered by the user

A = int(input("Enter Number Here: "))
B = int(input("Enter Number Here: "))
C = int(input("Enter Number Here: "))
D = int(input("Enter Number Here: "))


if (A > B and A > C and A > D):
    print("A is Greatest")
elif (B > C and B > D):
    print("B is Greatest")
elif (C > D):
    print("C is Greatest")
else:
    print("D is Greatest")