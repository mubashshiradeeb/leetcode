class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        s="".join(sorted(s))
        s=s[:-1]
        s=s[::-1]
        return s+"1"