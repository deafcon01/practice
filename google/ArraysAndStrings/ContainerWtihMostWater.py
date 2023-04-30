"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

HINT: Area = length of shorter vertical line * distance between lines
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<2:
            return 0
        curArea, maxArea=0, 0
        left,right=0,len(height)-1
        while left<=right:
            shorterline=min(height[left], height[right])
            width=right-left
            curArea=shorterline*width
            maxArea=max(maxArea, curArea)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxArea