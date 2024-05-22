from collections import defaultdict, deque
class Solution:
    def minReorder(self, n: int, connections: list[list[int]]) -> int:
        # mat = defaultdict(dict)
        # visited = [False]*n

        # for i,j in connections:
        #     mat[i][j] = 1
        #     mat[j][i] = 0

        # q = deque([0])
        # numedgesconvert = 0

        # visited[0] = True
        # while q:
        #     currnode = q.popleft()
        #     for nextnode, edge in mat[currnode].items():
        #         if not visited[nextnode]:
        #             numedgesconvert += edge
        #             q.append(nextnode)
        #             visited[nextnode] = True
        
        # return numedgesconvert
    
        graph = defaultdict(set)
        for a, b in connections:
            graph[a].add((b, 1))    # Original Edge
            graph[b].add((a, 0))    # Fake Edge to enable complete tree traversal
        print(graph)

        # DFS to traverse over the edges and
        # increment self.count when an edge directs away from '0'
        def dfs(start):
            for nei, is_real in graph[start]:
                if not visited[nei]:
                    self.count += is_real
                    visited[nei] = True
                    dfs(nei)
        
        # To avoid visiting the same node again
        visited = [False] * n
        # Mark the first node as visited
        visited[0] = True
        # To keep track of edges that go away from '0'
        self.count = 0
        
        # Start traversing the graph from '0'
        dfs(0)
        
        return self.count


    
myobj = Solution()
connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
print(myobj.minReorder(6, connections))
