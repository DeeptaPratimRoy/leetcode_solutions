# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def dfs(p,q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val !=q.val:
                return False
            return dfs(p.left,q.right) and dfs(p.right,q.left)
        return dfs(root.left,root.right)

            
            
            
            
        