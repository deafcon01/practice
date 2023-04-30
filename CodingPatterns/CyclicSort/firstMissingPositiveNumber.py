def firstMissingPositive(nums: list[int]):
    i=0
    while i<len(nums):
        if nums[i]>0 and nums[i]<len(nums) and nums[i]!=nums[nums[i]-1]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        else:
            i+=1
    num= len(nums)
    for i in range(num):
        if nums[i]!=i+1:
            return i+1
    return num+1

if __name__=='__main__':
    nums = [1,2,0]
    print(firstMissingPositive(nums))