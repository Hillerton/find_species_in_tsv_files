
import sys

tree_file = sys.argv[1]
file2 = sys.argv[2]
out = sys.argv[3]

list_dict = dict()
counter = 0

with open(tree_file, "r") as reader:
    next(reader)
    for line in reader:
        line = line.rstrip()
        
        tree = line.split("\t")[1]

        tree = tree.replace("(", "")
        tree = tree.replace(")", "")
        tree = tree.split(",")

        for i in tree:
           counter+=1
           i = i.split(":")[0]
           list_dict[counter] = i

reader.close()
           
species = dict()

with open(file2) as reader:
    for line in reader:
        line = line.rstrip()
        wanted = line.split("\t")

        species[wanted[0]] = wanted[1]+"\t"+wanted[2]

seen_species = list()
        
for val in list_dict.values():
    if val in species.keys():
        if species[val] not in seen_species:
            seen_species.append(species[val]) 

writer = open(out, "w+")

writer.write("#### species found in the QfO18 data ####\n")

for i in seen_species:
    writer.write(i+"\n")

store = list()
    
writer.write("\n\n#### species not found in QfO18 data ####\n")    
for j in species.values():
    if j not in seen_species:
        if j not in store:
            store.append(j)

writer.write("\n".join(store))
writer.close()
