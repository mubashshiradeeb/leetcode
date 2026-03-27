class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        prod=1
        sum1=0
        for i in str(n):
            prod*=int(i)
            sum1+=int(i)
        return prod-sum1