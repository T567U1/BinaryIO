# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        def go(root):
            if not root:
                return float('-inf')

            l = go(root.left)
            r = go(root.right)
            m = max(root.val, l, r)
            print(m, root.val)
            if root.val == m:
                self.ans += 1

            return m

        self.ans = 0
        go(root)

        return self.ans
