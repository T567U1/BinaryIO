# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        # Write your code here
        self.nums = []
        def go(node, k, g = []):
            if not node:
                self.nums.extend(g[::-1])
                return
            if len(g) == k:
                self.nums.extend(g[::-1])
                g = []
            g += node.val,
            return go(node.next, k, g)
        go(node, k)

        ans = LLNode(self.nums.pop())
        while self.nums:
            ans = LLNode(self.nums.pop(), ans)

        return ans
