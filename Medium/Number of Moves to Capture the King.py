class Solution:
    def solve(self, A):
        N = len(A)
        que = []
        for x in range(N):
            for y in range(N):
                if A[x][y] == 1:
                    que += (x, y),
                if A[x][y] == 2:
                    kr, kc = x, y

        dirs = [[x, y] for x in range(-2, 3) for y in range(-2, 3) if abs(x * y) == 2]
        dist = {loc: 0 for loc in que}

        for x,y in que:
            if x == kr and y == kc:
                return dist[x, y]
            for x1, y1 in dirs:
                nei = nr, nc = x + x1, y + y1
                if 0 <= nr < N and 0 <= nc < N and nei not in dist:
                    dist[nei] = dist[x, y] + 1
                    que += nei,

        return -1
