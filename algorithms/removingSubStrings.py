# Complete the function below.


# Complete the function below.


def removeFirst(s,t):
    
    if len(s) < len(t) or t not in s:
        return False,s
    
    lastIndexOftFound = 0
    iterator = 0
    
    firstFound = 0
    lastFound = 0

    for letter in s:
        
        if letter == t[lastIndexOftFound]:
            if lastIndexOftFound  == 0:
                firstFound = iterator
            if lastIndexOftFound == len(t)-1:
                return True, s[:firstFound] + s[iterator+1:] 
            lastIndexOftFound += 1
        else:
            if letter == t[0]:
                lastIndexOftFound = 1
                firstFound = iterator
            else:
                if letter not in t:
                    s = s[iterator+1:]
                    iterator = -1
                lastIndexOftFound = 0
        iterator += 1
    return False, s

def removeLast(s,t):
    
    if len(s) < len(t) or t not in s:
        return False,s
    
    nextIndexOftFound = -1
    lastPosition = len(s) -1 
    iterator = lastPosition
    firstFound = 0
    
    for index in range (lastPosition,-1,-1):
        if s[index] == t[nextIndexOftFound]:
            if nextIndexOftFound == -1:
                firstFound = iterator
            if nextIndexOftFound == -len(t):
                return True, s[:iterator] + s[firstFound +1:]
            nextIndexOftFound -=1
        else:
            if s[index] == t[-1]:
                nextIndexOftFound = -2
                firstFound = iterator
            else:
                if s[index] not in t:
                    s = s[:iterator]
                    iterator = 0
                nextIndexOftFound = -1
        iterator -= 1
    return False, s

def move(s,t,side,RemoveFirstMemory,RemoveLastMemory):
    if side == "last":
        
        if s in RemoveLastMemory:
            return RemoveLastMemory[s]
        
        removed,result = removeLast(s,t)
        if removed:
            RemoveLastMemory[s] = 1 + move(result,t,"last",RemoveFirstMemory,RemoveLastMemory)
            return RemoveLastMemory[s]
        else:
            return 0
    
    if side == "first":
        
        if s in RemoveFirstMemory:
            return RemoveFirstMemory[s]
        
        removed,result = removeFirst(s,t)
        
        if removed:
            RemoveFirstMemory[s] =  1 + move(result,t,"first",RemoveFirstMemory,RemoveLastMemory)        
        else:
            RemoveFirstMemory[s] = 0
        return RemoveFirstMemory[s]

def maxMoves(s, t):
    
    RemoveFirstMemory = dict()
    RemoveLastMemory = dict()
    
    return max(move(s,t,"first",RemoveFirstMemory,RemoveLastMemory),move(s,t,"last",RemoveFirstMemory,RemoveLastMemory))

def removeLast(s,t):
    
    if len(s) < len(t) or t not in s:
        return False,s
    
    nextIndexOftFound = -1
    lastPosition = len(s) -1 
    iterator = lastPosition
    firstFound = 0
    
    for index in range (lastPosition,-1,-1):
        if s[index] == t[nextIndexOftFound]:
            if nextIndexOftFound == -1:
                firstFound = iterator
            if nextIndexOftFound == -len(t):
                return True, s[:iterator] + s[firstFound +1:]
            nextIndexOftFound -=1
        else:
            if s[index] == t[-1]:
                nextIndexOftFound = -2
                firstFound = iterator
            else:
                if s[index] not in t:
                    s = s[:iterator]
                    iterator = 0
                nextIndexOftFound = -1
        iterator -= 1
    return False, s

def move(s,t,side,RemoveFirstMemory,RemoveLastMemory):
    if side == "last":
        
        if s in RemoveLastMemory:
            return RemoveLastMemory[s]
        
        removed,result = removeLast(s,t)
        if removed:
            RemoveLastMemory[s] = 1 + max(move(result,t,"last",RemoveFirstMemory,RemoveLastMemory),move(result,t,"first",RemoveFirstMemory,RemoveLastMemory))
            return RemoveLastMemory[s]
        else:
            return 0
    
    if side == "first":
        
        if s in RemoveFirstMemory:
            return RemoveFirstMemory[s]
        
        removed,result = removeFirst(s,t)
        
        if removed:
            RemoveFirstMemory[s] =  1 + max((move(result,t,"last",RemoveFirstMemory,RemoveLastMemory),move(result,t,"first",RemoveFirstMemory,RemoveLastMemory)))
        
        else:
            RemoveFirstMemory[s] = 0
        return RemoveFirstMemory[s]

def maxMoves(s, t):
    
    RemoveFirstMemory = dict()
    RemoveLastMemory = dict()
    
    return max((move(s,t,"last",RemoveFirstMemory,RemoveLastMemory),move(s,t,"first",RemoveFirstMemory,RemoveLastMemory)))