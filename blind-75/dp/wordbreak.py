def wordbreak(s: str, wordDict: list[str]) -> bool:
    n = len(s)
    dp = [True]+[False]*(n)
    for i in range(n+1):
        if dp[i]==False:
            continue
        for word in wordDict:
            if (i+len(word))<=n and s[i:i+len(word)]==word:
                dp[i+len(word)]=True
    return dp[n]


if __name__=="__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    print(wordbreak(s, wordDict))