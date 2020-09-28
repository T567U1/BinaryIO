class Solution:
    def solve(self, a):
        # Write your code here
        def go(a, i = 1, x = 1):
            if not a or a < i:
                return -1
            i *= x
            print(i)
            if i == a:
                return x
            return go(a, i, x + 1)

        return go(a)
