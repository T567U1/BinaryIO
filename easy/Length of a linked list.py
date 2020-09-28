# how you do this faster....
# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        # Write your code here
        def go(node, ans = 0):
            if not node:
                return ans
            return go(node.next, ans + 1)

        return go(node)
