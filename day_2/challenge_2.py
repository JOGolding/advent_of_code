file = 'day_2\input.txt' 
aim = 0
depth = 0
horizPos = 0
with open(file, 'r+') as f:
    for line in f:
        lineList = line.split()
        if lineList[0] == 'forward':
            horizPos += int(lineList[1])
            depth += aim*int(lineList[1])
        elif lineList[0] == 'down':
            aim += int(lineList[1])
        else:
            aim -= int(lineList[1])
print(horizPos*depth)
