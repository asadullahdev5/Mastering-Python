# write a program to greet all the person names stored in a list l1 and start with s 

l1 = ["Asad", "Salman" , "Sanam" , "Sahil", "Ali"]

for name in l1:
    if name.upper().startswith("S"):
        print("Hello", name , "Good Morning")