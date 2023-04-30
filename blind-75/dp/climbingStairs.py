def climbStairs(n:int)->int:
    if n==0:
        return 1
    if n <0:
        return 0
    leftsum = climbStairs(n-1)
    rightsum = climbStairs(n-2)
    return leftsum+rightsum

def climbStairs(n:int)->int:
    if n==0:
        return 1
    if n <0:
        return 0
    leftsum = climbStairs(n-1)
    rightsum = climbStairs(n-2)
    return leftsum+rightsum

def climbStairsTab(n:int)->int:
    table=[0]*(n+1)
    table[0]=1
    for i in range(n+1):
        if table[i] == 0:
            continue
        for j in [1,2]:
            if (i+j)<=n:
                table[i+j]+=table[i]
    return table[n]

if __name__ == '__main__':
    # print(climbStairs(5))
    print(climbStairsTab(5))