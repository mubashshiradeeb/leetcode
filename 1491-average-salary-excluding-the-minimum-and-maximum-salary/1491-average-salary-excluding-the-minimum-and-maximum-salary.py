class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        sum=0
        a=len(salary)
        for i in range(1,a-1):
            sum+=salary[i]
        return float(sum)/(a-2)