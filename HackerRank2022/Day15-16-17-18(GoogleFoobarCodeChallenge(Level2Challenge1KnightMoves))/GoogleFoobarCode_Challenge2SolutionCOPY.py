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

def knight_moves(position1, position2):
    x, y = position1, position2
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if 0 <= x < 8 and 0 <= y < 8]
    return moves

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
boardDict = {}
keys = range(64)
values = [(x, y) for x in range(8) for y in range(8)]
for i in keys:
        boardDict[i] = values[i]
# print(boardDict)
'''BOARD DICTIONARY ABOVE'''

# def boardPositionConverter(row, column):
#     boardArray

def solution(src, dest):
    boardDict = {}
    keys = range(64)
    values = [(x, y) for x in range(8) for y in range(8)]
    for i in keys:
            boardDict[i] = values[i]
    counter = 0
    listOfCheckedMoves = []
    src_cartesian = boardDict[src]
    dest_cartesian = boardDict[dest]
    moves_to_check = knight_moves(src_cartesian[0], src_cartesian[1])
    if dest_cartesian == src_cartesian:
        return 0
    if dest_cartesian in moves_to_check:
        return 1
    while dest_cartesian not in moves_to_check:
        moves_to_check.extend(listOfCheckedMoves)
        counter += 1
        listOfCheckedMoves = []
        for j in moves_to_check:
            newMoves = knight_moves(j[0], j[1])
            for k in newMoves:
                if k not in moves_to_check:
                    listOfCheckedMoves.append(k)
            if dest_cartesian in listOfCheckedMoves:
                break
    return counter

print(solution(0,63))


'''PRELIMINARY SOLUTION ABOVE'''
#


# currentPossibleMoves = [(1, 1), (1, 5), (3, 1), (3, 5), (0, 2), (0, 4), (4, 2), (4, 4)]
#
# print(currentPositionCartesian)
# print(position2Cartesian)

# print(boardDict[19])
# print(boardDict[19][0])
# print(boardDict[19][1])
# print(boardDict[28])

# currentPossibleMoves = [(1, 1), (1, 5), (3, 1), (3, 5), (0, 2), (0, 4), (4, 2), (4, 4)]


# '''attempting to map the new list of possible moves through the knight_moves function below without calling a function'''
# for i in currentPossibleMoves:
#     for x, y in i:
#         moves = list(product([x - 1, x + 1], [y - 2, y + 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
#         moves = [(x, y) for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
#         print(moves)

# result = map(knight_moves, currentPossibleMoves)
# print(list(result))


# def knight_moves(row, column):
#     x, y = row, column
#     moves = list(product([x - 1, x + 1], [y - 2, y + 2])) + list(product([x - 2, x + 2], [y - 1, y + 1]))
#     # moves = [boardArray[x, y] for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
#     moves = [(x, y) for x, y in moves if 0 <= x < 8 and 0 <= y < 8]
#
#     current_possible_moves = moves
#     # print(current_possible_moves)
#     return moves
#
#
# # while position1 not in currentPossibleMoves:
# #     print('hello')
#
# print(knight_moves(currentPositionCartesian[0], currentPositionCartesian[1]))
# print(knight_moves(2, 3))
#
#
#
# currentPossibleMovesList = knight_moves(currentPositionCartesian[0], currentPositionCartesian[1])
# print(f'{currentPossibleMovesList}<---currentpossiblemoveslist outside loop')

'''iterate over and keep adding possible moves to the list; even as the list grows, we are still looking at the'''
'''NEXT list of possible moves while increasing the moveCounter to account for the number of moves required'''
'''TENTATIVE SOLUTION BELOW ***note: add if statement to check if position 1 == position 2 at start as edge case'''
# totalPossibleMovesList = []
# for i in range(10):
#     if position2Cartesian in currentPossibleMovesList:
#         print('done at first if statement')
#         break
#     print('outer loop')
#     print(f'{currentPossibleMovesList}<---currentpossiblemoveslist inside 1st loop')
#     if position2Cartesian not in currentPossibleMovesList:
#         print('if statement')
#         moveCounter += 1
#         print(moveCounter)
#         # currentPossibleMovesListCopy = currentPossibleMovesList
#         print(f'{currentPossibleMovesList}<---currentpossiblemoveslist if statement within loop')
#         for j in currentPossibleMovesList:
#             print('inner loop')
#             print(f'{currentPossibleMovesList}<---currentpossiblemoveslist if statement within 2nd loop')
#             currentPositionCartesian = j
#             print(f'{currentPositionCartesian}<---currentPositionCartesian')
#             '''calculating current moves below'''
#             currentPossibleMoves = knight_moves(currentPositionCartesian[0], currentPositionCartesian[1])
#             print(f'{currentPossibleMoves} <--- currentPossibleMoves')
#             '''growing the list below'''
#             print(f'{len(currentPossibleMoves)}<-----len currentPossibleMoves')
#             for k in currentPossibleMoves:
#                 print(k)
#                 totalPossibleMovesList.append((k))
#                 print(f'{totalPossibleMovesList} <--- totalPossibleMovesList end of 2nd loop')
#                 if position2Cartesian in totalPossibleMovesList:
#                     print('done within final if statement')
#                     break
#             # currentPossibleMovesList = currentPossibleMovesList.extend(currentPossibleMoves)
#             # print(f'{currentPossibleMovesList} <--- currentPossibleMovesList end of 2nd loop')
#         # if position2 is in currentPossibleMoves
#         # print(currentPossibleMoves)
#         # # print(1)

