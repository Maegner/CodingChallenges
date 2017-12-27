"""
Problem:
    Given a 2D binary matrix filled with 0's and 1's,
    find the largest square containing only 1's and return its area. 
"""


def isSquare(x,y,matrix,size,mem):
    
    if (x,y) in mem :
        return False

    if x + size > len(matrix) or y + size > len(matrix[0]):
        return False
    for rowNr in range (x,x+size,1):
        for elementNr in range (y,y+size,1):
            if matrix[rowNr][elementNr] == '0':
                mem.append((rowNr-1,elementNr))
                return False
    return True
    
def maximalSquare(matrix):
    if matrix == []:
        return 0
    maxArea = 0
    height = len(matrix)
    width = len(matrix[0])
    inSquare = True
    mem = []
    x = 0
    for row in matrix:
        y = 0
        for element in row:
            currentArea = 0
            if element == '1':
                currentArea = 1
                while inSquare:
                    
                    if isSquare(x,y,matrix,currentArea,mem):
                        maxArea = max(maxArea,currentArea)
                        currentArea +=1
                    else:
                        inSquare = False
                inSquare = True
            y += 1
        x+=1
    return maxArea**2

matrix = [["0","1","1","0","0","1","0","1","0","1"],["0","0","1","0","1","0","1","0","1","0"],["1","0","0","0","0","1","0","1","1","0"],["0","1","1","1","1","1","1","0","1","0"],["0","0","1","1","1","1","1","1","1","0"],["1","1","0","1","0","1","1","1","1","0"],["0","0","0","1","1","0","0","0","1","0"],["1","1","0","1","1","0","0","1","1","1"],["0","1","0","1","1","0","1","0","1","1"]]
print(maximalSquare(matrix))