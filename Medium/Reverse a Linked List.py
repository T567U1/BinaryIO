# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        # Write your code here
        if not node:
            return node
        ans = LLNode(node.val)
        while node.next:
            ans = LLNode(node.next.val, ans)
            node = node.next

        return ans
