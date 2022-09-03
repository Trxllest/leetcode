# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        q = []
        # root.val = 0
        q.append(root)
        if not root:
            return False
        while q:
            curr = q.pop(0)
            if curr.left:
                q.append(curr.left)
                curr.left.val = curr.val+curr.left.val 
            if curr.right:
                q.append(curr.right)
                curr.right.val = curr.val+curr.right.val
            if (not curr.left) and (not curr.right) and (curr.val == targetSum):
                return True 
        return False