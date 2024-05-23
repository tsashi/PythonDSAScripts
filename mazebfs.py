from collections import deque
class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        entrancerow = entrance[0]
        entrancecol = entrance[1]
        totrow = len(maze)
        totcol = len(maze[0])
        bfsstack = deque()
        bfsstack.append(entrance)
        numofsteps = 0
        maze[entrance[0]][entrance[1]] = str(numofsteps)
        
        def checkcellonboundary(currcell: list[int]) -> bool:
            if currcell[0]==0 or currcell[0]==totrow-1 or currcell[1]==0 or currcell[1]==totcol-1:
                return True
            else:
                return False

        while bfsstack:
            for _ in range(len(bfsstack)):
                currcell = bfsstack.popleft()
                currcellrow = currcell[0]
                currcellcol = currcell[1]
                #go up if possible
                if currcellrow != 0 and maze[currcellrow-1][currcellcol]==".":
                    numofsteps = int(maze[currcellrow][currcellcol])
                    if checkcellonboundary([currcellrow-1, currcellcol]):
                        return (numofsteps+1)
                    else:
                        numofsteps +=1
                        maze[currcellrow-1][currcellcol] = str(numofsteps)
                        bfsstack.append([currcellrow-1, currcellcol])
                #go down if possible
                if currcellrow != totrow-1 and maze[currcellrow+1][currcellcol]==".":
                    numofsteps = int(maze[currcellrow][currcellcol])
                    if checkcellonboundary([currcellrow+1, currcellcol]):
                        return (numofsteps+1)
                    else:
                        numofsteps += 1
                        maze[currcellrow+1][currcellcol] = str(numofsteps)
                        bfsstack.append([currcellrow+1, currcellcol])
                #go left if possible
                if currcellcol != 0 and maze[currcellrow][currcellcol-1]==".":
                    numofsteps = int(maze[currcellrow][currcellcol])
                    if checkcellonboundary([currcellrow, currcellcol-1]):
                        return (numofsteps+1)
                    else:
                        numofsteps += 1
                        maze[currcellrow][currcellcol-1] = str(numofsteps)
                        bfsstack.append([currcellrow,currcellcol-1])
                #go right if possible
                if currcellcol != totcol-1 and maze[currcellrow][currcellcol+1]==".":
                    numofsteps = int(maze[currcellrow][currcellcol])
                    if checkcellonboundary([currcellrow, currcellcol+1]):
                        return (numofsteps+1)
                    else:
                        numofsteps += 1
                        maze[currcellrow][currcellcol+1] = str(numofsteps)
                        bfsstack.append([currcellrow,currcellcol+1])
        return -1

myobj = Solution()
maze = [["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".",".",".","+"],["+","+","+","+",".","+","."]]
entrance = [0,1]
print(myobj.nearestExit(maze,entrance))