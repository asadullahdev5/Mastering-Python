# Program get marks of students and sort them in ascending order

marks = []
for m in range(1,7):
    value = float(input("Enter marks Here:"))
    marks.append(value)
marks.sort()
print("Marks in ascending order:", marks)