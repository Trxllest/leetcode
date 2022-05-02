"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.


Example 1:

Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: s = "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: s = "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' or ')'.
s is a valid parentheses string.
"""

class Solution:
    def __str__(self) -> str:
        pass
        
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        x = 0
        new_s = ''
        for i in s:
            if i =="(":
                stack.append(i)
                x = x + 1
            if i == ")":
                stack.append(i)
                x = x - 1
            if x == 0:
                stack.pop(0)
                stack.pop()
                new_s = new_s + "".join(stack)
                stack =[]
        return new_s

# Test Case
t1 = Solution()
x = t1.removeOuterParentheses("()(())(((())))(()())")
print(x)
#Expect:()((()))()()