class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node, targetSum):
            if node is None:
                return False
            targetSum = targetSum - node.val
            if node.left is None and node.right is None:
                return targetSum == 0
            return dfs(node.left, targetSum) or dfs(node.right, targetSum)
        return dfs(root, targetSum)