class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic_nums = {}
        for n in nums:
            if n in dic_nums:
                return True
            else:
                dic_nums[n] = 0
        return False
    
    #O(n) worst case none of the values are duplicate must check whole list