from typing import List
from collections import defaultdict
def combinationSum(nums:List[int], target: int):
    # dp = dict()
    dp = defaultdict(int)
    dp[0] = 1 # base case
    for i in range(0, target):
        for x in nums:
            # if i+x not in dp.keys():
            #     dp [i+x] = 0
            dp[i+x] += dp[i]
    return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(combinationSum(nums, target))
