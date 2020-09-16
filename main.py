from random import randint


def setBoard(h, w):
    gameBoard = []

    for x in range(0, w):
        gameBoard.append(['~'])
        for y in range(1, h):
            gameBoard[x].append('~')
    return gameBoard


gameBoard = setBoard(10, 10)


def printBoard():
    for x in range(len(gameBoard)):
        print(' '.join(gameBoard[x]))


randomRow = randint(0, len(gameBoard) - 1)
randomCol = randint(0, len(gameBoard) - 1)
gameBoard[randomRow][randomCol] = '@'

printBoard()

for guesses in range(1, 4):
    print('Guess the location of the Ship (row, col)')
    row, col = input().split(",")

    print(row, col)

    if int(row) - 1 == randomRow and int(col) - 1 == randomCol:
        print('You guessed correctly!')
        gameBoard[int(row) - 1][int(col) - 1] = '#'
        printBoard()
        break
    else:
        print('Splash. You missed. Guess again')
        gameBoard[int(row) - 1][int(col) - 1] = 'X'

    printBoard()

