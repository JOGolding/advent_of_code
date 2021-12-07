file = 'day_1\input.txt'
prevNum = 0;
increaseCount = 0;    
with open(file, 'r+') as f:
    for line in f:
        if prevNum == 0:
            prevNum = int(line)
        elif int(line) > prevNum:
            increaseCount = increaseCount + 1
            prevNum = int(line)
        else:
            prevNum = int(line)
            
print(increaseCount)