class Solution:
    def solve(self, nums):
        # Write your code here
        i = list(sorted(set(nums)))
        return i == nums or i[::-1] == nums
