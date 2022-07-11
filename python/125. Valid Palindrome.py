class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lower_s = s.lower()
        new_s = []
        for char in lower_s:
            if char.isalnum():
                new_s.append(char)
        start,end = 0,len(new_s)-1
        
        while start <= end:
            if new_s[start] != new_s[end]:
                return False
            start += 1
            end -= 1
        return True
        