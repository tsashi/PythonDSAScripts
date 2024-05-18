# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return None
        rightsideelements = []
        bfsstack = []
        bfsstack.append(root)
        while len(bfsstack)>0:
            n = len(bfsstack)
            rightsideelements.append(bfsstack[-1].val)
            for i in range(n):
                node = bfsstack.pop(0)
                if node.left:
                    bfsstack.append(node.left)
                if node.right:
                    bfsstack.append(node.right)
        return rightsideelements