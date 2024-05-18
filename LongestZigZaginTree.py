# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root: TreeNode, max:int, dir: str):
            # print("new dfs",root, max, dir)
            nonlocal result
            if root:
                if dir=='left':
                    if root.right:
                        if result<max+1:
                            result = max+1 
                        dfs(root.right,max+1,'right')
                    if root.left:
                        dfs(root.left,1,'left')
                elif dir=='right':
                    if root.left:
                        if result<max+1:
                            result = max+1 
                        dfs(root.left,max+1,'left')
                    if root.right:
                        dfs(root.right,1,'right')
        
        if not root:
            return 0
        if root.left or root.right:
            result = 1
        if root.left:
            dfs(root.left,1,'left')
        if root.right:
            dfs(root.right,1,'right')
        return result
    
        # efficient code
        # self.maximum = 0
        # def dfs(node, left, right):
        #     self.maximum = max(self.maximum, left, right)
        #     if node.left:
        #         dfs(node.left, right+1, 0)
        #     if node.right:
        #         dfs(node.right, 0, left+1)
        # dfs(root, 0, 0)
        # return self.maximum