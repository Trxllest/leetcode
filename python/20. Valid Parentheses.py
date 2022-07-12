class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_brackets = []
        brackets = {')':'(','}':'{',"]":"["}
        
        for b in s:
            if b in brackets:
                if open_brackets and open_brackets[-1] == brackets[b]:
                    open_brackets.pop()
                else:
                    return False
            else:
                open_brackets.append(b)
        return True if not open_brackets else False
            
 