

year = 1

# a = str(year)
# b = a[-1]
# centurymarker = len(a) - 2
# century = a[:centurymarker]
# print(century)

a = str(year)
b = a[-1]
# centurymarker = len(a) - 2
result = int(a[:centurymarker])
if int(b) == 0:
    result = int(result) - 1
print(result)