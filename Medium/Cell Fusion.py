class Solution:
    def solve(self, cells):
        #brute force
        while len(cells) > 1:
            cells.sort()
            a = cells.pop()
            b = cells.pop()
            if a == b:
                continue
            else:
                cells += (a + b) // 3,

        return cells[-1] if cells else -1
        #heap
        '''
        def solve(self, cells):
        cells = [-x for x in cells]
        heapify(cells)
        while len(cells) > 1:
            a, b = -heappop(cells), -heappop(cells)
            if a != b:
                heappush(cells, -((a + b) // 3))
        return -cells[0] if cells else -1
        '''
