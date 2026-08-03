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
                current_list = []
                new_level = len(queue)
                for i in range(new_level):
                    current_element = queue.popleft()
                    current_list.append(current_element.val)
                    if current_element.left:
                        queue.append(current_element.left)
                    if current_element.right:
                        queue.append(current_element.right)
                result.append(current_list)
            return result
        return bfs(root)