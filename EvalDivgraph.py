from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        mat = defaultdict(dict)

        for index,eq in enumerate(equations):
            mat[eq[0]][eq[1]] = values[index]
            mat[eq[1]][eq[0]] = 1/values[index]
        
        n = len(mat)

        def dfs(start:str, end: str, ans: float) -> float:
            for nei, value in mat[start].items():
                if end == nei:
                    return ans*value
                elif not visited[nei]:
                    visited[nei] = True
                    answer = dfs(nei,end,ans*value)
                    if answer != -1:
                        return answer
            return -1

        anslist = []
        for query in queries:
            visited = defaultdict(lambda: False)
            
            visited[query[0]] = True

            answer = dfs(query[0], query[1], 1)

            if answer != -1:
                mat[query[0]][query[1]] = answer
                mat[query[1]][query[0]] = 1/answer
                anslist.append(answer)
            else:
                anslist.append(answer)

        return anslist
    
myobj = Solution()
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
print(myobj.calcEquation(equations, values, queries))

