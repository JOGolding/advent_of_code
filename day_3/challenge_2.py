file='day_3/input.txt'
testFile='day_3/test_input.txt'

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

def countBits(lst):
    zeroCount = lst.count('0')
    oneCount = lst.count('1')

    if zeroCount == oneCount:
        return '1'
    elif zeroCount < oneCount:
        return '1'
    else:
        return '0'


binarySplitList = readFile(file)
binarySplitList2 = readFile(file)

for i in range(len(binarySplitList[0])):
    extractedList = extract(binarySplitList, i)
    modeBit = countBits(extractedList)
    binarySplitList = list(filter(lambda x: x[i] == modeBit, binarySplitList))

x =(int("".join(binarySplitList[0]),2))

for i in range(len(binarySplitList2[0])):
    extractedList = extract(binarySplitList2, i)
    modeBit = countBits(extractedList)
    if len(binarySplitList2) == 1:
        y = (int("".join(binarySplitList2[0]),2))
    binarySplitList2 = list(filter(lambda x: x[i] != modeBit, binarySplitList2))

print(x*y)
        
        



    