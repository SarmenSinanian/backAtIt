from itertools import product
import numpy as np
import pandas as pd

'''BOARD DICTIONARY BELOW'''
boardDict = {}
keys = range(64)
values = [(x, y) for x in range(8) for y in range(8)]
for i in keys:
        boardDict[i] = values[i]
# print(boardDict)
'''BOARD DICTIONARY ABOVE'''

def knight_moves(row, column):
    x, y = row, column
    moves = list(product([x - 1, x + 1], [y - 2, y + 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
    # moves = [boardArray[x, y] for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
    moves = [(x, y) for x, y in moves if 0 <= x < 8 and 0 <= y < 8]

    current_possible_moves = moves
    # print(current_possible_moves)
    return moves


position1 = 0
position2 = 63
currentPosition = position1
currentPositionCartesian = boardDict[currentPosition]
position2Cartesian = boardDict[position2]

print(currentPositionCartesian)
print(position2Cartesian)

list1 = [(1, 2), (2, 1)]

lst1 = [x[0] for x in list1]
for i in list1:
    lst1.append(i[0])
    print(i)

# print(lst1)

# result = map(knight_moves, lst1, lst2)

'''PRELIMINARY SOLUTION BELOW'''
movesToCheck =knight_moves(currentPositionCartesian[0], currentPositionCartesian[1])
print(f'{movesToCheck}<---movesToCheck outside loop')

counter = 0
listOfCheckedMoves = []
while position2Cartesian not in movesToCheck:
    movesToCheck.extend(listOfCheckedMoves)
    counter += 1
    listOfCheckedMoves = []
    print(f'move#{counter}')
    for j in movesToCheck:

        # print(F'{movesToCheck}<----- movesToCheck')
        # print(f'{j}<-----j')
        newMoves = knight_moves(j[0], j[1])
        # print(f'{newMoves}<-----newMoves generated off j')
        # print('b')
        # print(f'{movesToCheck}<---movesToCheck FIRST FOR LOOP')

        for k in newMoves:
            # print(f'{k}<-----k being checked')
            if k not in movesToCheck:
                # print(f'{k}<-----k being added')
                listOfCheckedMoves.append((k))
                # print('appending')
            # print(f'{movesToCheck}<---movesToCheck SECOND FOR LOOP')
            # print(f'{listOfCheckedMoves}<---- listOfCheckedMoves')
        if position2Cartesian in listOfCheckedMoves:
            # print('done within final if statement')
            # print(f'{listOfCheckedMoves} listOfCheckedMoves in Final If Statement')
            break
        # print('END OF FOR LOOP')

'''PRELIMINARY SOLUTION ABOVE'''
#