#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


#Realized only sum need be computer and flipping of rows around was not necessary,
# contrary to what the description of the test asked...
matrix = [[4089, 1714, 459, 3709, 2113, 773],
          [969, 2435, 2197, 1766, 852, 1278],
          [2235, 1228, 429, 1771, 1832, 3673],
          [2728, 2050, 1747, 3488, 2439, 4086],
          [3451, 3472, 1816, 2635, 1365, 4091],
          [2772, 2673, 3237, 2672, 1182, 2357]]

def flippingMatrix(matrix):
    for i in len(matrix):
        
    l1 = [matrix[0][0], matrix[0][3], matrix[3][0], matrix[3][3]]
    l2 = [matrix[0][1], matrix[0][2], matrix[3][1], matrix[3][2]]
    l3 = [matrix[1][0], matrix[1][3], matrix[2][0], matrix[2][3]]
    l4 = [matrix[1][1], matrix[1][2], matrix[2][1], matrix[2][2]]
    return max(l1) + max(l2) + max(l3) + max(l4)

'''MEASURE HIGHEST IN EACH CORNER, EACH EDGE MIDROW/COLUMN, EACH SIDE, EACH CENTER'''

# #flip row if following true
# matrix[0][0] < matrix[0][3]
# #flip column if following true
# matrix[0][0] < matrix[3][0]
# #flip row and column if following true
# matrix[0][0] < matrix[3][3]
#
# #flip row if following true
# matrix[0][1] < matrix[0][2]
# #flip column if following true
# matrix[0][1] < matrix[3][1]
# #flip row and column if following true
# matrix[0][1] < matrix[3][2]
#
# #flip row if following true
# matrix[1][0] < matrix[1][3]
# #flip columm if following true
# matrix[1][0] <  matrix[2][0]
# #flip row and column if following true
# matrix[1][0] < matrix[2][3]
#
# #flip row if following true
# matrix[1][1] < matrix[1][2]
# #flip column if following true
# matrix[1][1] < matrix[2][1]
# #flip row and column if following true
# matrix[1][1] < matrix[2][2]

# matrix = [[112,42,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]
# matrix = [[107,54,128,15],[12,75,110,138],[100,96,34,85],[75,15,28,112]]




#V3
# def flippingMatrix(matrix):
#     for x in range(5):
#         #[0][0] ADJUSTMENT
#         for i in range(1):
#             if matrix[0][0] < matrix[0][3]:
#                 temp = [matrix[0][3], matrix[0][2], matrix[0][1], matrix[0][0]]
#                 matrix[0] = temp
#                 print('flip row 0')
#             if matrix[0][0] < matrix[3][0]:
#                 temp = [matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]]
#                 matrix[0][0] = temp[0]
#                 matrix[1][0] = temp[1]
#                 matrix[2][0] = temp[2]
#                 matrix[3][0] = temp[3]
#                 print('flip column 0')
#
#         #[0][1] ADJUSTMENT
#         for i in range(1):
#             if matrix[0][1] < matrix[0][2]:
#                 temp = [matrix[0][3], matrix[0][2], matrix[0][1], matrix[0][0]]
#                 matrix[0] = temp
#                 print('flip row 0')
#             if matrix[0][1] < matrix[3][1]:
#                 temp = [matrix[3][1], matrix[2][1], matrix[1][1], matrix[0][1]]
#                 matrix[0][1] = temp[0]
#                 matrix[1][1] = temp[1]
#                 matrix[2][1] = temp[2]
#                 matrix[3][1] = temp[3]
#                 print('flip column 1')
#
#
#         #[1][0] ADJUSTMENT
#         for i in range(1):
#             if matrix[1][0] < matrix[1][3]:
#                 temp = [matrix[1][3], matrix[1][2], matrix[1][1], matrix[1][0]]
#                 matrix[1] = temp
#                 print('flip row 1')
#             if matrix[1][0] < matrix[2][0]:
#                 temp = [matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]]
#                 matrix[0][0] = temp[0]
#                 matrix[1][0] = temp[1]
#                 matrix[2][0] = temp[2]
#                 matrix[3][0] = temp[3]
#                 print('flip column 0')
#
#         #[1][1] ADJUSTMENT
#         for i in range(1):
#
#             if matrix[1][1] < matrix[1][2]:
#                 temp = [matrix[1][3], matrix[1][2], matrix[1][1], matrix[1][0]]
#                 matrix[1] = temp
#                 print('flip row 1')
#             if matrix[1][1] < matrix[2][1]:
#                 temp = [matrix[3][1], matrix[2][1], matrix[1][1], matrix[0][1]]
#                 matrix[0][1] = temp[0]
#                 matrix[1][1] = temp[1]
#                 matrix[2][1] = temp[2]
#                 matrix[3][1] = temp[3]
#                 print('flip column 1')
#
#
#         for i in range(2):
#             if matrix[0][0] < matrix[3][3]:
#                 temp = [matrix[3][3], matrix[3][2], matrix[3][1], matrix[3][0]]
#                 matrix[3] = temp
#                 temp = [matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]]
#                 matrix[0][0] = temp[0]
#                 matrix[1][0] = temp[1]
#                 matrix[2][0] = temp[2]
#                 matrix[3][0] = temp[3]
#             if matrix[0][1] < matrix[3][2]:
#                 temp = [matrix[3][3], matrix[3][2], matrix[3][1], matrix[3][0]]
#                 matrix[3] = temp
#                 temp = [matrix[3][1], matrix[2][1], matrix[1][1], matrix[0][1]]
#                 matrix[0][1] = temp[0]
#                 matrix[1][1] = temp[1]
#                 matrix[2][1] = temp[2]
#                 matrix[3][1] = temp[3]
#             if matrix[1][0] < matrix[2][3]:
#                 temp = [matrix[2][3], matrix[2][2], matrix[2][1], matrix[2][0]]
#                 matrix[2] = temp
#                 temp = [matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]]
#                 matrix[0][0] = temp[0]
#                 matrix[1][0] = temp[1]
#                 matrix[2][0] = temp[2]
#                 matrix[3][0] = temp[3]
#             if matrix[1][1] < matrix[2][2]:
#                 temp = [matrix[2][3], matrix[2][2], matrix[2][1], matrix[2][0]]
#                 matrix[2] = temp
#                 temp = [matrix[3][1], matrix[2][1], matrix[1][1], matrix[0][1]]
#                 matrix[0][1] = temp[0]
#                 matrix[1][1] = temp[1]
#                 matrix[2][1] = temp[2]
#                 matrix[3][1] = temp[3]
#
#             print(f'FINAL MATRIX:')
#             print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
#             print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
#             print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3])
#             print(matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3])
#         a = matrix[0][0] + matrix[0][1] + matrix[1][0] + matrix[1][1]
#         # a = matrix[0][0] + matrix[0][1] + matrix[1][0] + matrix[1][1]
#     return a


