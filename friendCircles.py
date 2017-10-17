class Solution(object):
    
    def findFriends(self,number,M,circle):
        
        if number in circle:
            return
        
        iterator = 0
        
        for element in M[number]:
            if element == 1 and iterator != number:
                self.findFriends(iterator,M,circle)
                circle[iterator] = True
            elif element == 1 and iterator == number:
                circle[iterator] = True
            iterator += 1
                
    def findCircleNum(self,M):
        
        isInCircle = dict()
        
        iterator = 0
        
        result = 0
        
        for line in M:
            
            if not iterator in isInCircle:
                
                result += 1
                
                self.findFriends(iterator,M,isInCircle)
            
            iterator += 1
            
        return result

