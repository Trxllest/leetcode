# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root)[0]
    
    def dfs(self,root):
        if not root: 
            return [True,0] #the tree is balanced and the height is 0
        left,right = self.dfs(root.left),self.dfs(root.right)
        balanced = (left[0] and right[0] and 
                   abs(left[1]-right[1]) <=1)
        return [balanced,1+max(left[1],right[1])] #[balanced,i] index 1 is the current height and index 0 is whether or not the tree is balanced
    
    #O(h) worst case it is balanced and you check all levels on the way up
    
        
        
        
        