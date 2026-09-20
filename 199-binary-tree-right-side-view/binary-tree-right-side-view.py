from collections import deque
class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == n - 1:
                    result.append(node.val)
        return result