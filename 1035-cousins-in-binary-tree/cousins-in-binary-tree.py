class Solution:
    def isCousins(self, root, x, y):
        def dfs(node, parent, depth):
            if node is None:
                return
            if node.val == x:
                self.parent_x, self.depth_x = parent, depth
            if node.val == y:
                self.parent_y, self.depth_y = parent, depth
            dfs(node.left, node, depth + 1)
            dfs(node.right, node, depth + 1)
        self.parent_x = self.parent_y = None
        self.depth_x = self.depth_y = 0
        dfs(root, None, 0)
        return self.parent_x != self.parent_y and self.depth_x == self.depth_y