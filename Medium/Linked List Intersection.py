# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, l0, l1):
        x = set()
        y = set()
        def go(root, s):
            if not root:
                return
            s.add(root.val)
            go(root.next, s)

        go(l0, x)
        go(l1, y)

        z = sorted(x.intersection(y))
        ans = LLNode(z.pop())
        while z:
            ans = LLNode(z.pop(), ans)

        return ans
        
