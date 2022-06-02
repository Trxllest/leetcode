'''
Given the array prices where prices[i] is the price of the ith item in a shop.
There is a special discount for items in the shop, 
if you buy the ith item, then you will receive a discount equivalent to prices[j] 
where j is the minimum index such that j > i and prices[j] <= prices[i],
otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the 
ith item of the shop considering the special discount.

Example 1:

Input: prices = [8,4,6,2,3]
Output: [4,2,4,2,3]

Example 2:

Input: prices = [1,2,3,4,5]
Output: [1,2,3,4,5]
'''
class Solution:
    def __str__(self) -> str:
        pass
        
    def finalPrices(self, prices):
        stack = []
        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= prices[i]
            stack.append(i)
        return prices

t1 = Solution()
x = t1.finalPrices([8,4,6,2,3]) 
print(x)