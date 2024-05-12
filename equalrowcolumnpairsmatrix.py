class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        gridtr = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid))]

        pairs = 0
        for i in grid:
            for j in gridtr:
                if i ==j:
                    pairs +=1
        return pairs

        #fast code using zip() and map()
        # tpse = Counter(zip(*grid))
        # grid = Counter(map(tuple,grid))
        # return sum(tpse[t]*grid[t] for t in tpse)

        #code using defaultdict()
        # rc = defaultdict(int)
        # c = 0
        # for row in grid:
        #     rc[tuple(row)] += 1
        # for column in zip(*grid):
        #    c += rc[column]
        # return c