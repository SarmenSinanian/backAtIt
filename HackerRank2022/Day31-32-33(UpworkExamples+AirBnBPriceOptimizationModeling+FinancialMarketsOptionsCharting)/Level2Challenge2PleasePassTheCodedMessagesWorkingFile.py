import itertools

def solution(l):
    biggest = 0
    for length in range(1, len(l) + 1):
        for subset in itertools.permutations(l, length):
            numstrings = []
            for i in subset:
                numstrings.append(str(i))
            longstring = ["".join(numstrings)]
            for j in longstring:
                item = int(j)
                if item % 3 == 0:
                    if item > biggest:
                        biggest = item
    return biggest

'''original solution found in 2-3 hours max below'''
# biggest = 0
# nums = [3, 1, 4, 1, 5, 9]
# for L in range(1, len(nums)+1):
#     for subset in itertools.permutations(nums, L):
#         # print(subset)
#         # '''combine as string then turn to int'''
#         # list1 = ["".join(str(x)) for x in subset]
#         # print(list1)
#         list1 = []
#         for i in subset:
#             list1.append(str(i))
#             # print(i)
#         # print(list1)
#         list2 = ["".join(list1)]
#         # print(list2)
#         for j in list2:
#             print(int(j))
#             item = int(j)
#             if item % 3 == 0:
#                 print('FOUND ONE')
#                 contender = item
#                 if contender > biggest:
#                     biggest = contender
#     # print(biggest)

'''original solution found in 2-3 hours max above'''

# l = [3, 1, 4, 1, 5, 9]
#
# biggest = 0
# for length in range(1, len(l) + 1):
#     for subset in itertools.permutations(l, length):
#         numstrings = []
#         for i in subset:
#             numstrings.append(str(i))
#         longstring = ["".join(numstrings)]
#         for j in longstring:
#             item = int(j)
#             if item % 3 == 0:
#                 if item > biggest:
#                     biggest = item
#
#     print(biggest)
#

