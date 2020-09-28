class Solution:
    def solve(self, nums):
        # Write your code here
        ans = sorted(set(nums), key = lambda x: nums.count(x))
        return nums.count(ans[-1])
