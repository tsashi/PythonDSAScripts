from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        d = {0:0, 1:0, 2:0}
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    d[0] += 1
                elif grid[i][j]==1:
                    d[1] += 1
                else:
                    d[2] += 1
                    queue.append([i, j])
        minute = 0
        if d[1]==0:
            return minute
        if d[2]==0:
            print('here')
            return -1
        while queue:
            #every minute, the following loop happens
            for _ in range(len(queue)):
                currcell = queue.popleft()
                currcellrow = currcell[0]
                currcellcol = currcell[1]
                # grid[currcellrow][currcellcol] = 3
                #up becomes rotten if it exists
                if currcellrow != 0 and grid[currcellrow-1][currcellcol]==1:
                    d[1] -= 1
                    grid[currcellrow-1][currcellcol]=2
                    queue.append([currcellrow-1,currcellcol])
                #down becomes rotten if it exists
                if currcellrow != m-1 and grid[currcellrow+1][currcellcol]==1:
                    d[1] -= 1
                    grid[currcellrow+1][currcellcol]=2
                    queue.append([currcellrow+1,currcellcol])
                #left becomes rotten if it exists
                if currcellcol != 0 and grid[currcellrow][currcellcol-1]==1:
                    d[1] -= 1
                    grid[currcellrow][currcellcol-1]=2
                    queue.append([currcellrow,currcellcol-1])
                #right becomes rotten if it exists
                if currcellcol != n-1 and grid[currcellrow][currcellcol+1]==1:
                    d[1] -= 1
                    grid[currcellrow][currcellcol+1]=2
                    queue.append([currcellrow,currcellcol+1])
            minute += 1
            if d[1]==0:
                return minute
        return -1

grid = [[2,1,1],[1,1,0],[0,1,1]]

myobj = Solution()
print(myobj.orangesRotting(grid))

