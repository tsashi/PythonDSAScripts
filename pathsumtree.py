# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0
        sumonpath = []
        def dfs(root:TreeNode, sumonpath:[int]):
            nonlocal targetSum
            if root:
                sumonpath = [i+j for i,j in zip(sumonpath,[root.val]*len(sumonpath))]
                sumonpath.append(root.val)
                # print(sumonpath)
                for i in range(len(sumonpath)):
                    if sumonpath[i]==targetSum:
                        nonlocal result
                        result += 1
                if root.left:
                    dfs(root.left, sumonpath)
                if root.right:
                    dfs(root.right, sumonpath)
        
        if not root:
            return 0
        dfs(root, sumonpath)
        return result
