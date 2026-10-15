from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        queue = deque([root])
        sums = []
        while queue:
            total = 0
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            sums.append(total)
        return sums.index(max(sums)) + 1
