"""
Problem:
    Given a string containing just the characters '(' and ')', find 
    the length of the longest valid (well-formed) parentheses substring.
    For "(()", the longest valid parentheses substring is "()", which has length = 2.
    Another example is ")()())", where the longest valid parentheses substring is "()()",
    which has length = 4. 
"""


def largestValidParenthesis(s):
    stack = []
    i = 0
    largest = 0
    current = 0
    stack.append(-1)
    for parenthesis in s:
        if parenthesis == "(":
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
                current = 0
            else:
                
                current = max(i - stack[-1],current)
                largest = max(largest,current)
        i+=1
    return largest

print(largestValidParenthesis("())((())"))