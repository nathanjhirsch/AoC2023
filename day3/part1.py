import re
import logging

logging.basicConfig(filename='example.log', level=logging.DEBUG)

inputfile = "input.txt"

filter = re.compile("[^.{0-9]")
#transform input into 2D array
schematic = []
with open(inputfile) as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        row = []
        for character in line:
            #filter out garbage, only digits, periods and "P"
            if filter.match(character):
                row.append("P")
            else: row.append(character)
        schematic.append(row)

def findAdjacent(arr, i, j):
    n = len(arr)-1
    m = len(arr[0])-1

    v=[]

    for dx in range (-1 if (i > 0) else 0 , 2 if (i < n) else 1):
        for dy in range( -1 if (j > 0) else 0,2 if (j < m) else 1):
            if (dx != 0 or dy != 0):
                v.append(arr[i + dx][j + dy])
    return v

def getNumber(arr, digit, part_flag, i, j):
    # input cord is start of num
    # Size of given 2d array
    adjacentvector = findAdjacent(arr, i, j)
    if part_flag == False:
        if "P" in adjacentvector: 
            part_flag = True
    n = len(arr[i])
    if j+1 < n:
        if arr[i][j+1].isdigit():
            digit.append(arr[i][j+1])
            digit, part_flag = getNumber(arr, digit, part_flag, i, j+1)
    return digit, part_flag

dimx = range(len(schematic))
dimy = range(len(schematic[0]))
flag_innumber = False
num_list = []
for x in dimx:
    counter = 0
    flag_innumber = False
    for y in dimy:
        if schematic[x][y].isdigit():
            if flag_innumber == False:
                # print(f"Digit found! {schematic[x][y]}, at ({x},{y})")
                num, partornot = getNumber(schematic, [schematic[x][y]], False, x, y)
                counter = len(num)-2
                if len(num) > 1:
                    flag_innumber = True
                num = int("".join(num))
                if partornot: num_list.append(num)
            elif counter > 0: counter -= 1
            else: flag_innumber = False
        if flag_innumber:continue

sum=0
for num in num_list:
    sum += num

print(sum)