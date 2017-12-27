"""
Problem:
    Given a non-empty string s and a dictionary wordDict containing a 
    list of non-empty words, determine if s can be segmented into a 
    space-separated sequence of one or more dictionary words. 
    You may assume the dictionary does not contain duplicate words.
For example, given s = "leetcode", dict = ["leet", "code"].
Return true because "leetcode" can be segmented as "leet code". 
"""

def wordBreakAux(s,wordDict,prevSeen):
    if(s in prevSeen):
        return prevSeen[s]
    for i in range(1,len(s)+1,1):
        prefix = s[0:i]
        sufix = s[i:]
        if prefix in wordDict and wordBreakAux(sufix,wordDict,prevSeen):
            prevSeen[s]=True
            return True
    prevSeen[s] = False
    return False
    

def wordBreak(s, wordDict):
    if s == "" or wordDict == []:
        return False
    prevSeen = {}
    prevSeen[""] = True
    return wordBreakAux(s,wordDict,prevSeen)