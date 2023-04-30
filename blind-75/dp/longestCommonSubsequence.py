def longestCommonSubsequence(text1: str, text2: str) -> int:
    m,n=map(len,(text1,text2))
    dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif text1[i-1]==text2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]

def longestCommonSubsequence1(text1: str, text2: str) -> int:
    m, n = map(len, (text1, text2))
    if m < n:
        return longestCommonSubsequence1(text2, text1)
    dp = [0] * (n + 1)
    for c in text1:
        prevRow, prevRowPrevCol = 0, 0
        for j, d in enumerate(text2):
            prevRow, prevRowPrevCol = dp[j + 1], prevRow
            dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
    return dp[-1]

#Space optimised ones below
def longestCommonSubsequence2(text1: str, text2: str) -> int:
    m,n = map(len,(text1,text2))
    dp,dpprev = map(lambda x: [0]*(x+1), (n,n))
    for i in range(1, m+1):
        for j in range(1,n+1):
            if text1[i-1]==text2[j-1]:
                dp[j]=dpprev[j-1]+1
            else:
                dp[j]=max(dp[j-1], dpprev[j])
        dp, dpprev=dpprev,dp
    return dpprev[n]

def longestCommonSubsequence3(text1: str, text2: str) -> int:
    m,n = map(len,(text1,text2))
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    for i in range(1, m+1):
        for j in range(1,n+1):
            if text1[i-1]==text2[j-1]:
                dp[i%2][j]=dp[(i+1)%2][j-1]+1
            else:
                dp[i%2][j]=max(dp[i%2][j-1], dp[(i+1)%2][j])
    return dp[m%2][n]

if __name__ == "__main__":
    text1="ace"
    text2="abcde"
    print(longestCommonSubsequence(text1, text2))
    print(longestCommonSubsequence1(text1, text2))
    print(longestCommonSubsequence2(text1, text2))
    print(longestCommonSubsequence3(text1, text2))
    