#V2
# def flippingMatrix(matrix):
#     for x in range(5):
#         #[0][0] ADJUSTMENT
#         for i in range(1):
#             if matrix[0][0] < matrix[0][3]:
#                 temp = [matrix[0][3], matrix[0][2], matrix[0][1], matrix[0][0]]
#                 matrix[0] = temp
#             if matrix[0][0] < matrix[3][0]:
#                 temp = [matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]]
#                 matrix[0][0] = temp[0]
#                 matrix[1][0] = temp[1]
#                 matrix[2][0] = temp[2]
#                 matrix[3][0] = temp[3]
#             if matrix[0][0] < matrix[3][3]:
#                 temp = [matrix[3][3], matrix[3][2], matrix[3][1], matrix[3][0]]
#                 matrix[3] = temp
#                 temp = [matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]]
#                 matrix[0][0] = temp[0]
#                 matrix[1][0] = temp[1]
#                 matrix[2][0] = temp[2]
#                 matrix[3][0] = temp[3]
#         #[0][1] ADJUSTMENT
#         for i in range(1):
#             if matrix[0][1] < matrix[3][1]:
#                 temp = [matrix[3][1], matrix[2][1], matrix[1][1], matrix[0][1]]
#                 matrix[0][1] = temp[0]
#                 matrix[1][1] = temp[1]
#                 matrix[2][1] = temp[2]
#                 matrix[3][1] = temp[3]
#             if matrix[0][1] < matrix[3][2]:
#                 temp = [matrix[3][3], matrix[3][2], matrix[3][1], matrix[3][0]]
#                 matrix[3] = temp
#                 temp = [matrix[3][1], matrix[2][1], matrix[1][1], matrix[0][1]]
#                 matrix[0][1] = temp[0]
#                 matrix[1][1] = temp[1]
#                 matrix[2][1] = temp[2]
#                 matrix[3][1] = temp[3]
#             if matrix[0][1] < matrix[0][2]:
#                 temp = [matrix[0][3], matrix[0][2], matrix[0][1], matrix[0][0]]
#                 matrix[0] = temp
#         #[1][0] ADJUSTMENT
#         for i in range(1):
#             if matrix[1][0] < matrix[1][3]:
#                 temp = [matrix[1][3], matrix[1][2], matrix[1][1], matrix[1][0]]
#                 matrix[1] = temp
#             if matrix[1][0] < matrix[2][0]:
#                 temp = [matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]]
#                 matrix[0][0] = temp[0]
#                 matrix[1][0] = temp[1]
#                 matrix[2][0] = temp[2]
#                 matrix[3][0] = temp[3]
#             if matrix[1][0] < matrix[2][3]:
#                 temp = [matrix[2][3], matrix[2][2], matrix[2][1], matrix[2][0]]
#                 matrix[2] = temp
#                 temp = [matrix[3][0], matrix[2][0], matrix[1][0], matrix[0][0]]
#                 matrix[0][0] = temp[0]
#                 matrix[1][0] = temp[1]
#                 matrix[2][0] = temp[2]
#                 matrix[3][0] = temp[3]
#         #[1][1] ADJUSTMENT
#         for i in range(1):
#             if matrix[1][1] < matrix[2][1]:
#                 temp = [matrix[3][1], matrix[2][1], matrix[1][1], matrix[0][1]]
#                 matrix[0][1] = temp[0]
#                 matrix[1][1] = temp[1]
#                 matrix[2][1] = temp[2]
#                 matrix[3][1] = temp[3]
#             if matrix[1][1] < matrix[2][2]:
#                 temp = [matrix[2][3], matrix[2][2], matrix[2][1], matrix[2][0]]
#                 matrix[2] = temp
#                 temp = [matrix[3][1], matrix[2][1], matrix[1][1], matrix[0][1]]
#                 matrix[0][1] = temp[0]
#                 matrix[1][1] = temp[1]
#                 matrix[2][1] = temp[2]
#                 matrix[3][1] = temp[3]
#             if matrix[1][1] < matrix[1][2]:
#                 temp = [matrix[1][3], matrix[1][2], matrix[1][1], matrix[1][0]]
#                 matrix[1] = temp
#         print(f'FINAL MATRIX:')
#         print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
#         print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
#         print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3])
#         print(matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3])
#         a = matrix[0][0] + matrix[0][1] + matrix[1][0] + matrix[1][1]
#         a = matrix[0][0] + matrix[0][1] + matrix[1][0] + matrix[1][1]
#     return a

