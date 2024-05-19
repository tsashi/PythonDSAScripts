# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.visited = 0
        LCA = root
        pathtoroot = []
        pathtonode1 = []
        pathtonode2 = []

        def dfs(node, pathtoroot: [int]):
            # print(node.val, pathtoroot)
            nonlocal pathtonode1, pathtonode2
            pathtoroot = [i for i in pathtoroot]
            pathtoroot.append(node.val)
            if p.val == node.val:
                self.visited += 1
                pathtonode1 = pathtoroot.copy()
            if q.val == node.val:
                self.visited += 1
                pathtonode2 = pathtoroot.copy()
            if self.visited == 2:
                # print("Path to node 1:", pathtonode1)
                # print("Path to node 2:", pathtonode2)
                for i in pathtonode1[-1::-1]:
                    for j in pathtonode2[-1::-1]:
                        if i==j:
                            LCA.val = i
                            break
                    if i==j:
                        break
                return
            if node.left:
                dfs(node.left, pathtoroot)
            if node.right:
                dfs(node.right, pathtoroot)

        if not root:
            return 0
        dfs(root, pathtoroot)
        return LCA