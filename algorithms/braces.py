"""
Problem:
    Given an array of string with braces return an array of strings
    saying for each string if it is a valid braces string or not
    e.g {}()[] is and {(}) is not
"""


def auxiliarBrace(braces):
    stack = []
    stackLen = 0
    if braces == "":
            return False
    for brace in braces:
        if brace in ["[","{","("]:
            stack.append(brace)
            stackLen += 1
        elif brace == "]":
            if stackLen == 0:
                return False
            poped = stack.pop()
            if poped != "[":
                return False
            stackLen -=1
        elif brace == ")":
            if stackLen == 0:
                return False
            poped = stack.pop()
            if poped != "(":
                return False
            stackLen -=1
        elif brace == "}":
            if stackLen == 0:
                return False
            poped = stack.pop()
            if poped != "{":
                return False
            stackLen -=1
    if stackLen == 0:
        return True
    else:
        return False

def braces(values):
    response = []
    for braces in values:
        if(auxiliarBrace(braces)):
            response.append("YES")
        else:
            response.append("NO")
    return response

print(braces(["[](){}","["]))