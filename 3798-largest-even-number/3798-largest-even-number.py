class Solution(object):
    def largestEven(self, s):
        """
        :type s: str
        :rtype: str
        """
        if "2" not in s:
            return ""
        s=s[::-1]
        s=s[s.index("2"):]
        return s[::-1]