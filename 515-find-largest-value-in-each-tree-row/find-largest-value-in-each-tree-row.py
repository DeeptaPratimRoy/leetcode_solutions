from collections import deque

class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        queue = deque([root])
        result = []
        while queue:
            large = float('-inf')
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                large = max(large, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(large)
        return result