INT_MAX=10000000
def editDistance(str1, str2)->int:
    n = len(str1)
    m = len(str2)
    dp= [[INT_MAX for _ in range(m+1)] for _ in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+ min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    return dp[n][m]

if __name__ == "__main__":
    str1="abad"
    str2="abac"
    print(f"edit distance for {str1} and {str2}: {editDistance(str1, str2)}")
