class Solution(object):
    def diameterOfBinaryTree(self, root):
        diameter = [0] 
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            diameter[0] = max(diameter[0],left+right)
            return max(left,right)+1
        dfs(root)
        return diameter[0]
    