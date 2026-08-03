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
                new_level = len(queue)
                for i in range(new_level):
                    current = queue.popleft()
                    current_level.append(current.val)
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                result.append(current_level)
            return result
        return bfs(root)




            
        