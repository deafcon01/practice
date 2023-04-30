"""
Check if possible to generate a target sum
- non-negative
- return boolean
"""

def canSum(nums, target):
    if target==0:
        return True
    if target<0:
        return False
    for i in nums:
        remainder =  target-i
        if canSum(nums, remainder):
            return True
    return False

def canSumMemo(nums, target, memo):
    if target in memo:
        return memo[target]
    if target==0:
        return True
    if target<0:
        return False
    for i in nums:
        remainder = target-i
        if canSumMemo(nums, remainder, memo):
            memo[target] = True
            return True
    memo[target] = False
    return False

def canSumTab(nums, target):
    table= [False]*(target+1)
    table[0]=True
    for i in range(0,target+1):
        if table[target] == True:
            return True
        if table[i]==False:
            continue
        for num in nums:
            if num+i<=target:
                table[num+i]=True
    return table[target]


if __name__ == '__main__':
    nums=[2,4,5,3]
    target=7
    print(canSum(nums, target))
    print(canSumMemo(nums, target, dict()))
    print(canSumTab(nums, target))