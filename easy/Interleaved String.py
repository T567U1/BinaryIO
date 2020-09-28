class Solution:
    def solve(self, s0, s1):
        # Write your code here
        s0 = list(s0)
        s1 = list(s1)
        ans = ''
        while s1 and s0:
            ans += s0.pop(0) + s1.pop(0)

        ans += ''.join(s0) + ''.join(s1)
        return ans
            