'''v2 solution'''
# totalPossibleMovesList = []
# while position2Cartesian not in currentPossibleMovesList:
#     print('outer loop')
#     print(f'{currentPossibleMovesList}<---currentpossiblemoveslist inside 1st loop')
#     if position2Cartesian not in currentPossibleMovesList:
#         print('if statement')
#         moveCounter += 1
#         print(moveCounter)
#         # currentPossibleMovesListCopy = currentPossibleMovesList
#         print(f'{currentPossibleMovesList}<---currentpossiblemoveslist if statement within loop')
#         jCounter = 0
#         for j in currentPossibleMovesList:
#             jCounter += 1
#             print(f'{jCounter}<----jcounter')
#             print('inner loop')
#             print(f'{currentPossibleMovesList}<---currentpossiblemoveslist if statement within 2nd loop')
#             currentPositionCartesian = j
#             print(f'{currentPositionCartesian}<---currentPositionCartesian')
#             '''calculating current moves below'''
#             currentPossibleMoves = knight_moves(currentPositionCartesian[0], currentPositionCartesian[1])
#             print(f'{currentPossibleMoves} <--- currentPossibleMoves')
#             '''growing the list below'''
#             print(f'{len(currentPossibleMoves)}<-----len currentPossibleMoves')
#             kCounter=0
#             for k in currentPossibleMoves:
#                 print(k)
#                 kCounter +=1
#                 print(f'{kCounter}<----kCounter')
#                 totalPossibleMovesList.append((k))
#                 print(f'{totalPossibleMovesList} <--- totalPossibleMovesList end of 2nd loop')
#         if position2Cartesian in totalPossibleMovesList:
#             print('done within final if statement')
#             break

# '''OGv3. not going through rounds of moves, just iterating until it finds the position within the list'''
# position1 = 0
# position2 = 63
# currentPosition = position1
# currentPositionCartesian = boardDict[currentPosition]
# position2Cartesian = boardDict[position2]
#
# initialMoves = knight_moves(currentPositionCartesian[0], currentPositionCartesian[1])
# movesToCheck = initialMoves
#
# # while position2Cartesian not in currentPossibleMovesList:
# if position2Cartesian not in movesToCheck:
#     movesToRunKnightMovesOn = movesToCheck
#     print('abba')
#     counter = 0
#     for j in movesToRunKnightMovesOn:
#         counter+=1
#         print(f'move#{counter}')
#         newMoves = knight_moves(j[0], j[1])
#         print('b')
#         for k in newMoves:
#             movesToCheck.append((k))
#             print('appending')
#         if position2Cartesian in movesToCheck:
#             print('done within final if statement')
#             print(movesToCheck)
#             break

# letters = 'abcdefg'
#
# numbers = len(letters)
#
# for i in range(numbers-1,numbers+1):
#     print(i)


