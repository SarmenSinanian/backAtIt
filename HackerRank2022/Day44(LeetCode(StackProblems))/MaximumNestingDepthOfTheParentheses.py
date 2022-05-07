# A string is a valid parentheses string (denoted VPS) if it meets one of the following:
#
# It is an empty string "", or a single character not equal to "(" or ")",
# It can be written as AB (A concatenated with B), where A and B are VPS's, or
# It can be written as (A), where A is a VPS.
# We can similarly define the nesting depth depth(S) of any VPS S as follows:
#
# depth("") = 0
# depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
# depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
# depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
# For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.
#
# Given a VPS represented as string s, return the nesting depth of s.

s = "(1+(2*3)+((8)/4))+1"

maxLength = 0
currentLength = 0
stack = []

for i in s:
    # print(f'level 1 = {stack}')
    # if (i == '(') or (i == ')'):
        # print('hello')
        # print(f'level 2 = {stack}')
        if i == '(':
            # print(f'stack appending "{i}"')
            stack.append(i)
            # print(f'stack = {stack}')
            currentLength +=1
            if maxLength < currentLength:
                maxLength = currentLength
        if i == ')':
            # print(f'stack popping {stack}')
            stack.pop()
            currentLength -= 1

print(maxLength)

'''keep adding to stack for '(' and removing from stack when ')' '''

