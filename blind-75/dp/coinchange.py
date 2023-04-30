def coinChange(coins:list[int], amt: int)-> int:
    table=[0]+[amt+1]*(amount)
    for i in range(amt+1):
        if table[i]==-1:
            continue
        for coin in coins:
            if i+coin<=amt:
                func= lambda table,coin, i: table[i]+1 if table[i+coin]>table[i] else table[i+coin]
                table[coin+i] = func(table, coin, i)
    if table[amt]==amt+1:
        return -1
    return table[amt]

if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11
    print(coinChange(coins,amount))