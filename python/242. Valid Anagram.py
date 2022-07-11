class Solution(object):
    
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        dict_s,dict_t = {},{}
        
        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i],0)
            dict_t[t[i]] = 1 + dict_t.get(t[i],0)
        
        for c in dict_s:
            if dict_s[c] != dict_t.get(c,0):
                return False
        return True

        #O(s+t) for both time and memory complexity 

        """
        #alternate solution would be to sort which would not take up extra space
        
        return sorted(s) == sorted(t)
        """
