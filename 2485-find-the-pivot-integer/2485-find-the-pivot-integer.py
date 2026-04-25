class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum1=(n*(n+1))//2
        x=int(math.sqrt(sum1))
        if x*x==sum1:
            return x
        return -1