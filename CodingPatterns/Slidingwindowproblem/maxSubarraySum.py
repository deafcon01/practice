"""
problem statement: Given an array of positive numbers and a positive number ‘k,’ 
find the maximum sum of any contiguous subarray of size ‘k’.

If you observe closely, you will realize that to calculate the sum of a contiguous subarray, 
we can utilize the sum of the previous subarray. For this, consider each subarray as a 
Sliding Window of size ‘k.’ To calculate the sum of the next subarray, we need to slide the 
window ahead by one element. So to slide the window forward and 
calculate the sum of the new position of the sliding window, 
we need to do two things:

- Subtract the element going out of the sliding window, i.e., subtract the first element of the window.
- Add the new element getting included in the sliding window, i.e., the element coming right after the end of the window.
"""
def maxSubArrayK(k, nums):
    maxsum, start, winsum =0,0,0
    for idx, end in enumerate(nums):
        winsum += end
        if idx >= k-1:
            maxsum =  max(maxsum, winsum)
            winsum-=nums[start]
            start+=1
    return maxsum

if __name__ == '__main__':
    k=3
    nums=[2, 1, 5, 1, 3, 2]
    print(maxSubArrayK(k, nums))