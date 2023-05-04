'''
Capacity of knapsack = C
weight list : wt = []
price list : pr = []
No. of items = N
'''
def kProfit(C,N,wt,pr,dp):
    # Base Condition
    if N==0 or C==0:
        return 0
    # If sub problem is previously solved tehn return it.
    if dp[N][C] is not None:
        return dp[N][C]
    if wt[N-1] <= C:
        dp[N][C] = max(pr[N-1]+kProfit(C-wt[N-1],N-1,wt,pr,dp), kProfit(C,N-1,wt,pr,dp))
        return dp[N][C]
    else:
        dp[N][C] = kProfit(C,N-1,wt,pr,dp)
        return dp[N][C]
if __name__ == '__main__':
    C = 40
    wt = [30,10,40,20]
    pr = [10,20,30,40]
    N = len(pr)
    # define DP array
    dp = [[None] * (C + 1) for _ in range(N + 1)]
    # Call for kProfit to calculate max profit
    maxProfit = kProfit(C,N,wt,pr,dp)
    print (dp)
    print('Maximum Profit is : ',maxProfit)