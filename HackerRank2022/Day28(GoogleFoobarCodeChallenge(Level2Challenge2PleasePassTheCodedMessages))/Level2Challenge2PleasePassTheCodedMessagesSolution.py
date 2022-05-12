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