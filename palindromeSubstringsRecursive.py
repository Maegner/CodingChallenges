def isPalindrome(s):
    return s == s[::-1]

def palindromeInSubstring(s,memory,startIndex,endIndex):
    
    haskey = str(startIndex)+str(endIndex)

    if haskey in memory:
        return 0
    
    lenghtS = len(s)
    
    if lenghtS >1:
        memory[haskey] = isPalindrome(s)
        
        if memory[haskey]:
            return 1 + palindromeInSubstring(s[:len(s)-1],memory,startIndex,endIndex-1) + palindromeInSubstring(s[-len(s)+1:],memory,startIndex+1,endIndex)
        else:
            return 0 + palindromeInSubstring(s[:len(s)-1],memory,startIndex,endIndex-1) + palindromeInSubstring(s[-len(s)+1:],memory,startIndex+1,endIndex)
    else:
        return 0

def countPalindromes(s):
    memory = dict()
    
    lenghtS = len(s)

    return lenghtS + palindromeInSubstring(s,memory,0,lenghtS-1)
    