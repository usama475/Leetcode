class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minimum_price= prices[0]
        max_profit=0 
        # for i in range(len(prices)):
        #     price=prices[i]
        for price in prices:
            if price<minimum_price:
                minimum_price=price
            else:
                profit=price-minimum_price
                max_profit=max(profit,max_profit)   
        return max_profit             

    







        
    #    if not prices:
    #     return 0 
    #    min_price= prices[0]
    #    max_profit=0
    #    for price in prices[1:]:
    #      if price<min_price:
    #        min_price=price
    #      else:
    #       profit=price-min_price   
    #       max_profit= max(profit, max_profit) 
    #    return max_profit        
