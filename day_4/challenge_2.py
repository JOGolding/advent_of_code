def newBoard(x):
    n = x
    m = x
    a = [None] * n
    for i in range(n):
        a[i] = [None] * m
    return a


def getNums(file):
    with open(file, 'r+') as f:
        for line in f:
            return [int(nums) for nums in line.split(',')]


def getBoards(file):
    boards = []
    grid = []
    with open(file, 'r+') as f:
        for line in f:
            if line == '\n':
                boards.append(grid)
                grid = []
            else:
                grid.append([int(x) for x in line.split()])
        return boards


def extract(lst, n):
    return [item[n] for item in lst]


def Bingo(nums, boards, gridSize):

    currentHighest = 0
    mostPasses = 0

    for board in boards:
        emptyBoard = newBoard(gridSize)
        duplicateBoard = board
        bingo = False
        passes = 0
        totalUnmarked = 0
        for num in nums:
            for row in board:
                for pos in row:
                    rowIndex = board.index(row)
                    posIndex = row.index(pos)
                    if pos == num:
                        emptyBoard[rowIndex][posIndex] = num
                        duplicateBoard[rowIndex][posIndex] = None

                        for index, emptyRow in enumerate(emptyBoard):
                            columns = extract(emptyBoard, index)
                            if (all(emptyRow) or all(columns)) and bingo == False :
                                bingo = True
                                for duplicateRow in duplicateBoard:
                                    for duplicateItem in duplicateRow:
                                        if isinstance(duplicateItem, int):
                                            totalUnmarked += duplicateItem
                                if mostPasses == 0:
                                    currentHighest = totalUnmarked*num
                                    mostPasses = passes
                                elif passes > mostPasses:
                                    currentHighest = totalUnmarked*num
                                    mostPasses = passes
            passes += 1
        
    return currentHighest


testNums = getNums('day_4/testbingo.txt')
testBoards = getBoards('day_4/test_input.txt')

nums = getNums('day_4/bingo.txt')
boards = getBoards('day_4/input.txt')

print(Bingo(nums, boards, 5))
print(Bingo(testNums, testBoards, 3))