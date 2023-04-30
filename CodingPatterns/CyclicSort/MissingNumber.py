def missingNumber(nums:list[int])->int:
    start = 0 
    n = len(nums)
    while start<n:
        num =  nums[start]
        if num<n and num!=start:
            nums[start], nums[num]=nums[num], nums[start]
        else:
            start+=1
    for i in range(len(nums)):
            if nums[i] != i:
                return i
    return len(nums)

if __name__ == '__main__':
    nums =  [9,6,4,2,3,5,7,0,1]
    print(missingNumber(nums))