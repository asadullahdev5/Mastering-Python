# program to calculate the grade of a student from his marks from the following scheme
# 90 - 100 Ex
# 80 - 90 A
# 70 - 80 B
# 60 -70 C
# 50 - 60 D
# < 50 F

Marks = int(input("Enter Marks: "))

if(Marks > 90 and Marks <= 100):
    print("Excellent")
elif(Marks > 80 and Marks <= 90):
    print("You got A")
elif(Marks > 70 and Marks <= 80):
    print("You got B")
elif(Marks > 60 and Marks <= 70):
    print("You got C")
elif(Marks > 50 and Marks <= 60):
    print("You got D")
else:
    print("Failed")