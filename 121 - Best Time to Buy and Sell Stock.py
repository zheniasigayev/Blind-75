class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy and Sell represent the dates 
        buy = 0 # Must buy before selling
        sell = 1 # Must sell after buying
        maxProfit = 0 # Initialize to zero since no transactions were made yet
        
        while sell < len(prices): # 
            if prices[buy] < prices[sell]: # Check if transaction is profitable
                profit = prices[sell] - prices[buy] # Calculate profit
                maxProfit = max(maxProfit, profit) # Determines max profit from previously calculated values 
            else:
                buy = sell # Buy is higher than sell, so we set buy = sell to get lowest purchase price. Even if down                       the road there isn't a higher selling price, we're fine since the maxProfit variable won't update
            sell += 1 # Increment regardless in an attempt to find a lower buy value / higher sell value
        return maxProfit # Returns 0 if array was descending (highest -> lowest)

        
    """
    1. Initialize Buy to 0 and Sell to 1 since buying comes before selling
    2. Set MaxProfit to 0 since no transactions were made yet
    3. Iterate over the list. Won't have index out of bounds error since we use strictly less than
    4. Check to see if transaction is profitable
        4.1. If True, calculate profit and check if it's the largest seen so far
        4.2. If False, set buy date to sell date since price of stock is cheaper at that sell date (aka cheaper to buy)
    5. Increment sell date to repeat from Step 3
    6. Return maxProfit. If it was never profitable, returns 0 as was initialized 

    
    Runtime: O(n) - Loops through entire array once
    Memory: O(1) - No use of external arrays etc. Just used variables and pointers. 
    
    
    """