'''CONVERT CHESSBOARD INTO ARRAY'''
'''DISTANCE BETWEEN TWO POINTS ON ARRAY'''
'''RUN IF STATEMENTS'''

from itertools import product
def knight_moves(position1, position2):
    x, y = position1, position2
    moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
    moves = [(x,y) for x,y in moves if x >= 0 and y >= 0 and x < 8 and y < 8]
    return moves

print(knight_moves(4,4))