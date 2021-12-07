file='day_3/input.txt'

def readFile(fileName):
    fileObj = open(fileName, 'r')
    binaryStrings = fileObj.read().splitlines()
    binaryStringsSplit = []
    for item in binaryStrings:
        binaryStringsSplit.append([char for char in item])
    fileObj.close()
    return binaryStringsSplit

def extract(lst, n):
    return [item[n] for item in lst]

binarySplitList = readFile(file)
mostCommonBits = ''

for i in range(len(binarySplitList[0])):
    extractedList = extract(binarySplitList, i)
    modeBit = max(set(extractedList), key=extractedList.count)
    mostCommonBits += str(modeBit)


inverseMCB = ''.join(['1' if i == '0' else '0'
                     for i in mostCommonBits])

print(int(mostCommonBits,2)*int(inverseMCB,2))




