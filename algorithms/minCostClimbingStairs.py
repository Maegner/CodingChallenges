"""
Problem:
    On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
    Once you pay the cost, you can either climb one or two steps. 
    You need to find minimum cost to reach the top of the floor, and you 
    can either start from the step with index 0, or the step with index 1. 
"""

def minCostClimbingStairs(cost):
    if cost == []:
        return 0
    jump2cost = 0
    jump1cost = 0
    for i in range (-len(cost)-1,-1,-1):
        hereCost = cost[i] + min(jump1cost,jump2cost)
        jump2cost = jump1cost
        jump1cost = hereCost
    return min(jump1cost,jump2cost)

print(minCostClimbingStairs([0,1,1,0]))