"""
From top left to bottom right
valid moves: right , down
Find shortest path
"""

def gridTraveler(m,n):
    #base case
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    return gridTraveler(m-1,n)+gridTraveler(m,n-1)

def gridTravelerMemo(m,n,memo):
    key = str(m)+','+str(n)
    if key in memo:
        return memo[key]
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    memo[key]= gridTravelerMemo(m-1,n,memo)+gridTravelerMemo(m,n-1,memo)
    return memo[key]

def gridTravelerTab(m,n):
    tb = [[0]*(n+1)]*(m+1)
    tb[1][1]=1
    for i in range(m+1):
        for j in range(n+1):
            current=  tb[i][j]
            if (j+1)<=n:
                tb[i][j+1]=current
            if (i+1)<=m:
                tb[i+1][j]=current
    return tb[m][n]

if __name__ == '__main__':
    m,n=50,50
    # print(gridTraveler(m,n))
    # print(gridTravelerMemo(m,n,dict()))
    print(gridTravelerTab(18,18))
