# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        levels = []
        q = []
        q.append(root)
        while q:
            toPop = len(q)
            temp = []
            while toPop > 0:
                curr = q.pop(0)
                temp.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                toPop -= 1
            levels.append(temp)
        return levels

"""
Time complex: O(n)
Space: O(n)
    
    1. Count the nodes at current level. 
    2. For every node, enqueue its children to queue.
"""