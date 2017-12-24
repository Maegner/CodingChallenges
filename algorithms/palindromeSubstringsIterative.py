

def isPalindrome(s):
    return s == s[::-1]

def splitString(s,limits):
    leftLimit = limits[0]
    rightLimit = limits[1]
    return ((leftLimit,rightLimit-1),s[:len(s)-1]) ,((leftLimit+1,rightLimit),s[-len(s)+1:])


def countPalindromes(s):
    
    mem = []
    result = 0
    visitedSubstrings = dict()

    if isPalindrome(s):
        result += 1

    leftSplit,rightSplit = splitString(s,(0,len(s)))
    
    visitedSubstrings[(0,len(s))] = True

    mem.append(leftSplit) 
    mem.append(rightSplit)

    while(len(mem[0][1])>1):
        newM = []
        for sub in mem:
            if sub[0] in visitedSubstrings:
                continue
            else:
                if isPalindrome(sub[1]):
                    result +=1

                leftSplit,rightSplit = splitString(sub[1],sub[0])
                visitedSubstrings[sub[0]] = True
                newM.append(leftSplit)
                newM.append(rightSplit)

        mem = newM
        
    return result + len(s)