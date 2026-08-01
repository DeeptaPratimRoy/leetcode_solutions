from collections import deque

class Solution(object):
    def levelOrder(self, root):
        def bfs(node):
            if node is None:
                return []

            queue = deque()
            queue.append(node)
            result = []
            while queue:
                current_level = []
                level_size = len(queue)
                for i in range(level_size):
                    current_node = queue.popleft()
                    current_level.append(current_node.val)
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
                result.append(current_level)
            return result
        return bfs(root)