# '''EDITED #3 OF v3. not going through rounds of moves, just iterating until it finds the position within the list'''
# position1 = 0
# position2 = 63
# currentPosition = position1
# currentPositionCartesian = boardDict[currentPosition]
# position2Cartesian = boardDict[position2]
#
# initialMoves = knight_moves(currentPositionCartesian[0], currentPositionCartesian[1])
# movesToCheck = initialMoves
#
# # while position2Cartesian not in currentPossibleMovesList:
# # if position2Cartesian not in movesToCheck:
# #     print('abba')
# allMoves = []
# allMoves.append(movesToCheck)
# while position2Cartesian not in allMoves:
#     counter = 0
#     for j in movesToCheck:
#         counter+=1
#         print(f'move#{counter}')
#         print(F'{movesToCheck}<----- movesToCheck')
#         print(f'{j}<-----j')
#         newMoves = knight_moves(j[0], j[1])
#         print(f'{newMoves}<-----newMoves generated off j')
#         print('b')
#         print(f'{movesToCheck}<---movesToCheck FIRST FOR LOOP')
#         for k in newMoves:
#             print(f'{k}<-----k being checked')
#             if k not in movesToCheck:
#                 print(f'{k}<-----k being added')
#                 movesToCheck.append((k))
#                 print('appending')
#             print(f'{movesToCheck}<---movesToCheck SECOND FOR LOOP')
#         if position2Cartesian in movesToCheck:
#             print('done within final if statement')
#             print(f'{movesToCheck} movesToCheck in Final If Statement')
#             break
#     break

#

# '''EDITED #2 OF v3. not going through rounds of moves, just iterating until it finds the position within the list'''
# position1 = 0
# position2 = 63
# currentPosition = position1
# currentPositionCartesian = boardDict[currentPosition]
# position2Cartesian = boardDict[position2]
#
# initialMoves = knight_moves(currentPositionCartesian[0], currentPositionCartesian[1])
# movesToCheck = initialMoves
#
# # while position2Cartesian not in currentPossibleMovesList:
# # if position2Cartesian not in movesToCheck:
# #     print('abba')
# counter = 0
# for j in movesToCheck:
#     counter+=1
#     print(f'move#{counter}')
#     print(F'{movesToCheck}<----- movesToCheck')
#     print(f'{j}<-----j')
#     newMoves = knight_moves(j[0], j[1])
#     print(f'{newMoves}<-----newMoves generated off j')
#     print('b')
#     print(f'{movesToCheck}<---movesToCheck FIRST FOR LOOP')
#     for k in newMoves:
#         print(f'{k}<-----k being checked')
#         if k not in movesToCheck:
#             print(f'{k}<-----k being added')
#             movesToCheck.append((k))
#             print('appending')
#         print(f'{movesToCheck}<---movesToCheck SECOND FOR LOOP')
#     if position2Cartesian in movesToCheck:
#         print('done within final if statement')
#         print(f'{movesToCheck} movesToCheck in Final If Statement')
#         break
# #

# '''EDITED #1 v3. not going through rounds of moves, just iterating until it finds the position within the list'''
# position1 = 0
# position2 = 63
# currentPosition = position1
# currentPositionCartesian = boardDict[currentPosition]
# position2Cartesian = boardDict[position2]
#
# print(currentPositionCartesian, position2Cartesian)
#
# initialMoves = knight_moves(currentPositionCartesian[0], currentPositionCartesian[1])
# newBatch = initialMoves
#
# # while position2Cartesian not in currentPossibleMovesList:
# if position2Cartesian not in newBatch:
#     movesToRunKnightMovesOn = newBatch
#     print('abba')
#     counter = 0
#     print(newBatch)
#     movesToCheck = []
#     for j in movesToRunKnightMovesOn:
#         counter+=1
#         print(f'move#{counter}')
#         print(j)
#         newMoves = knight_moves(j[0], j[1])
#         print('b')
#         for k in newMoves:
#             movesToCheck.append((k))
#             print('appending')
#             print(movesToCheck)
#         if position2Cartesian in movesToCheck:
#             print('done within final if statement')
#             print(movesToCheck)
#             break
#         newBatch = movesToCheck



'''INITIAL LIST OF POSSIBLE MOVES GENERATED'''
'''INITIAL LIST OF POSSIBLE MOVES HAS EACH MOVE RAN THROUGH KNIGHT_MOVES FUNCTION TO FIND POTENTIAL NEW MOVES'''
'''ALL POTENTIAL NEW MOVES TOSSED INTO LIST'''
'''KNIGHT_MOVES FUNCTION RAN ON LIST OF NEW MOVES, REPEATING THE PROCESS'''




# df = pd.DataFrame({'column_1':['a','c'], 'column_2':['b','d']}, index=[1,2])

# ind = [(i, np.where(df[i] == 'd')[0].tolist()) for i in list(df) if len(np.where(df[i] == 'd')[0]) > 0]
# # print(ind)



# print(currentPossibleMoves)

# while not position1 == position2:

# '''get index location of board position to convert into cartesian coordinates from individual position marker'''
# '''i.e. 27 into (3,3)'''
