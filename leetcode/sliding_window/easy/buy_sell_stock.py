from typing import List

class Solution: # this one is kind of like two pointers
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0
        
        l, r = 0, 1
        profit = 0
        
        while r < len(prices): # while our search pointer is not at the last element in the array
            if (prices[l] < prices[r]): # if the left price is lower than the right price, there'll be profit
                profit = max(prices[r] - prices[l], profit) # check if the new profit is more than the old, then assign
            else:
                l = r # if the left stock price is greater than the right, set the new left to new starting point
            r += 1 # increment the window
    
        return profit
                    

txt_file = open(
    "/Users/kyvaunebrammer/Projects/leetcode/sliding_window/easy/test_prices.txt", "r")
file_content = txt_file.read()
txt_file.close()

content_list = file_content.replace("[","").replace("]","").split(",")
content_list = list(map(int, content_list))

print(str(Solution().maxProfit(content_list)))
