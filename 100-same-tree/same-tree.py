class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        left_result = self.isSameTree(p.left, q.left)
        right_result = self.isSameTree(p.right, q.right)
        if left_result and right_result:
            return True
        else:
            return False