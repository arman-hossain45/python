# import os
# if(not os.path.exists("data")):
#     os.mkdir("data")#ossystem folder inside create a file named data

# for i in range(1,4):
#     os.mkdir(f"data/day{i+1}")#inside data folder create 3 folders named day1,day2,day3

# #if we want to rename 3 folder name then write this code 
# import os
# for i in range(1,4):
#  os.rename(f"data/day{i+1}",f"data/tutorial{i+1}")
#
#if we want to see any file or folder is exits or not then write this code syntax
import os
folders=os.listdir("data")
print(folders)
for folder in folders:
    print(folder)

    print(os.listdir(f"data/{folder}"))
    print(os.getcwd())
