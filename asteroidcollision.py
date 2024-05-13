class Solution:
    def asteroidCollision(self, ast: list[int]) -> list[int]:        
        n=len(ast)
        i = n-1
        while i>0:
            if ast[i]<0 and ast[i-1]>0:
                if abs(ast[i])==ast[i-1]:
                    ast.pop(i)
                    ast.pop(i-1)
                    i -= 1
                    if i >= len(ast):
                        i = len(ast)-1
                elif abs(ast[i])>ast[i-1]:
                    ast.pop(i-1)
                    i -= 1
                else:
                    ast.pop(i)
                    if i >= len(ast):
                        i = len(ast)-1
            else:
                i -= 1
        return ast
myobj = Solution()
asteroids = [-2, -2, 1, -1]
print(myobj.asteroidCollision(asteroids))

