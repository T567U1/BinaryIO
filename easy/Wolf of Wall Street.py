class Solution:
    def solve(self, prices):
        # Write your code here
        if not prices:
            return 0
        ans = float('-inf')
        m = prices.index(max(prices))

        while True:
            ans = max(prices[m] - min(prices[:m + 1]), ans)
            prices = prices[m + 1:]
            if not prices:
                break
            m = prices.index(max(prices))

        return ans
