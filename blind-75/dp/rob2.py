def rob(nums:list[int])->int:
    if len(nums)==1:
        return nums[0]
    prev1, prev2=0,0
    for i in range(0,len(nums)-1):
        num=nums[i]
        tmp=prev1
        prev1= max(prev2+num, prev1)
        prev2= tmp
    max1=prev1
    prev1, prev2=0,0
    for i in range(1, len(nums)):
        num=nums[i]
        tmp=prev1
        prev1= max(prev2+num, prev1)
        prev2= tmp
    max2=prev1
    return max(max1, max2)

if __name__ == '__main__':
    nums = [2,3,2]
    print(rob(nums))