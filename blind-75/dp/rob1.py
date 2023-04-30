def rob(nums:list[int])->int:
    prev1, prev2=0,0
    for i in range(0,len(nums)):
        num=nums[i]
        tmp=prev1
        prev1= max(prev2+num, prev1)
        prev2= tmp
    return prev1

if __name__ == '__main__':
    nums = [2,3,2]
    print(rob(nums))