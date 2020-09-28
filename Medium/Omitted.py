class Solution:
    def solve(self, nums):
        # Write your code here
        # get product forward and backwards
        ans = []
        x = [1]
        y = [1]
        for i, j in zip(nums, nums[::-1]):
            x += i * x[-1],
            y = [j * y[0]] + y
        #first item of x is one and it won't affect results last item on y is 
        #not cominig so it can be left out
        for z, (i, j) in enumerate(zip(x, y[1:])):
            print(i, j)
            ans += i * j,

        return ans
