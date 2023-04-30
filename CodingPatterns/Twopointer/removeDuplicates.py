def removeDuplicates(nums: list[int]) -> int:
    left=0
    for idx in range(1,len(nums)):
        if nums[left]!=nums[idx]:
            nums[left+1]=nums[idx]
            left+=1
    return left+1

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(removeDuplicates(nums))
