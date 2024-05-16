# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1list = self.leafsequence(root1)
        root2list = self.leafsequence(root2)
        return (root1list == root2list)

    def leafsequence(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        if (not root.left) and (not root.right):
            return [root.val]
        leftlist = self.leafsequence(root.left)
        rightlist = self.leafsequence(root.right)
        return leftlist + rightlist