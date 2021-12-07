file = 'day_2\input.txt' 
aim = 0
depth = 0
horizPos = 0
with open(file, 'r+') as f:
    for line in f:
        lineList = line.split()
        value = int(lineList[1])
        if lineList[0] == 'forward':
            horizPos += value
            depth += aim*value
        elif lineList[0] == 'down':
            aim += value
        else:
            aim -= value
print(horizPos*depth)
