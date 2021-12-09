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

def function(lst, x):
    for i in range(len(lst[0])):
        extractedList = extract(lst, i)
        modeBit = countBits(extractedList)
        if x == 'most':
            lst = list(filter(lambda x: x[i] == modeBit, lst))
        else:
            lst = list(filter(lambda x: x[i] != modeBit, lst))

        if len(lst) == 1:
            return (int("".join(lst[0]),2))

print(function(binarySplitList,'most')*function(binarySplitList,''))
        
        



    