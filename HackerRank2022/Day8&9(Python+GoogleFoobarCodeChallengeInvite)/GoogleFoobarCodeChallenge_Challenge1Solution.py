# ''' V1 BELOW '''
# '''take n'''
# '''counter=0; while counter<6'''
# '''n+=1'''
# '''check if new n (the n+=1) isPrime'''
# '''if True, add to primeListString, n+=1. counter +=1'''
# '''if False, n+=1'''
# '''when counter =6, return first 5 digits of primeListString'''
# def nextPrimes(n):
#     counter = 0
#     primeList = []
#     while counter < 6:
#         n += 1
#         for i in range(n, n+1):
#             if isPrime(i):
#                 primeList.append(i)
#                 counter += 1
#     primeListString = ''.join(map(str, primeList))
#     print(primeListString[0:5])
#
#
# # nextPrimes(5)
#
# def primeString():
#     primeList = []
#     counter=0
#     for i in range(10006):
#         # print(i)
#         if isPrime(i):
#             primeList.append(i)
#             counter+=1
#     primeListString = ''.join(map(str, primeList))
#     print(counter)
#     return primeListString
#
# def solution(n):
#     prime = primeString()
#     print(prime[n:n+5])
#
# solution(100)


'''EARLIER VERSION WAS BOTH: RUNNING TOO LONG & NOT GETTING 10000 CHARATERS WORTH OF PRIMES
    BUT WAS INSTEAD RUNNING THROUGH 10000 *NUMBERS* IN GENERAL AND THAT WAS NOT THE RIGHT APPROACH'''
'''FINAL VERSION BELOW'''

'''FINAL VERSION AKA V2'''
def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def solution(n):
    primeString = ''
    prime = 2
    while len(primeString) < 10005:
        primeString += str(prime)
        prime += 1
        while not isPrime(prime):
            prime += 1
    print(primeString[n:n + 5])


solution(0)