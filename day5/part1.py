from tqdm import tqdm

inputfile = "input.txt"

insoilmap = False
infertmap = False
inwatermap = False
inlightmap = False
intempmap = False
inhummap = False
inlocmap = False

mapping_dict = {
    "seed2soil":{},
    "soil2fert":{},
    "fert2watr":{},
    "watr2lght":{},
    "lght2temp":{},
    "temp2hmdy":{},
    "hmdy2spot":{},
}

def build_mapping_dict(book, name, line):
    row = len(book[name])
    book[name][row] = {
        "input": int(line[1]),
        "output": int(line[0]),
        "length": int(line[2])
    }

with open(inputfile) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        # print(line)
        if line[:5] == "seeds":
            seeds = line[7:].split(" ")
        if (line[:17] == "seed-to-soil map:" or insoilmap):
            if not insoilmap: insoilmap = True
            elif line != "":
                build_mapping_dict(mapping_dict, "seed2soil", line.split(" "))
            else: insoilmap = False
        if (line[:23] == "soil-to-fertilizer map:" or infertmap):
            if not infertmap: infertmap = True
            elif line != "":
                build_mapping_dict(mapping_dict, "soil2fert", line.split(" "))
            else: infertmap = False
        if (line[:24] == "fertilizer-to-water map:" or inwatermap):
            if not inwatermap: inwatermap = True
            elif line != "":
                build_mapping_dict(mapping_dict, "fert2watr", line.split(" "))
            else: inwatermap = False
        if (line[:19] == "water-to-light map:" or inlightmap):
            if not inlightmap: inlightmap = True
            elif line != "":
                build_mapping_dict(mapping_dict, "watr2lght", line.split(" "))
            else: inlightmap = False
        if (line[:25] == "light-to-temperature map:" or intempmap):
            if not intempmap: intempmap = True
            elif line != "":
                build_mapping_dict(mapping_dict, "lght2temp", line.split(" "))
            else: intempmap = False
        if (line[:28] == "temperature-to-humidity map:" or inhummap):
            if not inhummap: inhummap = True
            elif line != "":
                build_mapping_dict(mapping_dict, "temp2hmdy", line.split(" "))
            else: inhummap = False
        if (line[:25] == "humidity-to-location map:" or inlocmap):
            if not inlocmap: inlocmap = True
            elif line != "":
                build_mapping_dict(mapping_dict, "hmdy2spot", line.split(" "))
            else: inlocmap = False

def transformer(dict, dictkey, seed):
    seedmap = dict[dictkey]
    # print(seedmap)
    transformation = 0
    for key in seedmap.keys():
        #this is iterating through Ids
        if seed >= seedmap[key]["input"] and seed < (seedmap[key]["input"] + seedmap[key]["length"]):
            # print(f"seed: {seed}, input: {seedmap[key]["input"]}, length: {seedmap[key]["length"]}, output: {seedmap[key]["output"]}")
            transformation = seed-seedmap[key]["input"]+seedmap[key]["output"]
    if transformation == 0: transformation = seed
    return(transformation)

locations=[]

for i, seed in enumerate(seeds):
    # print(f"mapping seed {i+1} of {len(seeds)}: {seed}")
    seed = int(seed)
    temp = 0
    for key in mapping_dict.keys():
        seed = transformer(mapping_dict, key, seed)
        # print(f"working key: {key}, transform to {seed}")
    locations.append(seed)

locations.sort()
print(locations[0])