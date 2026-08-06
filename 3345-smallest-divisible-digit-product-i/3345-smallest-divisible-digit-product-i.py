class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        import math
        while 1:
            product=1
            for i in str(n):
                product*=int(i)
            if product%t==0:
                return n
            n+=1