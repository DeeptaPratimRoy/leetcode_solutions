class Solution:
    def isSymmetric(self, root):

        def dfs(a, b):
            if a is None and b is None:
                return True

            if a is None or b is None:
                return False

            if a.val != b.val:
                return False

            return dfs(a.left, b.right) and dfs(a.right, b.left)

        return dfs(root.left, root.right)