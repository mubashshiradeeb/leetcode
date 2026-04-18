class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        a="".join(str(ord(char)-ord('a')+1) for char in s)
        res=sum(int(digit) for digit in a)
        for _ in range(k - 1):
            res=sum(int(digit) for digit in str(res))
        return res