# find out whether a given name is present in a list or not

Names = ["asAd" , "aLi" , "MubEen"]
user = input("Enter Name: ")
if user.lower() in [name.lower() for name in Names]:
    print("Yes name available")

else:
    print("not available")
