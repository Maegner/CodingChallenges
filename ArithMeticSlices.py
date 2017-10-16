class Solution(object):
    
    def findSubGroupNumber(self,number):
        result = 0
        iterator = 1
        for n in range (number,2,-1):
            result += iterator
            iterator += 1
        return result
    
    def numberOfArithmeticSlices(self, A):
        
        if len(A) < 3:
            return 0
        
        lastInSequence = 0
        currentSeparation = 0
        result = 0
        currentInSequence = 0
        first = True
        
        for element in A:
            
            if first:
                lastInSequence = A[0]
                currentInSequence+=1
                currentSeparation = A[1] - A[0]
                first = False
                continue
            else:
                if element - lastInSequence == currentSeparation:
                    lastInSequence = element
                    currentInSequence += 1
                
                else:
                    if currentInSequence == 3:
                        result += 1
                    elif currentInSequence > 3:
                        result += self.findSubGroupNumber(currentInSequence)
                    currentInSequence = 2
                    currentSeparation =  element - lastInSequence
                    lastInSequence = element
        if currentInSequence == 3:
            result += 1
        elif currentInSequence > 3:
            result += self.findSubGroupNumber(currentInSequence)
        return result
