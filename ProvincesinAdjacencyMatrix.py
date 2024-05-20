class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        visited = set()
        province = 0


        def dfs(city:int):
            for ind, con in enumerate(isConnected[city]):
                if ind not in visited and con == 1:
                    visited.add(ind)
                    dfs(ind)

        for i in range(n):
            if i not in visited:
                province += 1
                visited.add(i)
                dfs(i)
        
        return province

myobj = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(myobj.findCircleNum(isConnected))
