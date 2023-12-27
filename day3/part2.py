import re
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)

inputfile = "input.txt"

def findAdjacent(arr, i, j):
    n = len(arr)-1
    m = len(arr[0])-1

    v=[]

    for dx in range (-1 if (i > 0) else 0 , 2 if (i < n) else 1):
        for dy in range( -1 if (j > 0) else 0,2 if (j < m) else 1):
            if (dx != 0 or dy != 0):
                v.append(arr[i + dx][j + dy])
    return v

def getNumber(list, digit, j):
    # input cord is start of num
    # Size of given 2d array
    n = len(list)
    if j+1 < n:
        if list[j+1].isdigit():
            digit.append(list[j+1])
            digit = getNumber(list, digit, j+1)
    return digit

#transform input into 2D array
#replace garbage symbols
#consolidate numbers
schematic = []
flag_innumber = False
with open(inputfile) as f:
    lines = f.readlines()
    for y, line in enumerate(lines):
        line = line.strip()
        row = []
        for x, character in enumerate(line):
            if character.isdigit():
                # print(f"Digit found! {character}, at ({x},{y})")
                # print(f"flag for innumber is currently {flag_innumber}")
                if flag_innumber == False:
                    num = getNumber(line, [character], x)
                    counter = len(num)-1
                    # print(f"the num is {num} and we will iterate {counter} times")
                    if len(num) > 1:
                        flag_innumber = True
                    num = int("".join(num))
                    row.append(num)
                elif counter > 0: 
                    counter -= 1
                    row.append(num)
                else: 
                    flag_innumber = False
                    row.append(character)
            #filter out garbage, only digits, periods and "P"
            elif character == "*":
                row.append("*")
                flag_innumber = False
            else:
                row.append(".")
                flag_innumber = False
        schematic.append(row)

for line in schematic:
    print(line)

#Find *, then find adjacent #. drop duplicates, must be  2 nums remaining

dimx = range(len(schematic))
dimy = range(len(schematic[0]))
flag_innumber = False
gear_box = []
for x in dimx:
    for y in dimy:
        if schematic[x][y] == "*":
            print(f"* found! {schematic[x][y]}, at ({x},{y})")
            adjacent_things = findAdjacent(schematic, x, y)
            print(adjacent_things)
            setlist = list(set(adjacent_things))
            print(setlist)
            # digits=[i for i in adjacent_things if i.isdigit()]
            # print(digits)
            num_set = []
            for item in setlist:
                if str(item).isdigit():
                    if len(num_set) < 3:
                        num_set.append(item)
            print(num_set)
            if len(num_set) == 2:
                gear_ratio = num_set[0]*num_set[1]
                gear_box.append(gear_ratio)
sum=0
for gear in gear_box:
    sum += gear

print(sum)