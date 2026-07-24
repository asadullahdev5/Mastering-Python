# Recursive Function to calculate the sum of first n natural numbers

def natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + natural_numbers(n-1)
        

a = natural_numbers(15)
print(a)