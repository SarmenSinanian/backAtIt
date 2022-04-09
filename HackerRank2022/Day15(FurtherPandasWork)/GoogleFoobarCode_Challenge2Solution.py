# '''CONVERT CHESSBOARD INTO ARRAY'''
# '''DISTANCE BETWEEN TWO POINTS ON ARRAY'''
# '''RUN IF STATEMENTS'''

# '''RUN knight_moves AND PLACE ALL OUTCOMES INTO LIST'''
# '''EACH TIME knight_moves IS RAN, ADD TO COUNTER'''
# '''EACH TIME, CHECK IF FINAL POSITION IS WITHIN NEW LIST'''
# '''IF NOT WITHIN NEW LIST, RUN knight_moves AGAIN ON NEW LIST'''

from itertools import product
import numpy as np
def knight_moves(position1, position2):
    x, y = position1, position2
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
    return moves

print(knight_moves(1,1))

counter = 0
currentPosition = []

position1 = 19

# '''BOARD GENERATION BELOW'''
# boardArray = []
# for i in range(8):
#     boardRow = i*8
#
#     boardRowList = [x for x in range(boardRow, boardRow+7)]
#     boardArray.append(boardRowList)
#     print(boardArray)
# '''END BOARD GENERATION (ABOVE)'''

# while not currentPosition == position2: