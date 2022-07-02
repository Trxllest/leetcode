
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left,right = 0,len(nums)-1
        index = len(nums)-1
        solution = [0] *len(nums)
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                solution[index] = nums[left]*nums[left]
                index = index - 1
                left = left + 1
            else:
                solution[index] = nums[right] * nums[right]
                index = index - 1
                right = right - 1
        return solution