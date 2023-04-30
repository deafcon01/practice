from itertools import product
def gridTravelerTab(m,n):
    dp = [1]*n
    for _, j in product(range(1, m), range(1, n)):
        dp[j] += dp[j-1]
    return dp[-1]

if __name__ == '__main__':
    m,n=50,50
    # print(gridTraveler(m,n))
    # print(gridTravelerMemo(m,n,dict()))
    print(gridTravelerTab(3,2))