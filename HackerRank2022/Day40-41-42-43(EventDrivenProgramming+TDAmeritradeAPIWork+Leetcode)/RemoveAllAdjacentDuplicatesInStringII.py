# 1209. Remove All Adjacent Duplicates in String II
# Medium
#
# 3732
#
# 72
#
# Add to List
#
# Share
# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.
#
# We repeatedly make k duplicate removals on s until we no longer can.
#
# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.


# s = 'pbbcggttciiippooaais'
# k = 2
#
# blank = ''
# counter = 0
# for i in s:
#     counter += 1
#     if counter == len(s):
#         # print('a')
#         break
#     if i == s[counter] and len(blank) == 0:
#         print('z')
#         blank += i + s[counter]
#         print(f'blank 1 = {blank}')
#     if i == s[counter]:
#         # blank += i + s[counter]
#         print(f'i={i}')
#         print(f's of counter= {s[counter]}')
#
#         blank += i
#         print(f'blank 2 = {blank}')
#         # print('b')
#     if len(blank) == k:
#         # print(blank)
#         # print(s)
#         s = s.replace(blank, '')
#         blank = ''
#         counter = 0
#         print('c')
#         i = counter
#         # print(i)
#     # print(i)
# print(s)

# s = 'pbbcggttciiippooaais'
# k = 2
#
# blank = ''
# counter = 0
#
# for i in s:
#     # counter += 1
#     blank = i
#     print('level 1')
#     print(len(s))
#     for j in range(len(s)):
#         print('level 2')
#         print(len(s))
#         print(f'j = {j}')
#         print(f's[j] = {s[j-1]}')
#         # print(f'j = {j} s[j] = {s[j]}')
#         print(s[j-1])
#         if j+1 < len(s):
#             if s[j] == s[j+1]:
#                 print('level 3')
#                 print(s[j])
#                 blank += s[j]
#                 if len(blank) == k:
#                     print('level 4')
#                     print(blank)
#                     s = s.replace(blank,'')
#                     blank = ''
#     print(len(s))
#     print(f'LENGTH OF STRING = {len(s)}')
#     print(f'I = {i}')
# print(s)

# s = 'deeedbbcccbdaa'
# k = 2
#
# blank = ''
# counter = 0
#
# for i in s:
#     # print(i)
#     counter += 1
#     blank = i
#     print(i)
#     for j in len(s):
#         if
#         if counter < len(s):
#             if i == s[counter]:
#                 blank += s[counter]
#                 print(blank)

s = 'deeedbbcccbdaa'
k = 3
#
# blank = ''
#
# for i in s:
#     if i

stck = []

for c in s:
    print(f'c = {c}')
    if stck and stck[-1][0] == c:  # check if stack is not empty
        print(f'stack = {stck}')
        print(f'stck[-1][0] = {stck[-1][0]}')
        stck[-1][1] += 1
        if stck[-1][1] == k:
            # stckpop = stck.pop()
            stck.pop()
            # print(f'stckpop = {stckpop}')
    else:
        # stckappend = stck.append([c, 1])
        stck.append([c, 1])
        # print(f'stck.append([c, 1]) = {stck.append([c, 1])}')

print( ''.join(c * cnt for c, cnt in stck))

dog = [['a',1],['b',2],['c',3]]
#
# print(dog[0][-1])

# cat = []
#
# if cat:
#     print('True')
# else:
#     print('False')