# '''CONVERT CHESSBOARD INTO ARRAY'''
# '''DISTANCE BETWEEN TWO POINTS ON ARRAY'''
# '''RUN IF STATEMENTS'''

# '''RUN knight_moves AND PLACE ALL OUTCOMES INTO LIST'''
# '''EACH TIME knight_moves IS RAN, ADD TO COUNTER'''
# '''EACH TIME, CHECK IF FINAL POSITION IS WITHIN NEW LIST'''
# '''IF NOT WITHIN NEW LIST, RUN knight_moves AGAIN ON NEW LIST'''

from itertools import product
import numpy as np
import pandas as pd

# def knight_moves(position1, position2):
#     x, y = position1, position2
#     moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
#     moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
#     return moves

'''BOARD ARRAY GENERATION BELOW'''
board = []
for i in range(8):
    boardRow = i * 8

    boardRowList = [x for x in range(boardRow, boardRow + 7)]
    board.append(boardRowList)
boardArray = np.array(board)
# print(boardArray[3, 3])
'''BOARD ARRAY GENERATION ABOVE'''

'''BOARD DICTIONARY BELOW'''
dicts = {}
keys = range(64)
values = [(x, y) for x in range(8) for y in range(8)]
for i in keys:
        dicts[i] = values[i]
# print(dicts)
'''BOARD DICTIONARY ABOVE'''

# def boardPositionConverter(row, column):
#     boardArray


moveCounter = 0
position1 = 19
position2 = 28
currentPosition = position1
currentPositionCartesian = dicts[currentPosition]
position2Cartesian = dicts[position2]
# currentPossibleMoves = [(1, 1), (1, 5), (3, 1), (3, 5), (0, 2), (0, 4), (4, 2), (4, 4)]

print(currentPositionCartesian)
print(position2Cartesian)

# print(dicts[19])
# print(dicts[19][0])
# print(dicts[19][1])
# print(dicts[28])

currentPossibleMoves = [(1, 1), (1, 5), (3, 1), (3, 5), (0, 2), (0, 4), (4, 2), (4, 4)]


'''attempting to map the new list of possible moves through the knight_moves function below without calling a function'''
for i in currentPossibleMoves:
    for x, y in i:
        moves = list(product([x - 1, x + 1], [y - 2, y + 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
        moves = [(x, y) for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
        print(moves)

# result = map(knight_moves, currentPossibleMoves)
# print(list(result))


def knight_moves(row, column):
    x, y = row, column
    moves = list(product([x - 1, x + 1], [y - 2, y + 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
    # moves = [boardArray[x, y] for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
    moves = [(x, y) for x, y in moves if 0 <= x < 8 and 0 <= y < 8]

    current_possible_moves = moves
    # print(current_possible_moves)
    return moves


# while position1 not in currentPossibleMoves:
#     print('hello')

print(knight_moves(dicts[19][0], dicts[19][1]))
print(knight_moves(2, 3))

'''iterate over and keep adding possible moves to the list; even as the list grows, we are still looking at the'''
'''NEXT list of possible moves while increasing the moveCounter to account for the number of moves required'''

for i in range(6):
    if currentPosition != position2:
        moveCounter += 1
        currentPossibleMoves = knight_moves(dicts[currentPosition][0], dicts[currentPosition][1])
        currentPossibleMoves = currentPossibleMoves
        print(currentPossibleMoves)
        # if position2 is in currentPossibleMoves
        # print(currentPossibleMoves)
        # # print(1)

    if currentPosition == position2:
        print('done')





# df = pd.DataFrame({'column_1':['a','c'], 'column_2':['b','d']}, index=[1,2])

# ind = [(i, np.where(df[i] == 'd')[0].tolist()) for i in list(df) if len(np.where(df[i] == 'd')[0]) > 0]
# # print(ind)



# print(currentPossibleMoves)

# while not position1 == position2:

# '''get index location of board position to convert into cartesian coordinates from individual position marker'''
# '''i.e. 27 into (3,3)'''
