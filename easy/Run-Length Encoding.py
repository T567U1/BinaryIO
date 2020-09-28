class Solution:
    def solve(self, s):
        # Write your code here
        if not s:
            return s
        ans = ''
        c = ''
        for i in s:
            if c and i not in c:
                print(c)
                ans += str(len(c)) + c[0]
                c = ''
            c += i
        else:
            ans += str(len(c)) + c[0]

        return ans
