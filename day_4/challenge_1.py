def newBoard():
    n = 5
    m = 5
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


testNums = getNums('day_4/testbingo.txt')
testBoards = getBoards('day_4/test_input.txt')

nums = getNums('day_4/bingo.txt')
boards = getBoards('day_4/input.txt')


def Bingo(nums, boards):

    currentHighest = 0
    leastPasses = 0

    for board in boards:
        emptyBoard = newBoard()
        duplicateBoard = board
        boardComplete = False
        passes = 0
        totalUnmarked = 0
        for num in nums:
            passes += 1
            for row in board:
                for pos in row:
                    rowIndex = board.index(row)
                    posIndex = row.index(pos)
                    if pos == num:
                        emptyBoard[rowIndex][posIndex] = num
                        duplicateBoard[rowIndex][posIndex] = None

                        for index, emptyRow in enumerate(emptyBoard):
                            columns = extract(emptyBoard, index)
                            if all(emptyRow) or all(columns):
                                for duplicateRow in duplicateBoard:
                                    for duplicateItem in duplicateRow:
                                        if isinstance(duplicateItem, int):
                                            totalUnmarked += duplicateItem
                                if boardComplete == True:
                                    break
                                elif leastPasses == 0:
                                    currentHighest = totalUnmarked*num
                                    print(currentHighest)
                                    leastPasses = passes
                                    boardComplete = True
                                elif passes < leastPasses:
                                    currentHighest = totalUnmarked*num
                                    print(currentHighest)
                                    leastPasses = passes
                                    boardComplete = True
    return currentHighest

print(Bingo(nums, boards))
#print(Bingo(testNums, testBoards))