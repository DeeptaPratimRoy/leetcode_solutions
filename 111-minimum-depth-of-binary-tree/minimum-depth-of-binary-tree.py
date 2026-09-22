from collections import deque
class Solution:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        queue = deque([root])
        depth = 1
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            depth+=1


        