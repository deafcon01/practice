"""
PS:
Given a string, find the length of the longest substring in it with no more than K
 distinct characters.
"""

def longestSubstringWithKDistinctChars(str1, k):
    start = 0
    max_length = 0
    char_frequency = {}

    for end in range(len(str1)):
        right = str1[end]
        if right not in char_frequency:
            char_frequency[right] = 0
        char_frequency[right] += 1

        while len(char_frequency) > k:
            left = str1[start]
            char_frequency[left] -= 1
            if char_frequency[left] == 0:
                del char_frequency[left]
            start += 1 
            max_length = max(max_length, end-start + 1)
    return max_length

def longestSubstringWithKDistinctChars1(str1, k):
    leftidx=0
    maxlen=0
    char_map = {}
    for rightidx, rightchar in enumerate(str1):
        if rightchar not in char_map:
            char_map[rightchar]=0
        char_map[rightchar]+=1

        while len(char_map) > k:
            leftchar=str1[leftidx]
            char_map[leftchar] -=1
            if char_map[leftchar]==0:
                del char_map[leftchar]
            leftidx+=1
            maxlen=max(maxlen, rightidx-leftidx+1)
    return maxlen


if __name__ == '__main__':
    str1="araaci"
    k=1
    print(longestSubstringWithKDistinctChars(str1, k))
    print(longestSubstringWithKDistinctChars1(str1, k))