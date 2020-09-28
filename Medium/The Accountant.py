class Solution:
    def solve(self, n):
        # Write your code here
        i = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
        ans = []
        while n > 0:
            ans += n % 26,
            n = (n - 1) // 26
        return ''.join([i[x] for x in ans[::-1]])
