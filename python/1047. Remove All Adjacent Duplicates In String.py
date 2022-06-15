'''
You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.
It can be proven that the answer is unique.

Examples:
Input: s = "abbaca"
Output: "ca"

Input: s = "azxxzy"
Output: "ay"
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and s[i] == stack[-1]:
                stack.pop()
                #continue
            else:
                stack.append(s[i])
        return "".join(stack)


t1 = Solution()
x = t1.removeDuplicates("azxxzy")
print(x)

