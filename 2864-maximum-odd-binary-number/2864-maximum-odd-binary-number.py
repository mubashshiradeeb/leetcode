class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        s="".join(sorted(s))
        return s[:-1][::-1]+"1"