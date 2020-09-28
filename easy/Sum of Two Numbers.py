import collections
class Solution:
    def solve(self, nums, k):
        # Write your code here
        dic = collections.Counter(nums)
        for i in set(nums):
            dic[i] -= 1
            if k - i in dic and dic[k - i] > 0:
                return True
            dic[i] += 1
        return False
