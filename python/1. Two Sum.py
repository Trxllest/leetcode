class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # for x in range(len(nums)):
        #     for y in range(x+1,len(nums)):
        #         if (nums[x] + nums[y]) == target:
        #             return [x,y]
        # O(n^2)
        
        dict_num = {}
        for n in range(len(nums)):
            val = target-nums[n]
            if val in dict_num:
                return [dict_num[val],n]
            else:
                dict_num[nums[n]] = n
        """
        O(n) we traverse the nums list checking against our dictionary in one pass
        O(n) for memory since we are building the hashmap
        """
        
