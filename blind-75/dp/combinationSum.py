def combinationSum(nums:list[int], target:int)-> int:
    table = [1]+[0]*target
    for i in range(target+1):
        if table[i]==0:
            continue
        for num in nums:
            if (i+num)<=target:
                table[i+num]+=table[i]
    return table[target]

if __name__ == '__main__':
    nums = [1,2,3]
    target=4
    print(combinationSum(nums, target))