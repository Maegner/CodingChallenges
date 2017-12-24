"""
Problem: 
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum 
of all numbers along its path.
Note: You can only move either down or right at any point in time.
"""


def minPathSum(grid):
    w, h = len(grid[0]), len(grid)
    costs = [[9999999999 for x in range(w)] for y in range(h)]
    previous = [[0 for x in range(w)] for y in range(h)]
    target = (h-1,w-1)
    currentPosition = (0,0)
    costs[0][0] = grid[0][0]
    Q = []

    while currentPosition != target:
        right = (currentPosition[0],currentPosition[1]+1)
        down = (currentPosition[0]+1,currentPosition[1])
        if(down[0]<h):
            nextCost = grid[down[0]][down[1]] + costs[currentPosition[0]][currentPosition[1]]
            if costs[down[0]][down[1]] > nextCost:
                costs[down[0]][down[1]] = nextCost
                previous[down[0]][down[1]] = currentPosition
                Q.append((nextCost,down))
        if(right[1]<w):
            nextCost = grid[right[0]][right[1]] + costs[currentPosition[0]][currentPosition[1]]
            if costs[right[0]][right[1]] > nextCost:
                costs[right[0]][right[1]] = nextCost
                previous[right[0]][right[1]] = currentPosition
                Q.append((nextCost,right))
        Q = sorted(Q,key=lambda value: value[0])
        nextPosition = Q.pop(0)[1]
        currentPosition = nextPosition
    return costs[target[0]][target[1]]

shortestPath([[1,2,5],[3,2,1]])