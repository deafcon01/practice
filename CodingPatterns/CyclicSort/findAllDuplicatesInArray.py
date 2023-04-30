def findDuplicates(nums:list[int])->list[int]:
    # for i in range(len(nums)):
    #     while i != nums[i] - 1 and nums[i] != nums[nums[i]-1]:
    #         nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    i=0
    while i<len(nums):
        if nums[i]!=nums[nums[i]-1]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        else:
            i+=1

    return [nums[it] for it in range(len(nums)) if it != nums[it] - 1]

if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    print(findDuplicates(nums))