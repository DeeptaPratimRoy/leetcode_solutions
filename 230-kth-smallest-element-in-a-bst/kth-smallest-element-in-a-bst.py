class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = [0]
        def dfs(node):
            if node is None:
                return None
            left = dfs(node.left)
            if left is not None:
                return left
            count[0] += 1
            if count[0] == k:
                return node.val
            return dfs(node.right)
        return dfs(root)