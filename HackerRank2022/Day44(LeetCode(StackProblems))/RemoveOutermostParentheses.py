# A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.
#
# For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
# A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.
#
# Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.
#
# Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

# Input: s = "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

s = "(()())(())(()(()))"

stack = []
sectionCounter = 0
totalCounter = 0
list1 = []
previousLen = 0
finals = []
result = ''

for i in s:
    totalCounter += 1
    if stack:
        if i == '(' and stack[-1] == '(':
            stack.append(i)
            sectionCounter += 1
            print(f'level 1 stack = {stack}')
            print(list1)
        if i == ')' and stack[-1] == '(':
            list1.append(stack.pop())
            list1.append(i)
            sectionCounter += 1
            print(f'level 2 stack = {stack}')
            if not stack:
                # print(s[totalCounter-sectionCounter:totalCounter])
                print(s[previousLen:sectionCounter])
                b = s[previousLen:sectionCounter]
                finals.append(b[1:-1])
                previousLen = len(s[0:sectionCounter])

    else:
        print(f'stack appending {i} onto {stack}')
        stack.append(i)
        sectionCounter += 1

print(''.join(finals))

# return ''.join(save2)

# print(result)