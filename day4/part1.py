inputfile = "input.txt"
list_of_keys = []
list_of_rolls = []

with open(inputfile) as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line[8:]
        keys = line.split(" | ")[0].split(" ")
        rolls = line.split(" | ")[1].split(" ")
        keys = [key for key in keys if key != ""]
        rolls = [roll for roll in rolls if roll != ""]
        list_of_keys.append(keys)
        list_of_rolls.append(rolls)

sum = 0
for i, keys in enumerate(list_of_keys):
    rolls = list_of_rolls[i]
    matches = len([j for j in keys if j in rolls])
    # print(f"matches: {matches}")
    if matches == 0:
        points = 0
    else: points = 2**(matches-1)
    # print(f"points: {points}")
    sum += points
print(sum)