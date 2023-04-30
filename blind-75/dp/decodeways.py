def numdecodings(s: str)->int:
    if not s:
        return 0
    strlen= len(s)
    dp=[1]+[0]*strlen
    dp[1]= 0 if s[0]=='0' else 1
    for i in range(2,strlen+1):
        if 0<int(s[i-1:i])<=9:
            dp[i]+=dp[i-1]
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i - 2]
    return dp[strlen]
    

if __name__=='__main__':
    s="231"
    print(numdecodings(s))