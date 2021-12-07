from os import read


def readFile(fileName):
    fileObj = open(fileName, 'r')
    numsString = fileObj.read().splitlines()
    nums = list(map(int, numsString))
    fileObj.close()
    return nums
    
numArray = readFile('day_1\input.txt')
total = 0
prevTotal = 0
increaseCount = 0
for x in range(len(numArray)-2):
    total = numArray[x] + numArray[x+1] + numArray[x+2]
    if prevTotal == 0:
        prevTotal = total
    elif total > prevTotal:
        increaseCount+=1
        prevTotal = total
    else:
        prevTotal = total

print(increaseCount)




