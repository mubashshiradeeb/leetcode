class Solution(object):
    def isSubstringPresent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=s[::-1]
        for i in range(len(s)-1):
            if str(s[i])+str(s[i+1]) in a:
                return True
        return False
            