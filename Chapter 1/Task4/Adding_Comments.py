import os # import os module to work with files and folders

folder_path = "D:\Learning Books"  # give him a folder path
contents = os.listdir(folder_path) # get a list of all files and folders inside

print("These Items are Inside The Folders") # print a heading
for item in contents: # using loop for each item in a list
    print(item) # print the name of the item