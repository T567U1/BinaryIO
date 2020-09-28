class Solution:
    def solve(self, n):
        # Write your code here
        ans = []
        for i in range(1, n + 1):
            i = str(i)
            if int(i) % 3 == 0 or '3' in i or '6' in i or '9' in i:
                ans += 'clap',
            else:
                ans += i,

        return ans
