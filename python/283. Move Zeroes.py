class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ptr = 0
        for i in range(0,len(nums)):
            if (nums[i] != 0):
                nums[ptr] = nums[i]
                ptr += 1
                
        if (ptr != len(nums)):
            for i in range(ptr, len(nums)):
                nums[i] = 0
                
    '''
    Test Cases
    [0,1,0,3,12]
    [0]
    [1]
    [1,2,3,4]
    [-1,0,3]
    '''