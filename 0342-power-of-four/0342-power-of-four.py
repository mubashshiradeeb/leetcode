class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0: return False
        res=math.log(n, 4)
        return res.is_integer()