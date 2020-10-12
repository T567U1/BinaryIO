# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, ll0, ll1):
        x = set()
        def go(root, x):
            if not root:
                return
            x.add(root.val)
            go(root.next, x)

        go(ll0, x)
        go(ll1, x)

        x = sorted(x)
        ans = LLNode(x.pop())
        while x:
            ans = LLNode(x.pop(), ans)

        return ans
