import os

# Open a file
path = "./data/jester"
dirs = os.listdir(path)

make_path="./results/jester"
pre_dirs = os.listdir(make_path)
print(dirs, pre_dirs)

for d in dirs:
    if d not in pre_dirs:
        directory=make_path+"/"+d
        os.makedirs(directory)
