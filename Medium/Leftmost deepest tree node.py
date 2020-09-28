# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        # Write your code here
        self.dic = {}
        def go(root, level = 0):
            if not root:
                return
            if level in self.dic:
                pass
            else:
                self.dic[level] = root.val
            go(root.left, level + 1)
            go(root.right, level + 1)

        go(root)
        return self.dic[max(self.dic)]
