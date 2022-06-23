# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Recursive
        max_diameter = [0]
        def maxdepth(root):
            if not root:
                return 0
            left_height = maxdepth(root.left)
            right_height = maxdepth(root.right)
            diameter = left_height + right_height
            max_diameter[0] = max(diameter,max_diameter[0])
           
            return 1 + max(left_height,right_height)
        maxdepth(root)
        return max_diameter[0]