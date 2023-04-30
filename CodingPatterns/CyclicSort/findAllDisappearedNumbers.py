def findDisappearedNumbers(nums: list[int]) -> list[int]:
    i=0
    while i<len(nums):
        if nums[i]!=nums[nums[i]-1]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        else:
            i+=1
    return [it+1 for it in range(len(nums)) if it+1 != nums[it]]

if __name__ == '__main__':
    nums = [4,3,2,7,8,2,3,1]
    print(findDisappearedNumbers(nums))