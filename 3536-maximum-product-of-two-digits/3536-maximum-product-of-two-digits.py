class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        a="".join(sorted(str(n),reverse=True))
        return int(a[0])*int(a[1])