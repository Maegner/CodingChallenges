class Solution(object):
    
    def maxSubArray(self, nums):
        
        sums = [0] * len(nums)
        sums[0] = nums[0]
        
        for lastElementInSubArray in range(1,len(sums),1):
            sums[lastElementInSubArray] = max(sums[lastElementInSubArray-1]+nums[lastElementInSubArray],nums[lastElementInSubArray])
            
        return max(sums)
