# Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.
#
# Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a zigzag. More formally, your task is to construct an array of length numbers.length - 2, where the ith element of the output array equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.
#
# Example
#
# For numbers = [1, 2, 1, 3, 4], the output should be solution(numbers) = [1, 1, 0].
#
# (numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1;
# (numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3;
# (numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4;
# For numbers = [1, 2, 3, 4], the output should be solution(numbers) = [0, 0];
#
# Since all the elements of numbers are increasing, there are no zigzags.
#
# For numbers = [1000000000, 1000000000, 1000000000], the output should be solution(numbers) = [0].
#
# Since all the elements of numbers are the same, there are no zigzags.

def solution(numbers):
    list1 = []
    for i in range(len(numbers)-2):
        arraynums = [numbers[i], numbers[i+1], numbers[i+2]]
        if arraynums[0] < arraynums[1] > arraynums[2] or arraynums[0] > arraynums[1] < arraynums[2]:
            list1.append(1)
        else:
            list1.append(0)
    return list1


# Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.
#
# Example
#
# For a = [25, 2, 3, 57, 38, 41], the output should be solution(a) = [2, 3, 5].
#
# Here are the number of times each digit appears in the array:
#
# 0 -> 0
# 1 -> 1
# 2 -> 2
# 3 -> 2
# 4 -> 1
# 5 -> 2
# 6 -> 0
# 7 -> 1
# 8 -> 1
# The most number of times any number occurs in the array is 2, and the digits which appear 2 times are 2, 3 and 5. So the answer is [2, 3, 5].

def solution(a):
    slots = []
    slotssum = [0] * 10
    result = []
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in a:
        for j in str(i):
            slots.append(int(j))
    for k in slots:
        slotssum[k] += 1
    a = max(slotssum)
    for count, m in enumerate(slotssum):
        if m == a:
            result.append(count)
    return result


