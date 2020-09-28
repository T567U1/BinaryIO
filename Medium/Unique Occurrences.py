import collections
class Solution:
    def solve(self, nums):
        # Write your code here
        nums = collections.Counter(nums)
        return len(nums.values()) == len(set(nums.values()))
