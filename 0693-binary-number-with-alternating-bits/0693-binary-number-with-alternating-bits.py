class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n=str(bin(n)[2:])
        for i in range(len(n)-1):
            j=i+1
            if n[i]==n[j]:
                return False
        return True