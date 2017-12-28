"""
Problem:
    You are a professional robber planning to rob houses along a street. 
    Each house has a certain amount of money stashed, the only constraint 
    stopping you from robbing each of them is that adjacent houses have security
    system connected and it will automatically contact the police if two adjacent
    houses were broken into on the same night.
    Given a list of non-negative integers representing the amount of money of each house,
    determine the maximum amount of money you can rob tonight without alerting the police.
"""


def auxRob(nums,i,mem,currentValue):
    if i in mem:
        return mem[i] + currentValue
    if i >= 0:
        return currentValue
    else:
        mem[i] = max(auxRob(nums,i+2,mem,currentValue+nums[i]),auxRob(nums,i+1,mem,currentValue))
    return mem[i]

#ACCEPTED BUT TOO SLOW
def rob(nums):
    nValues = len(nums)
    mem = {}
    mem[-1] = nums[-1]
    for i in range (-2,-nValues-1,-1):
        auxRob(nums,i,mem,0)
    return mem[-nValues]

#ACCEPTED BUT FAST
def efficientRob(nums):
    if nums == []:
        return 0
    yesPrev = 0
    notPrev = 0
    for value in nums:
        currentYes = notPrev + value
        currentNo = max(yesPrev,notPrev)
        yesPrev = currentYes
        notPrev = currentNo
    return max(currentYes,currentNo)