class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max1=0
        for i in accounts:
            sum1=sum(i)
            if sum1>max1:
                max1=sum1
        return max1