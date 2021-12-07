from typing import ItemsView


file='day_3/input.txt'

def splitBinary(string):
    return [x for x in string]

def readFile(fileName):
    fileObj = open(fileName, 'r')
    numsString = fileObj.read().splitlines()
    numsSplit = []
    for i in numsString:
        numsSplit.append(splitBinary(i))
    fileObj.close()
    return numsSplit

def extract(lst, n):
    return [item[n] for item in lst]

numSplitList = readFile(file)
mostCommonBits = ''

for i in range(len(numSplitList[0])):
    for x in numSplitList:
        extractedList = extract(numSplitList, i)
        modeBit = max(set(extractedList), key=extractedList.count)
    mostCommonBits += str(modeBit)

inverseMCB = ''.join(['1' if i == '0' else '0'
                     for i in mostCommonBits])

print(int(mostCommonBits,2)*int(inverseMCB,2))




