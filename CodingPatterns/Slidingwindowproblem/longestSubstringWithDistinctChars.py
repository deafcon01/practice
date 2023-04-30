def LongestSubstringWithDistinctChars(s):
    left=0
    seen = {}
    maxlen = 0
    for right, curr in enumerate(s):
        if curr in seen:
            left=max(left, seen[curr]+1)
        maxlen = max(maxlen, right-left+1)
        seen[curr]=right
    return maxlen

if __name__ == '__main__':
    s = "abcdbcbb"
    print(LongestSubstringWithDistinctChars(s))