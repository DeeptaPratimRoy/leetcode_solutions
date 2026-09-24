from collections import deque
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        if root is None:
            return False
        queue = deque([(root,None)])
        while queue:
            px = py = None
            n= len(queue)
            for i in range(n):
                node,parent = queue.popleft()
                if node.val == x:
                    px = parent
                if node.val == y:
                    py = parent
                if node.left:
                    queue.append((node.left,node))
                if node.right:
                    queue.append((node.right,node))
            if px is not None and py is not None and px != py:
                return True
        return False
