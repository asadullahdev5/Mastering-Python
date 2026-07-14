import os 

folder_path = "D:\Learning Books"
contents = os.listdir(folder_path)

print("These Items are Inside The Folders")
for item in contents:
    print(item)