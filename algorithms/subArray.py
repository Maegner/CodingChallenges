def  subarraySum(arr): #TOO SLOW, O(n²)
    
    result = 0
    lenghtArray = len(arr)
    iterator = 0
    prevResult = 0  #prevents recalculation
    
    for element in arr:
        result += element
        prevResult  = element
        
        for i in range (iterator+1,lenghtArray,1):
            prevResult += arr[i]
            result += prevResult
        iterator += 1
        
    return result