class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        b=[]
        for i in range(n+1):
            a=bin(i)[2:]
            b.append(a.count("1"))
        return b