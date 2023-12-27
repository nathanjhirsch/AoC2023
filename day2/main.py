class GameRoll:
    def __init__(self, id_input, red_input, blue_input, green_input, string_input = None):
        self.id_num = int(id_input)
        self.red = int(red_input)
        self.blue = int(blue_input)
        self.green = int(green_input)
        self.string = string_input

    def __repr__(self):
        return f"Game {self.id_num}: {self.blue} blue, {self.red} red, {self.green} green"

inputfile = "input.txt"

Games_Objlist = []
game_list = []
with open(inputfile) as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        #do some parsing magic to get the game ID
        split_1 = line.split(": ")
        game_id = split_1[0].split(" ")[1]
        game_list.append(int(game_id))
        #do some parsing magic to get the color options
        rolls = split_1[1].split("; ")
        for roll in rolls:
            colors = roll.split(", ")
            blue = 0
            green = 0
            red = 0
            for color in colors:
                if "blue" in color:
                    blue = color.split(" ")[0]
                elif "green" in color:
                    green = count = color.split(" ")[0]
                elif "red" in color:
                    red = count = color.split(" ")[0]

            Games_Objlist.append(GameRoll(game_id, red, blue, green))
            
# Add blank game at end to trigger rollup correctly. Dumb and hacky but w/e            
Games_Objlist.append(GameRoll(Games_Objlist[len(Games_Objlist)-1].id_num + 1, 0, 0, 0))

power_list = []
starting_id = 1
red_max = 0
blue_max = 0
green_max = 0

for game in Games_Objlist:
    print(game)
    if game.id_num != starting_id:      
        #record previous game_id power
        print(f"blue_max: {blue_max}, red_max: {red_max}, green_max: {green_max}")
        power = red_max*blue_max*green_max
        power_list.append(power)
        print(power)

        #prepare for new game_id
        red_max = 0
        blue_max = 0
        green_max = 0
        starting_id = game.id_num

    if game.red > red_max:
        red_max = game.red
    if game.blue > blue_max:
        blue_max = game.blue
    if game.green > green_max:
        green_max = game.green
        #problem is the else statement isn't triggered by last row.. we could just fake this by adding one more gameobj.
sum=0

for power in power_list:
    sum += power

print(sum)