def countPairs(numbers,k):
    mem = dict()
    count = 0
    for number in numbers:
        if not number in mem:
            mem[number] = number
    for key in mem:
        if key + k in mem:
            count += 1
    return count

print(countPairs([1,2,3,4,5,6],2))