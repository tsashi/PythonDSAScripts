class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [1]*len(rooms)

        def dfs(rooms: list[list[int]], currentkeys: list[int]):
            nonlocal visited
            for i in currentkeys:
                if visited[i]==1:
                    # print("room :",i)
                    visited[i] = 0            
                    dfs(rooms, rooms[i])
        
        visited[0] = 0
        dfs(rooms, rooms[0])

        if sum(visited) == 0:
            return True
        else:
            return False


myobj = Solution()
rooms = [[1,3],[3,0,1],[2],[0]]
print(myobj.canVisitAllRooms(rooms))
