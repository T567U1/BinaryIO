# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        self.ans = 0
        def go(root):
            if not root:
                return
            self.ans += root.val
            go(root.left)
            go(root.right)

        go(root)

        return self.ans
