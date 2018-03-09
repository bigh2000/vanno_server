import os

# Open a file
path = "./data/jester"
try:
    dirs = os.listdir(path)
except:
    os.makedirs(path)
    dirs = os.listdir(path)
dirs.sort()

make_path="./results/jester"
pre_dirs = os.listdir(make_path)
pre_dirs.sort()
print(dirs)
print(pre_dirs)

for d in dirs:
    if d not in pre_dirs:
        directory=make_path+"/"+d
        os.makedirs(directory)
