"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1

Example 3
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen = {}
        maxlen = 0
        for right, curr in enumerate(s):
            if curr in seen:
                left=max(left, seen[curr]+1)
            maxlen = max(maxlen, right-left+1)
            seen[curr]=right
        return maxlen