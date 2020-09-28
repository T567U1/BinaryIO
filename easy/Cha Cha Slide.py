class Solution:
    def solve(self, s0, s1):
        # Write your code here
        if len(s0) != len(s1):
            return False
        return s0 in s1 + s1
