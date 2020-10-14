class Solution:
    def solve(self, intervals):
        x = sorted(intervals, key = lambda x: x[0])
        y = sorted(intervals, key = lambda x: x[1])

        return [x[-1][0], y[0][1]]
