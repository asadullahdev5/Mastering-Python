# Write a program to print the following star pattren 

n = 5
for i in range (1, n+1):
    print(" " * (n - i), end="")
    print("*" * (2*i  - 1))