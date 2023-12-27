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

wins = [ ["Original"] for _ in range(len(list_of_keys)) ]
for i, keys in enumerate(list_of_keys):
    rolls = list_of_rolls[i]
    matches = len([j for j in keys if j in rolls])
    # print(f"matches: {matches}")
    cardcount = len(wins[i])
    for j in range(matches):
        for k in range(cardcount):
            wins[i+j+1].append("WIN")
# for line in wins:
    # print(line)
card_count = 0
for cards in wins:
    card_count += len(cards)
print(card_count)  