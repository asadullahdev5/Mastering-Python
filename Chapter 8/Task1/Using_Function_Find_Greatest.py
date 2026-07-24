# Write a program using function to find greatest of three numbers

def greatest (a , b , c):
    if (a >= b or a >=c):
        return"A greater"
    elif (b >= c):
        return"B is Greater"
    else:
        return "C is Greater"

num1 = 2
num2 = 9
num3 = 7

Find = greatest(num1, num2, num3)
print(Find)