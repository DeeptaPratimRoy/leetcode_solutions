# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        queue = deque([(root,None)])
        while queue:
            n = len(queue)
            px = py =None
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
            if px is not None or py is not None:
                if px is not None and py is not None and px!=py:
                    return True
                else:
                    return False
        return False