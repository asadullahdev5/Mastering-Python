# Genrate multiplicaion tables from 2 to 20 and write 
# it to the diffrent files place these files in a folder of 13 years old

import os 

folder_name = '13 years old'

if not os.path.exists(folder_name):
    os.makedirs(folder_name)

for i in range(2, 21):
    file_name = os.path.join(folder_name, f"Table_{i}.txt")

    f = open(file_name, "w")

    for j in range (1, 11):
        f.write(f"{i} X {j} = {i * j}\n")

    f.close()
print("Completed all tables on Thirteen Years old folder ")