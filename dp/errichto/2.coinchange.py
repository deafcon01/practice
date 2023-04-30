"""
Min possible coins used
"""
from collections import defaultdict
def coinChange(nums, target):
    dp=defaultdict(lambda:float('inf'))
    dp[0]=0
    for amount in range(1,target+1):
        for coin in nums:
            if amount-coin >= 0:
                dp[amount]=min(dp[amount],dp[amount-coin]+1)
    return dp[target]

if __name__ == '__main__':
    nums = [1, 2, 5]
    target = 11
    print(coinChange(nums, target))