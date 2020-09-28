class Solution:
    def solve(self, s):
        # Write your code here
        ans = ' '
        for i in s:
            if i == ans[-1]:
                continue
            else:
                ans += i

        return ans[1:]
