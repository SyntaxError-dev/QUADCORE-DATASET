# 1. We must define what a Node is so the code can run
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.total = 0

    def bstToGst(self, root):
        if root is not None:
            self.bstToGst(root.right)
            self.total += root.val
            root.val = self.total
            self.bstToGst(root.left)
        return root


    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol = Solution()
    new_root = sol.bstToGst(root)
    print(f"New Root Value: {new_root.val}") # Should be 5 (3+2)