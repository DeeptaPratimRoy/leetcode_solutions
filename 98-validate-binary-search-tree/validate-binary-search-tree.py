class Solution(object):
    def isValidBST(self, root):
        def bst(node, min_value, max_value):
            if node is None:
                return True
            if node.val <= min_value or node.val >= max_value:
                return False
            return bst(node.left, min_value, node.val) and bst(node.right, node.val, max_value)
        return bst(root, float('-inf'), float('inf'))