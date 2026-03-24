class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=1
        k=1
        while (2**k-1)<=n:
            k+=1
            count+=1
        return count