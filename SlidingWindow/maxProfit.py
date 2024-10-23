class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_Profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_Profit = max(max_Profit, profit)
            else:
                l = r
            r += 1

        return max_Profit




#test
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))

