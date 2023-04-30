from typing import List


class Solution:
    def max_profit(self, prices: List[int]) -> int:
        price_len=len(prices)
        min_price, max_price, i=prices[0],0,0
        while i< price_len:
            if prices[i]<min_price:
                min_price=prices[i]
            if prices[i]-min_price> max_price:
                max_price= prices[i]-min_price
            i+=1
        return max_price



if __name__ == "__main__":
    obj = Solution()
    prices = [7,1,5,3,6,4]
    print(obj.max_profit(prices))
