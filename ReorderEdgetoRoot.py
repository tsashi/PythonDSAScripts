from collections import defaultdict, deque
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        mat = defaultdict(dict)
        visited = [False]*n

        for i,j in connections:
            mat[i][j] = 1
            mat[j][i] = 0

        q = deque([0])
        numedgesconvert = 0

        visited[0] = True
        while q:
            currnode = q.popleft()
            for nextnode, edge in mat[currnode].items():
                if not visited[nextnode]:
                    numedgesconvert += edge
                    q.append(nextnode)
                    visited[nextnode] = True
        
        return numedgesconvert
    
myobj = Solution()
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(myobj.minReorder(6, connections))
