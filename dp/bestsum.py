"""
Return best possible to generate a target sum
- non-negative
- return boolean
"""
def bestSum(nums,target):
    if target == 0:
        return []
    if target <0:
        return None
    shortestcombination = None
    for i in nums:
        remainder =  target-i
        remaindercombination = bestSum(nums,remainder)
        if remaindercombination != None:
            combination = [*remaindercombination, i]
            if shortestcombination==None or len(combination)<len(shortestcombination):
                shortestcombination = combination
    return shortestcombination

def bestSumMemo(nums,target, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target <0:
        return None
    shortestcombination = None
    for i in nums:
        remainder =  target-i
        remaindercombination = bestSumMemo(nums,remainder, memo)
        if remaindercombination != None:
            combination = [*remaindercombination, i]
            if shortestcombination==None or len(combination)<len(shortestcombination):
                shortestcombination = combination
    memo[target] =  shortestcombination
    return shortestcombination

def bestSumTab(nums, target):
    table=[None]*(target+1)
    table[0]=[]
    for i in range(target+1):
        if table[i] == None:
            continue
        for num in nums:
            if i+num<=target:
                func= lambda table,num,i:[*table[i],num] if(table[num+i]==None or len(table[num+i])>len([*table, num])) else table[num+i]
                table[num+i] = func(table,num,i)
    return table[target]

if __name__ == '__main__':
    nums=[2,4,5,3,7]
    target=7
    # nums=[1,2,5,25]
    # target=100
    # print(bestSum(nums,target))
    print(bestSumMemo(nums,target, dict()))
    print(bestSumTab(nums,target))