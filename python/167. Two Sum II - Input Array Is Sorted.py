


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        result = [0,0]
        for i in range(len(numbers)):
            sum = numbers[left] + numbers[right]
            if sum == target:
                result[0] = left + 1
                result[1] = right + 1
            elif sum < target:
                left = left + 1
            else:
                right = right - 1
        return result
    
    ## O(n)
        