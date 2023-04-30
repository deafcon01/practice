from typing import List
class Solution:
    """
    Kadane's Algorithm
    """
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=cursum=nums[0]
        for i in nums[1:]:
            cursum=max(cursum+i,i)
            maxsum=max(maxsum,cursum)
        return maxsum