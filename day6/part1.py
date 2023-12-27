inputfile = "input.txt"

with open(inputfile) as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        