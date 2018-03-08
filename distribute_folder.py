import os, sys, json
from random import shuffle

# Open a file
path = "./data/jester"
dirs = os.listdir( path )
ids=[]

make_path="./env/jester"
with open("ids.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        ids.append(line.replace("\n",""))

n_folder_per_id=1

folder_dict={i:[] for i in ids}

shuffle(dirs)

print(ids,folder_dict)


k=0
for i in ids:
	if i <> "vdo_ver":
		for j in range(n_folder_per_id):
			folder_dict[i].append(dirs[k])
			k+=1

json.dump(folder_dict,open(os.path.join(make_path,"job_assign.json"),"w"),indent=4)
	
