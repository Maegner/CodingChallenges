class Solution(object):
    
    def calCulateSteps(self,stepOn,n,memoTable):
        
        if stepOn > n:
            return 0
        elif stepOn == n:
            return 1
        elif stepOn in memoTable:
            return memoTable[stepOn][0] + memoTable[stepOn][1]
        
        else:
            memoTable[stepOn] = (self.calCulateSteps(stepOn+1,n,memoTable),self.calCulateSteps(stepOn+2,n,memoTable))
            
        return memoTable[stepOn][0] + memoTable[stepOn][1]
        
    
    
    def climbStairs(self, n):
        memoTable = dict()
        
        return self.calCulateSteps(0,n,memoTable)
        
        
        
