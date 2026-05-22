# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q) -> bool:
        while p and q:
            print(p.val, q.val)
            if p.val == q.val:
                if self.isSameTree(p.left, q.left) == False:
                    return False
                if self.isSameTree(p.right, q.right) == False:
                    return False
                break
            else:
                return False
        if p and not q or not p and q:
            return False
        return True
# Test the function
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
# p = TreeNode(1, TreeNode(2))
# q = TreeNode(1, None, TreeNode(2))
print(Solution().isSameTree(p, q))  # Output: True
