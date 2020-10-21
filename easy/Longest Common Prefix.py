class Solution:
    def solve(self, words):
        ans = words[0]
        while words:
            z = words.pop()
            t = ''
            for x, y in zip(ans, z):
                if x != y:
                    break
                t += x
            ans = t

        return ans 
