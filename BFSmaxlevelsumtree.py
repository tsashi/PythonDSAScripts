# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        bfsstack = deque([(root)])
        maxsum = -10**5-1
        maxlevel = 0
        level = 0
        while bfsstack:
            currsum = 0
            level += 1
            for _ in range(len(bfsstack)):
                node = bfsstack.popleft()
                currsum += node.val
                if node.left:
                    bfsstack.append(node.left)
                if node.right:
                    bfsstack.append(node.right)
            if maxsum < currsum:
                maxsum = currsum
                maxlevel = level
        return maxlevel