#V1
# def flippingMatrix(matrix):
#     for x in range(5):
#         for i in range(len(matrix)):
#             print('\n')
#             print('MATRIX BELOW')
#             print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
#             print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
#             print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3])
#             print(matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3])
#             print('MATRIX ABOVE')
#             print('\n')
#             for i in range(len(matrix)):
#                 if (matrix[i][0] + matrix[i][1]) < (matrix[i][2] + matrix[i][3]):
#                     print(f'flipped row {i}: {matrix[i][0]}, {matrix[i][1]}, {matrix[i][2]},'
#                           f' {matrix[i][3]}')
#                     temp = [matrix[i][3], matrix[i][2], matrix[i][1], matrix[i][0]]
#                     matrix[i] = temp
#                 else:
#                     print(f'SKIPPED ROW {i}')
#                 if (matrix[0][i] + matrix[1][i] < (matrix[2][i] + matrix[3][i])):
#                     print(f'flipped column {i}: {matrix[0][i]}, {matrix[1][i]}, {matrix[2][i]},'
#                           f' {matrix[3][i]}')
#                     temp = [matrix[3][i], matrix[2][i], matrix[1][i], matrix[0][i]]
#                     matrix[0][i] = temp[0]
#                     matrix[1][i] = temp[1]
#                     matrix[2][i] = temp[2]
#                     matrix[3][i] = temp[3]
#                 else:
#                     print(f'SKIPPED COLUMN {i}')
#             print('\n')
#             print(f'FINAL MATRIX:')
#             print(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3])
#             print(matrix[1][0], matrix[1][1], matrix[1][2], matrix[1][3])
#             print(matrix[2][0], matrix[2][1], matrix[2][2], matrix[2][3])
#             print(matrix[3][0], matrix[3][1], matrix[3][2], matrix[3][3])
#             a = matrix[0][0] + matrix[0][1] + matrix[1][0] + matrix[1][1]
#             print(f'PRELIMINARY SUM {a}')
#     print('Finished')
#     return a

print(flippingMatrix(matrix))


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     q = int(input().strip())
#
#     for q_itr in range(q):
#         n = int(input().strip())
#
#         matrix = []
#
#         for _ in range(2 * n):
#             matrix.append(list(map(int, input().rstrip().split())))
#
#         result = flippingMatrix(matrix)
#
#         fptr.write(str(result) + '\n')
#
#     fptr.close()
