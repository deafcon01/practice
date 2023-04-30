"""
PS:
Given an array of positive integers and a number ‘S,’ find the length of the 
smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
Return 0 if no such subarray exists.
"""
import math 
def smallestsubarraysum(S, nums):
    start, winsum=0,0
    minlen=math.inf
    for end in range(len(nums)):
        winsum+=nums[end]
        while winsum>=S:
            minlen = min(end-start+1, minlen)
            winsum-=nums[start]
            start+=1
    if minlen==len(nums):
        return 0
    return minlen

if __name__ == '__main__':
    nums =  [2, 1, 5, 2,8]
    S = 7
    print(smallestsubarraysum(S, nums))
        