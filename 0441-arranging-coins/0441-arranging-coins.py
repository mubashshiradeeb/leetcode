class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=0
        while i<=n:
            n-=i
            i+=1
        return i-1