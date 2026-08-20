class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        while i<n:
            n-=i
            i+=1
        if i==n:
            return i
        return i-1