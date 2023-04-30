"""
Return combination, If not possible return None
"""

def howSum(nums, target):
    if target==0:
        return []
    if target<0:
        return None
    for i in nums:
        remainder = target-i
        result = howSum(nums, remainder)
        if result != None:
            return [i,*result]
    return None

def howSumMemo(nums, target, memo):
    if target in memo:
        return memo[target]
    if target==0:
        return []
    if target<0:
        return None
    for i in nums:
        remainder = target-i
        result = howSumMemo(nums, remainder, memo)
        if result != None:
            memo[target]= [i,*result ]
            return memo[target]
    memo[target] = None
    return None

def howSumTab(nums, target):
    table=[None]*(target+1)
    table[0]=[]
    for i in range(target+1):
        if table[i] == None:
            continue
        for num in nums:
            if i+num<=target:
                table[num+i]=[num,*table[i]]
    return table[target]

if __name__ == '__main__':
    nums=[5,3,4]
    target=7
    print(howSum(nums, target))
    print(howSumMemo(nums, target, dict()))
    print(howSumTab(nums, target))