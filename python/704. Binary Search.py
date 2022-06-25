class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        len_nums = len(nums)
        left = 0
        right = len_nums-1
        middle = (left + right)//2 #other languages this can cause an error for large inputs (left+((right-left)//2)) fixes this
        while left <= right:
            middle = (left + right)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1
    