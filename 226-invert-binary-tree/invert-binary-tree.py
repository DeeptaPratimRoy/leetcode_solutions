# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def dfs(node):
            if node is None:
                return None
            node.left,node.right = node.right,node.left
            dfs(node.left)
            dfs(node.right)
            return node
        return dfs(root)

        